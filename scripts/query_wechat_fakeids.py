#!/usr/bin/env python3
"""
Query WeChat public account fakeids via wechat-download-api

Usage:
    python3 scripts/query_wechat_fakeids.py

Requirements:
    - wechat-download-api running at http://localhost:5000
    - Already logged in via QR code scan
"""

import requests
import json
import time
from datetime import datetime

API_BASE = "http://localhost:5000"

# Accounts to query
ACCOUNTS = [
    "商隐社",
    "军武次位面",
    "功夫财经",
    "正和岛",
    "正商参考",
    "中国经营报",
    "MBA智库",
    "星海情报局",
]

def check_health():
    """Check if API is running"""
    try:
        resp = requests.get(f"{API_BASE}/api/health", timeout=5)
        return resp.status_code == 200
    except:
        return False

def search_account(name):
    """Search for a WeChat public account"""
    url = f"{API_BASE}/api/public/searchbiz"
    params = {"query": name}
    
    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
        
        if data.get("success") and data.get("data", {}).get("list"):
            return data["data"]["list"]
        else:
            return None
    except Exception as e:
        print(f"  Error: {e}")
        return None

def main():
    print("# Business & Finance WeChat Accounts - Fakeid Query Results")
    print(f"# Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Check health
    print("Checking API health...")
    if not check_health():
        print(f"❌ Error: wechat-download-api is not running at {API_BASE}")
        print()
        print("Please start the service first:")
        print("  cd /path/to/wechat-download-api")
        print("  docker-compose up -d")
        print()
        print("Then login via QR code:")
        print(f"  open {API_BASE}/login.html")
        return
    
    print("✅ API is running")
    print()
    print("---")
    print()
    
    results = []
    
    for account in ACCOUNTS:
        print(f"## {account}")
        
        accounts = search_account(account)
        
        if not accounts:
            print("❌ No results found")
            print()
            continue
        
        # Get first result (most relevant)
        first = accounts[0]
        nickname = first.get("nickname", "N/A")
        fakeid = first.get("fakeid", "N/A")
        alias = first.get("alias", "N/A")
        
        print(f"- **Name:** {nickname}")
        print(f"- **Fakeid:** `{fakeid}`")
        print(f"- **Alias:** {alias}")
        print()
        
        # Generate table row
        table_row = f"| {nickname} | `{fakeid}` | {alias} | TODO: Add description | TODO: Add use cases |"
        print(f"Table row:\n{table_row}")
        print()
        print("---")
        print()
        
        results.append({
            "name": nickname,
            "fakeid": fakeid,
            "alias": alias
        })
        
        # Rate limiting
        time.sleep(0.5)
    
    # Print summary
    print()
    print("## Summary Table")
    print()
    print("| Name | fakeid | Alias | Description | Use Cases |")
    print("|------|--------|-------|-------------|-----------|")
    for r in results:
        print(f"| {r['name']} | `{r['fakeid']}` | {r['alias']} | TODO | TODO |")
    
    print()
    print("## Next Steps")
    print()
    print("1. Copy the table rows above")
    print("2. Paste into `references/wechat_accounts_registry.md`")
    print("3. Fill in description and use cases")
    print("4. Commit and push:")
    print("   git add references/wechat_accounts_registry.md")
    print("   git commit -m 'feat: Add Business & Finance WeChat accounts'")
    print("   git push")
    
    # Save to JSON
    output_file = "wechat_fakeids_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print()
    print(f"✅ Results saved to {output_file}")

if __name__ == "__main__":
    main()
