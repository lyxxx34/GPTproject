
"""
27-基于Streamlit和OpenAI API的聊天应用,支持对话记忆功能.

"""

from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ConversationSummaryBufferMemory
import warnings
import streamlit as st
from langchain_openai import ChatOpenAI



warnings.filterwarnings('ignore')



def get_ai_response(user_prompt):
    #用于构建带有对话记忆功能的聊天应用。
    # try:
    model = ChatOpenAI(
        model='gpt-4o-mini',
        api_key=st.session_state['API_KEY'],
        base_url='https://twapi.openai-hk.com/v1'
    )
    chain = ConversationChain(llm=model,memory=st.session_state['memory'])
    return chain.invoke({'input':user_prompt})['response']
    # except Exception as err:
        # return '暂时无法获取服务器响应：'

st.title('# 我的ChatGPT')

with st.sidebar:
    api_key = st.text_input('请输入自己专属的API秘钥：',type='password')
    st.session_state['API_KEY'] = api_key


if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'ai','content':'你好主人，我是你的AI助手，我叫小美'}]
    #用于实现完整保存所有历史对话信息的对话记忆策略。
    st.session_state['memory'] = ConversationBufferMemory(return_message=True)


for message in st.session_state['messages']:
    role,content = message['role'],message['content']
    st.chat_message(role).write(content)

user_input = st.chat_input()
if user_input:
    if not api_key:
        st.info('请输入专属秘钥！！！')
        st.stop()
    st.chat_message('human').write(user_input)
    st.session_state['messages'].append({'role':'human','content':user_input})
    with st.spinner('AI正在思考，请等待...'):
        resp_from_ai = get_ai_response(user_input)
        st.session_state['history'] = resp_from_ai
        st.chat_message('ai').write(resp_from_ai)  # 信息框
        st.session_state['messages'].append({'role': 'ai', 'content': resp_from_ai})


