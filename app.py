import streamlit as st

def main():
    st.set_page_config(page_title = "Chat with the documents", page_icon=":books:")
    st.header("Chat with the documents :books:")
    st.text_input("Ask a question:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your documents here and click on Process")
        st.button("Process")

    
if __name__ == '__main__':
    main()