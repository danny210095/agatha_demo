from models.user_context import UserContextManager
from models.flowise import FlowiseAgent

user_context_manager = UserContextManager()
flowise_agent = FlowiseAgent()

class MessageHandler:
    async def handle_message(self, user_id, group_id, user_input, reply_token):
        if group_id:
            user_mode = user_context_manager.get_user_mode(group_id, user_id)
            if user_mode == "呼叫模式" and "@bot" not in user_input:
                return None

            current_topic, _ = user_context_manager.get_user_context(user_id)
            if not current_topic:
                return "請先選擇主題（例如：我要問ESG）。"

            # 保存聊天记录
            user_context_manager.save_chat_history(current_topic, user_id, user_input)

            # 获取聊天历史
            conversation_history = user_context_manager.get_chat_history(current_topic, user_id)

            # 调用 Flowise Agent
            response = await flowise_agent.send_to_agent(
                current_topic, user_input, conversation_history
            )
            return response if response else "抱歉，未能獲取答案"

