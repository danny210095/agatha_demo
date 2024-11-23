from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

class GPTModel:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.model = ChatOpenAI(model=model_name)

    def is_relevant_message(self, messages):
        conversation = "\n".join(messages)
        response = self.model([
            HumanMessage(content=f"以下是群组的聊天内容：\n{conversation}\n"
                                 "请判断是否有需要我处理的主题。如果有，返回'是'；否则返回'否'。")
        ])
        return "是" in response.content
