#!/bin/bash
# Fill WeChat fakeids for Business & Finance domain
# 
# Prerequisites:
# 1. wechat-download-api service running at http://localhost:18080
# 2. Already logged in via QR code scan
#
# Usage:
#   chmod +x scripts/fill_wechat_fakeids.sh
#   ./scripts/fill_wechat_fakeids.sh

API_BASE="http://localhost:18080"

# Business & Finance accounts to search
accounts=(
  "商隐社"
  "军武次位面"
  "功夫财经"
  "正和岛"
  "正商参考"
  "中国经营报"
  "MBA智库"
  "星海情报局"
)

echo "# Business & Finance WeChat Accounts - Fakeid Query Results"
echo "# Generated at: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Check API health
echo "Checking API health..."
health=$(curl -s "$API_BASE/api/health" 2>&1)
if [ -z "$health" ]; then
  echo "❌ Error: wechat-download-api is not running at $API_BASE"
  echo ""
  echo "Please start the service first:"
  echo "  cd /path/to/wechat-download-api"
  echo "  docker-compose up -d"
  echo ""
  echo "Then login via QR code:"
  echo "  open http://localhost:18080/login.html"
  exit 1
fi

echo "✅ API is running"
echo ""
echo "---"
echo ""

# Search each account
for account in "${accounts[@]}"; do
  echo "## $account"
  
  result=$(curl -s "$API_BASE/api/public/searchbiz?query=$account")
  
  if [ -z "$result" ]; then
    echo "❌ Error: Empty response"
    echo ""
    continue
  fi
  
  # Check if request succeeded
  ret=$(echo "$result" | jq -r '.ret // -1')
  
  if [ "$ret" != "0" ]; then
    err_msg=$(echo "$result" | jq -r '.err_msg // "Unknown error"')
    echo "❌ Error: $err_msg"
    echo ""
    continue
  fi
  
  # Parse first result
  list_count=$(echo "$result" | jq -r '.list | length')
  
  if [ "$list_count" -eq 0 ]; then
    echo "❌ No results found"
    echo ""
    continue
  fi
  
  # Extract info
  nickname=$(echo "$result" | jq -r '.list[0].nickname')
  fakeid=$(echo "$result" | jq -r '.list[0].fakeid')
  alias=$(echo "$result" | jq -r '.list[0].alias // "N/A"')
  
  echo "- **Name:** $nickname"
  echo "- **Fakeid:** \`$fakeid\`"
  echo "- **Alias:** $alias"
  echo ""
  
  # Suggest table row
  echo "Table row:"
  echo "| $nickname | \`$fakeid\` | $alias | TODO: Add description | TODO: Add use cases |"
  echo ""
  echo "---"
  echo ""
  
  # Rate limiting
  sleep 1
done

echo ""
echo "## Next Steps"
echo ""
echo "1. Copy the table rows above"
echo "2. Paste into \`references/wechat_accounts_registry.md\`"
echo "3. Fill in description and use cases"
echo "4. Commit and push:"
echo "   git add references/wechat_accounts_registry.md"
echo "   git commit -m 'feat: Add Business & Finance WeChat accounts'"
echo "   git push"
