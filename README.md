
# Agatha demo

## 簡介
此專案是一個基於 **LINE Messaging API** 和 **Flowise AI** 的智能聊天機器人。支持多主題對話，包括：
- ESG 問答
- IT 開發需求顧問
- 企業徵信
- 資安諮詢顧問

## 專案結構

```plaintext
project/
├── main.py                    # 主入口檔案，負責啟動 FastAPI 應用
├── config.py                  # 配置檔案，管理全域配置和密鑰
├── models/                    # 模型相關程式碼目錄
│   ├── database.py            # MongoDB 相關操作封裝
│   ├── flowise.py             # Flowise API 操作類，用於與不同 Agent 通信
│   ├── gpt.py                 # GPT 模型操作類，用於處理自然語言分析
│   └── user_context.py        # 使用者模式與主題管理類
└── utils/                     # 工具類程式碼目錄
    ├── message_handler.py     # 訊息解析與分發邏輯，結合使用者上下文處理訊息
    └── linebot_api.py         # LINE Messaging API 操作封裝
```

---

## 目錄說明

1. **`main.py`**  
   - 專案的入口檔案，啟動 FastAPI 服務並定義 Webhook 路由。

2. **`config.py`**  
   - 管理專案的全域配置，包括 API 金鑰、資料庫 URI 以及各 Agent 的設定。

3. **`models/`**  
   - **`database.py`**：封裝 MongoDB 資料庫操作，提供連線與集合管理功能。
   - **`flowise.py`**：Flowise API 的操作封裝類，根據主題調用對應的 Agent。
   - **`gpt.py`**：封裝 GPT 模型的調用邏輯，用於訊息相關性判斷等功能。
   - **`user_context.py`**：負責管理使用者的模式、主題與聊天歷史。

4. **`utils/`**  
   - **`message_handler.py`**：主要邏輯入口，根據使用者模式與主題分發訊息，調用 Flowise 和 GPT。
   - **`linebot_api.py`**：封裝 LINE Messaging API 的操作，包括訊息發送與回覆。

---

## 使用範例

### 1. 安裝依賴
確保安裝了專案所需的依賴，並執行以下命令：
```bash
pip install -r requirements.txt
```

### 2. 配置環境變數
在 `.env` 文件或伺服器環境中設置以下變數：
```plaintext
OPENAI_API_KEY=你的_openai_api_key
LINE_CHANNEL_SECRET=你的_line_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=你的_line_channel_access_token
MONGODB_URI=你的_mongodb_connection_string
```

### 3. 啟動服務
執行以下命令啟動 FastAPI 服務：
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. 配置 LINE Bot Webhook
在 LINE Developer 平台中配置 Webhook 地址為：
```
https://<你的域名>/webhooks/line
```

---

## 功能特點

1. **多主題支持**  
   - 支持 ESG 問答、IT 顧問、企業徵信、資安諮詢等多種主題。
   - 每個主題獨立使用 Flowise Agent 和 MongoDB 集合管理聊天歷史。

2. **智能分發**  
   - 根據使用者輸入，自動分發到對應的 Agent。

3. **LINE 群組和個人對話模式**  
   - 支持群組的 `呼叫模式` 和 `主動模式`，可根據使用者需求自由切換。

---

## 範例場景

### 群組對話
- **使用呼叫模式：**
  - 使用者輸入 `@bot 我想了解ESG的合規要求`，機器人返回 ESG 的相關回答。
  
- **使用主動模式：**
  - 機器人根據群組話題，自動檢測是否需要回覆。

### 個人對話
- 使用者輸入：`請問IT開發需要什麼資源？`
- 機器人返回相關建議，並根據上下文進行多輪對話。

---

## 貢獻者
如果您對此專案有任何建議或希望進行貢獻，歡迎提交 Issue 或 Pull Request。

---

## 授權
此專案基於 [MIT License](LICENSE) 授權，歡迎自由使用與修改。
