import streamlit as st
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import (
    DuckDuckGoSearchRun,
    ArxivQueryRun,
    WikipediaQueryRun,
    YahooFinanceNewsTool
)
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper

def initialize_tools():
    return [
        DuckDuckGoSearchRun(name="Search"),
        YahooFinanceNewsTool(),
        ArxivQueryRun(api_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)),
        WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200))
    ]

def create_chat_interface():
    st.title("Langchain Search Engine With llama")
    api_key = st.sidebar.text_input("Enter your groq api key:", type="password")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
        ]
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    return api_key

def main():
    api_key = create_chat_interface()
    
    if prompt := st.chat_input(placeholder="What is machine learning?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
        tools = initialize_tools()
        
        search_agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handling_parsing_errors=True
        )
        
        with st.chat_message("assistant"):
            response = search_agent.run(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)

if __name__ == "__main__":
    main()
