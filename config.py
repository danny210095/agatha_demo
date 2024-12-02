# 配置文件

# LINE Messaging API
CHANNEL_SECRET = '05385042f1a323bf022b74be469abc74'
CHANNEL_ACCESS_TOKEN = 'CD3fBCvin8ifnta+Q7+golm4/LvVCrFke5HOImJvHR8iBTqCDNFSjo9CH6m4jg2HnaPssthXXgX8cLUjrZL06prQo5rQ51ycqfzMA4St2MqGo3mKtUXtXkvqR9OOKrNeGvO7ELhhBnyLF5iOzhGiBwdB04t89/1O/w1cDnyilFU=EN'

# MongoDB 配置
MONGODB_URI = 'mongodb+srv://emergence:emergence@chatbot.xm0ea.mongodb.net/?retryWrites=true&w=majority&appName=ChatBot'

# Flowise Endpoints 與 Chat memory collections 設定
BOT_CONFIG = {
    "ESG": {
        "endpoint": "https://flowise.agatha-ai.com/api/v1/prediction/1dc3fa73-ea42-466a-b642-f8a003f36146",
        "collection": "ESGBotChatHistory"
    },
    "IT": {
        "endpoint": "https://flowise.agatha-ai.com/api/v1/prediction/72c0a572-6cc1-4db7-812f-5a7a17057149",
        "collection": "ITBotChatHistory"
    },
    "Credit": {
        "endpoint": "https://flowise.agatha-ai.com/api/v1/prediction/dfde5edd-70bd-4e54-8ae9-ee76c8c8d409",
        "collection": "LeadsBotChatHistory"
    },
    "Cybersecurity": {
        "endpoint": "https://flowise.agatha-ai.com/api/v1/prediction/0b2334fb-1b1b-4453-a32c-9d9c3a028c07",
        "collection": "CybersecurityBotChatHistory"
    }
}

# 默認模式
DEFAULT_MODE = "呼叫模式"
