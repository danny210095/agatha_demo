from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME

class GPTModel:
    def __init__(self):
        # 從配置中加載模型名稱和 API Key
        self.model = ChatOpenAI(model=OPENAI_MODEL_NAME, openai_api_key=OPENAI_API_KEY)

    def is_relevant_message(self, messages):
        """
        判斷訊息是否與當前話題相關。
        :param messages: 最近幾條群組訊息列表
        :return: True (相關) 或 False (不相關)
        """
        conversation = "\n".join(messages)
        response = self.model([
            HumanMessage(content=f"以下是群组的聊天内容：\n{conversation}\n"
                                 "請判斷是否有需要我處理的主題。如果有，返回「是」；否則返回「否」。")
        ])
        return "是" in response.content
