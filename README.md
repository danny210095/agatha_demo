# agatha_demo

## Directory
project/
├── main.py                    # 主入口文件
├── config.py                  # 配置文件
├── models/
│   ├── database.py            # MongoDB 相關操作
│   ├── flowise.py             # Flowise API
│   ├── gpt.py                 # GPT 模型
│   └── user_context.py        # 用戶模式和主題管理
└── utils/
    ├── message_handler.py     # 消息解析和分發邏輯
    └── linebot_api.py         # LINE Messaging API 操作封裝
