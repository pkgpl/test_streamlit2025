import streamlit as st


if "messages" not int st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role":"user","content":prompt})

    response = f"Echo: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role":"assistant", "content":response})
    