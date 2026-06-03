# WeChat Public Accounts Registry (微信公众号账号库)

This file pre-defines high-quality WeChat public accounts by vertical domain to reduce account discovery time during research.

## How to Get fakeid

Before filling this registry, you need to get the `fakeid` for each public account:

### Method 1: Use wechat-download-api (Recommended)

```bash
# Search for public account
curl "http://localhost:18080/api/public/searchbiz?query=公众号名称"

# Response example:
# {
#   "ret": 0,
#   "list": [
#     {
#       "fakeid": "MzIwNzQxMjM0NQ==",
#       "nickname": "摇滚客",
#       "alias": "rockchinamusic",
#       "round_head_img": "https://..."
#     }
#   ]
# }

# Copy the "fakeid" field to this registry
```

### Method 2: Use wechat-query skill

If you have `wechat-query` skill installed in QClaw:

```
Ask QClaw: "Search WeChat public account: 摇滚客"
```

The skill will return the fakeid automatically.

---

## Registry Structure

Each entry has the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| `name` | Public account display name | 摇滚客 |
| `fakeid` | Unique identifier (from searchbiz API) | MzIwNzQxMjM0NQ== |
| `alias` | WeChat ID (optional) | rockchinamusic |
| `description` | What this account covers | 音乐资讯、乐队访谈、演出信息 |
| `use_cases` | When to use this source | 音乐行业动态、演出信息、乐队访谈 |

---

## Vertical Domains

### 1. 文娱/娱乐 (Entertainment & Music)

**Music & Concerts:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| 摇滚客 | `TODO: fill` | - | 摇滚音乐资讯、乐队访谈 | 音乐行业动态、演出信息 |
| 音乐财经 | `TODO: fill` | - | 音乐产业商业报道 | 音乐行业商业分析、市场趋势 |
| 网易云音乐 | `TODO: fill` | - | 音乐平台动态、歌单推荐 | 音乐平台运营、用户趋势 |
| TODO: Add more | - | - | - | - |

**Movies & TV:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| 豆瓣电影 | `TODO: fill` | - | 电影评分、影评 | 电影行业分析、用户偏好 |
| TODO: Add more | - | - | - | - |

**Performing Arts:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 2. 财经/金融 (Finance & Economy)

**General Finance:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| 财经杂志 | `TODO: fill` | - | 深度财经报道 | 宏观经济、政策解读 |
| 36氪 | `TODO: fill` | - | 科技财经、创业投资 | 创投动态、融资信息 |
| 虎嗅APP | `TODO: fill` | - | 商业科技评论 | 商业模式分析、行业洞察 |
| TODO: Add more | - | - | - | - |

**Investment & Stock:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 3. 体育 (Sports)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 4. 医疗/健康 (Healthcare & Medical)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 5. 教育 (Education)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 6. 科技/AI (Technology & AI)

**Already covered in `source_registry_ai_events.md` - see that file for AI-specific accounts.**

**General Tech:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| 36氪 | `TODO: fill` | - | 科技财经 | 科技行业动态、创投信息 |
| 量子位 | `TODO: fill` | - | AI 前沿技术 | AI 技术进展、产业应用 |
| 机器之心 | `TODO: fill` | - | AI 技术报道 | AI 技术、产品、研究 |
| TODO: Add more | - | - | - | - |

---

### 7. 游戏 (Gaming)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 8. 汽车出行 (Automotive & Transportation)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 9. 房产/地产 (Real Estate)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 10. 消费/零售 (Consumer & Retail)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 11. 法律/政策 (Law & Policy)

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| TODO: Add | - | - | - | - |

---

### 12. 其他垂直领域 (Other Verticals)

| Domain | Name | fakeid | Description | Use Cases |
|--------|------|--------|-------------|-----------|
| Energy | TODO: Add | - | - | - |
| Agriculture | TODO: Add | - | - | - |
| Environment | TODO: Add | - | - | - |

---

## Usage Instructions

### For Skill Developers

When implementing domain-specific research:

1. **Check this registry first** - Look up pre-defined accounts for the target domain
2. **Use fakeid directly** - Skip `searchbiz` discovery if fakeid is already known
3. **Subscribe to accounts** - Use `/api/rss/subscribe` with fakeid
4. **Fetch articles** - Use `/api/public/articles?fakeid=xxx`

### For Users

To contribute new accounts to this registry:

1. **Search for the public account** using `searchbiz` API
2. **Copy the fakeid** from the response
3. **Add to this file** following the table format
4. **Submit a PR** or update your local copy

---

## Maintenance Notes

- **Update frequency**: As needed when new high-quality accounts are discovered
- **Validation**: Periodically check if accounts are still active
- **Coverage**: Aim for 3-5 high-quality accounts per vertical domain
- **Quality criteria**: Official accounts, high follower count, frequent updates, authoritative content

---

## Example: How to Fill This Registry

### Step-by-Step Guide

**Example: Adding "摇滚客" to Music domain**

1. **Search for the account:**
```bash
curl "http://localhost:18080/api/public/searchbiz?query=摇滚客"
```

2. **Parse the response:**
```json
{
  "ret": 0,
  "list": [
    {
      "fakeid": "MzIwNzQxMjM0NQ==",
      "nickname": "摇滚客",
      "alias": "rockchinamusic",
      "round_head_img": "https://..."
    }
  ]
}
```

3. **Fill the table:**

**Before:**
```markdown
| 摇滚客 | `TODO: fill` | - | 摇滚音乐资讯、乐队访谈 | 音乐行业动态、演出信息 |
```

**After:**
```markdown
| 摇滚客 | `MzIwNzQxMjM0NQ==` | rockchinamusic | 摇滚音乐资讯、乐队访谈 | 音乐行业动态、演出信息 |
```

4. **Commit and push:**
```bash
git add references/wechat_accounts_registry.md
git commit -m "feat: Add 摇滚客 to Music domain"
git push
```

---

## Integration with source_registry.md

This file is referenced by `source_registry.md` when:

- User requests domain-specific news (e.g., "音乐行业新闻")
- User needs industry-specific information (e.g., "财经政策解读")
- User asks for vertical-specific events (e.g., "音乐节活动")

**The skill will:**

1. Look up pre-defined accounts in this registry
2. Use fakeid to fetch articles directly
3. Skip the discovery step → Faster results!

---

## Future Enhancements

- [ ] Add more vertical domains
- [ ] Add automated validation (check if accounts are still active)
- [ ] Add RSS feed URLs for accounts that support it
- [ ] Add last_updated timestamp for each account
- [ ] Add multi-language support for account descriptions
