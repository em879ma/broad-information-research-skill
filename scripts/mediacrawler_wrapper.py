#!/usr/bin/env python3
"""
MediaCrawler 封装脚本 - 简化调用接口
为 broad-information-research-skill 提供统一的 MediaCrawler 调用方式
"""

import subprocess
import sys
import json
import os
from pathlib import Path
from datetime import datetime

# MediaCrawler 仓库路径
MEDIACRAWLER_PATH = Path("/Users/zhuoyuwei/MediaCrawler")

# 平台名称映射
PLATFORM_MAP = {
    "xiaohongshu": "xhs",
    "xhs": "xhs",
    "小红书": "xhs",
    "douyin": "dy",
    "dy": "dy",
    "抖音": "dy",
    "kuaishou": "ks",
    "ks": "ks",
    "快手": "ks",
    "bilibili": "bili",
    "bili": "bili",
    "b站": "bili",
    "哔哩哔哩": "bili",
    "weibo": "wb",
    "wb": "wb",
    "微博": "wb",
    "tieba": "tieba",
    "贴吧": "tieba",
    "baidu_tieba": "tieba",
    "zhihu": "zhihu",
    "知乎": "zhihu",
}


def get_platform_code(platform: str) -> str:
    """将平台名称转换为 MediaCrawler 内部代码"""
    platform_lower = platform.lower().strip()
    return PLATFORM_MAP.get(platform_lower, platform_lower)


def run_crawler(
    platform: str,
    keywords: str,
    max_notes: int = 20,
    crawl_type: str = "search",
    login_type: str = "qrcode",
    output_format: str = "jsonl"
) -> dict:
    """
    运行 MediaCrawler 爬取数据
    
    Args:
        platform: 平台名称（支持中文或英文代码）
        keywords: 搜索关键词
        max_notes: 最大爬取数量
        crawl_type: 爬取类型 (search/creator/feed)
        login_type: 登录方式 (qrcode/cookie)
        output_format: 输出格式 (jsonl/csv)
    
    Returns:
        dict: {"success": bool, "data_file": str, "error": str}
    """
    
    platform_code = get_platform_code(platform)
    
    # 验证平台是否支持
    if platform_code not in PLATFORM_MAP.values():
        return {
            "success": False,
            "error": f"不支持的平台: {platform}，支持的平台: {list(set(PLATFORM_MAP.values()))}"
        }
    
    # 确保在 MediaCrawler 目录下运行
    if not MEDIACRAWLER_PATH.exists():
        return {
            "success": False,
            "error": f"MediaCrawler 目录不存在: {MEDIACRAWLER_PATH}"
        }
    
    # 构建命令
    cmd = [
        "uv", "run", "python", "main.py",
        "--platform", platform_code,
        "--lt", login_type,
        "--type", crawl_type,
        "--keywords", keywords,
        "--crawler_max_notes_count", str(max_notes),
    ]
    
    print(f"🚀 启动 MediaCrawler...")
    print(f"   平台: {platform_code}")
    print(f"   关键词: {keywords}")
    print(f"   最大数量: {max_notes}")
    print(f"   命令: {' '.join(cmd)}")
    print()
    
    try:
        # 切换工作目录并执行
        result = subprocess.run(
            cmd,
            cwd=MEDIACRAWLER_PATH,
            capture_output=True,
            text=True,
            timeout=300  # 5分钟超时
        )
        
        if result.returncode != 0:
            return {
                "success": False,
                "error": f"爬取失败 (返回码 {result.returncode}):\n{result.stderr}"
            }
        
        # 查找输出文件
        data_dir = MEDIACRAWLER_PATH / "data" / platform_code / "jsonl"
        if not data_dir.exists():
            return {
                "success": True,
                "warning": "爬取成功但未找到输出文件",
                "data_file": None
            }
        
        # 获取最新的 jsonl 文件
        jsonl_files = sorted(data_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True)
        
        if not jsonl_files:
            return {
                "success": True,
                "warning": "爬取成功但未找到 .jsonl 文件",
                "data_file": None
            }
        
        latest_file = jsonl_files[0]
        
        # 读取并统计结果
        with open(latest_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        return {
            "success": True,
            "data_file": str(latest_file),
            "total_items": len(lines),
            "platform": platform_code,
            "keywords": keywords,
            "output_preview": [json.loads(line) for line in lines[:3]] if lines else []
        }
        
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "爬取超时（5分钟），请检查网络连接或增加超时时间"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"执行失败: {str(e)}"
        }


def batch_crawl(platforms: list, keywords: str, max_notes: int = 20) -> dict:
    """
    批量爬取多个平台
    
    Args:
        platforms: 平台列表
        keywords: 搜索关键词
        max_notes: 每个平台最大爬取数量
    
    Returns:
        dict: {"results": [...], "summary": {...}}
    """
    results = []
    success_count = 0
    
    for platform in platforms:
        print(f"\n{'='*60}")
        print(f"📱 正在爬取平台: {platform}")
        print(f"{'='*60}")
        
        result = run_crawler(platform, keywords, max_notes)
        results.append({
            "platform": platform,
            "result": result
        })
        
        if result.get("success"):
            success_count += 1
        
        print()  # 空行分隔
    
    return {
        "results": results,
        "summary": {
            "total_platforms": len(platforms),
            "success_count": success_count,
            "failed_count": len(platforms) - success_count
        }
    }


def list_supported_platforms() -> list:
    """列出所有支持的平台"""
    return list(set(PLATFORM_MAP.values()))


def check_mediacrawler_status() -> dict:
    """检查 MediaCrawler 安装状态"""
    status = {
        "installed": MEDIACRAWLER_PATH.exists(),
        "path": str(MEDIACRAWLER_PATH),
        "uv_available": False,
        "playwright_ready": False,
    }
    
    if status["installed"]:
        # 检查 uv
        try:
            result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
            status["uv_available"] = result.returncode == 0
        except:
            pass
        
        # 检查 Playwright 浏览器
        chromium_path = MEDIACRAWLER_PATH / "chromium-1134"  # 版本号可能不同
        status["playwright_ready"] = chromium_path.exists() or (
            MEDIACRAWLER_PATH / ".venv" / "bin" / "playwright"
        ).exists()
    
    return status


if __name__ == "__main__":
    # CLI 接口
    import argparse
    
    parser = argparse.ArgumentParser(description="MediaCrawler 封装脚本")
    parser.add_argument("--platform", "-p", required=True, help="平台名称")
    parser.add_argument("--keywords", "-k", required=True, help="搜索关键词")
    parser.add_argument("--max-notes", "-n", type=int, default=20, help="最大爬取数量")
    parser.add_argument("--type", "-t", default="search", help="爬取类型 (search/creator/feed)")
    parser.add_argument("--check", action="store_true", help="检查安装状态")
    parser.add_argument("--list-platforms", action="store_true", help="列出支持的平台")
    
    args = parser.parse_args()
    
    if args.check:
        status = check_mediacrawler_status()
        print(json.dumps(status, indent=2, ensure_ascii=False))
    elif args.list_platforms:
        platforms = list_supported_platforms()
        print("支持的平台:")
        for p in sorted(platforms):
            print(f"  - {p}")
    else:
        result = run_crawler(args.platform, args.keywords, args.max_notes, args.type)
        print(json.dumps(result, indent=2, ensure_ascii=False))
