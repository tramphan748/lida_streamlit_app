import streamlit as st

def show_API_key():
   
    cohere, gemini = st.tabs(["🖇COHERE", "🌎 GEMINI"])
    with cohere:
        st.header("🖇 _:violet[COHERE APIs KEY:]_")
        st.write("""Calls made using Trial keys are free of charge. Trial keys are rate-limited, and cannot be used for commercial purposes.
                 Remember to use API keys securely. Don't share or embed them in public code. 
                 """)
        st.divider()
        st.markdown("#### Step 1: Visit the following link: *[Cohere Website](https://dashboard.cohere.com/welcome/login)* and sign up if you don’t already have an account.")
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

    with gemini:
        st.header("🌎 _:blue[GEMINI APIs KEY:]_")
        st.write("Calls made using Trial keys are free of charge. Trial keys are rate-limited, and cannot be used for commercial purposes. Remember to use API keys securely. Don't share or embed them in public code.")
        st.divider()
        st.markdown("#### Step 1: Visit the following link: *[GoogleAI Website](https://ai.google.dev/gemini-api/docs?_gl=1*ukm4s0*_ga*MjAyODgwMzE2NC4xNzM1MzgwNTcw*_ga_P1DBVKWT6V*MTczNTQ0MTI3OS40LjEuMTczNTQ0Mzg5Ni4zMy4wLjExMTc0NzU1MjE.)* and sign up if you don’t already have an account.")
        st.image("material/gemini-web/1.png", caption="Figure 1. Login Interface")
        
        st.divider()
        st.markdown(
            """ 
            #### Step 2:  In the left sidebar of the interface, click on the :blue[API KEY] section.
            """
        )
        st.image("material/gemini-web/2.png", caption="Figure 2.Instruction to get API KEY")
        
        
        st.divider()
        st.markdown(
            """ 
            #### Step 3: Click on :blue-background["Get a Gemini API key in Google AI Studio"] button to proceed to the next step.
            """
        )
        st.image("material/gemini-web/3.png", caption="Figure 3. Instruction to Get API KEY")
        
        st.divider()
        st.markdown(
            """ 
            #### Step 4: After completing Step 3, you will be redirected to a new page that looks like the image below. Click on the :blue[API KEY] section to retrieve your API key!
            """
        )
        st.image("material/gemini-web/4.png", caption="Google AI studio website")
        
        
        st.divider()
        st.markdown(
            """ 
            #### Step 5: Tap on the button :blue-background["Copy"] to get your own API KEY. Now, you can enter it and enjoy our service!
            """
        )
        st.image("material/gemini-web/5.png", caption="Figure 5. Last Step to call your API KEY")
        
        
        st.warning(
            """ 
            **A few notes when using :blue[GEMINI]:** \n

            Since this project is designed for users who may not specialize in AI or data-related fields:
            - We prioritize cost-effective solutions.
            - For our project, GEMINI offers a free tier with limited access. Be aware that usage beyond the free limit may incur additional charges, so it's important to monitor your API calls.
            - Gemini-1.5-Flash family: Free of charge, up to 1 million tokens of storage per hour
            - Because GEMINI API has rate limits. We recommend reviewing your usage regularly to avoid hitting those limits.
            """
        )
show_API_key()
