import logging
import asyncio
from fastapi import FastAPI, Request, HTTPException
from linebot.v3.webhook import WebhookParser
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage
)
from config import CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from utils.message_handler import MessageHandler
from models.user_context import UserContextManager

app = FastAPI()
parser = WebhookParser(CHANNEL_SECRET)
line_bot_api = AsyncMessagingApi(AsyncApiClient(Configuration(access_token=CHANNEL_ACCESS_TOKEN)))

message_handler = MessageHandler()
user_context_manager = UserContextManager()

@app.post("/webhooks/line")
async def handle_callback(request: Request):
    signature = request.headers.get('X-Line-Signature')
    if not signature:
        raise HTTPException(status_code=400, detail="Missing X-Line-Signature")

    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessageContent):
            user_id = event.source.user_id
            group_id = event.source.group_id if hasattr(event.source, "group_id") else None
            user_input = event.message.text
            reply_token = event.reply_token

            response = await message_handler.handle_message(user_id, group_id, user_input, reply_token)
            if response:
                await line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[TextMessage(text=response)]
                    )
                )

    return {"message": "OK"}
