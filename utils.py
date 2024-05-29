from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

def get_chat_response(prompt, memory):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="sk-Kvfp4z4xqFMKa86A5dDfC1Df654941A4A9B508B4496fDc74"
                       ,openai_api_base="https://api.aigc369.com/v1")
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", f"你是一个非常暴躁的智能助手，说话经常阴阳怪气，惹人们生气"),
         MessagesPlaceholder(variable_name="history"),
         ("human", "{input}")
         ]
    )

    chain = ConversationChain(llm=model, memory=memory, prompt=prompt_template)

    response = chain.invoke({"input": prompt})
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问题是什么？", memory, os.getenv("OPENAI_API_KEY")))
