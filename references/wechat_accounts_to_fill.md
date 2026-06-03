# WeChat Accounts - Business & Finance Domain

**Status:** Waiting for fakeid lookup

## How to Fill

### Step 1: Start wechat-download-api

```bash
cd /path/to/wechat-download-api
docker-compose up -d
```

### Step 2: Login via QR Code

```bash
open http://localhost:18080/login.html
```

Scan the QR code with WeChat.

### Step 3: Run the Query Script

```bash
cd /Users/zhuoyuwei/broad-information-research-skill
./scripts/fill_wechat_fakeids.sh
```

### Step 4: Copy Results to Registry

Copy the table rows from the script output and paste into `references/wechat_accounts_registry.md`.

---

## Accounts to Add

### Business & Finance (商业财经)

1. **商隐社**
   - Description: 深度商业报道
   - Use cases: 商业模式分析、企业案例研究

2. **军武次位面**
   - Description: 军事科技、国际局势
   - Use cases: 军事装备、地缘政治分析

3. **功夫财经**
   - Description: 财经评论、投资观点
   - Use cases: 投资策略、财经热点解读

4. **正和岛**
   - Description: 企业家社群、商业思想
   - Use cases: 企业家访谈、管理思想

5. **正商参考**
   - Description: 商业资讯、行业分析
   - Use cases: 行业趋势、商业洞察

6. **中国经营报**
   - Description: 财经新闻、企业经营
   - Use cases: 企业动态、宏观经济

7. **MBA智库**
   - Description: 管理知识、商业案例
   - Use cases: 管理理论、案例分析

8. **星海情报局**
   - Description: 商业情报、行业研究
   - Use cases: 竞品分析、市场研究

---

## Expected Output Format

After running the script, you'll get output like:

```markdown
| 商隐社 | `MzIwNzQxMjM0NQ==` | shangyinshe | 深度商业报道 | 商业模式分析、企业案例研究 |
| 军武次位面 | `MzI1NjQyODk3MQ==` | junwu123 | 军事科技、国际局势 | 军事装备、地缘政治分析 |
...
```

Copy these rows and paste into `wechat_accounts_registry.md` under the "财经/金融" section.

---

## Quick Manual Method

If you prefer manual lookup:

```bash
# For each account:
curl "http://localhost:18080/api/public/searchbiz?query=商隐社" | jq '.'

# Copy the fakeid from the response
# Paste into the registry table
```

---

## Registry File Location

```
/Users/zhuoyuwei/broad-information-research-skill/references/wechat_accounts_registry.md
```

Find the section:

```markdown
### 2. 财经/金融 (Finance & Economy)

**General Finance:**

| Name | fakeid | Alias | Description | Use Cases |
|------|--------|-------|-------------|-----------|
| 财经杂志 | `TODO: fill` | - | 深度财经报道 | 宏观经济、政策解读 |
```

Replace `TODO: fill` with the actual fakeid.
