import aiohttp
import logging
from config import BOT_CONFIG

class FlowiseAgent:
    async def send_to_agent(self, topic, user_input, conversation_history):
        endpoint = BOT_CONFIG[topic]["endpoint"]
        if not endpoint:
            return "當前主題暫不支持。"

        async with aiohttp.ClientSession() as session:
            payload = {
                "question": user_input,
                "history": conversation_history
            }
            try:
                async with session.post(endpoint, json=payload) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("text", "無回應")
            except Exception as e:
                logging.error(f"Flowise 請求失敗: {e}")
                return None

