import streamlit as st

def show_API_key():
    st.header("── .✦_:blue[COHERE API KEY:]_")
    st.markdown("""
                After experimenting with various :blue-background[large language models], we found that the :violet[command-xlarge-nightly] model from Cohere provides the best performance. 
                Here, we’ll guide you *step-by-step* on how to retrieve your Cohere API key.
                """)
    st.divider()
    st.markdown("#### Step 1: Visit this link: *[Cohere Website](https://dashboard.cohere.com/welcome/login)* and sign up if you don’t already have an account.")
    st.image("material/cohere-web/log_in.png", caption="Figure 1. Login Interface")

    st.markdown("""
                Once you’ve logged in successfully, you’ll see the Cohere *dashboard* as shown below:
                """)
    st.image("material/cohere-web/cohere-dashboard.png", caption="Figure 2. Dashboard Interface")

    st.divider()
    st.markdown("#### Step 2: On the left side of the dashboard, look for the :gray[API KEY] section. Click on it: ")
    st.image("material/cohere-web/cohere-b2.png", caption="Figure 3. API KEY Section")

    st.divider()
    st.markdown("#### Step 3: Save your :blue[API KEY] and enter it in the :blue[Enter API KEY:] field on the :red[Features] page.")
    st.image("material/cohere-web/cohere-b3.png", caption="Figure 4. Save your API key to use for future tasks.")

    st.warning("""
            **A few notes when using :violet[COHERE]:**  \n
            Since this project is designed for users who may not specialize in data-related fields:  
            - We prioritize cost-effective solutions.  
            - For our project, :violet[COHERE] allows up to 1000 free requests per month.
            """)

show_API_key()
