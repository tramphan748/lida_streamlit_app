import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
import time
# from dataprep.clean import clean_headers, clean_missing, clean_date, clean_columns

# Import LIDA libraries
from lida import Manager, TextGenerationConfig, llm
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from PIL import Image

# Load environment variables
load_dotenv()


def load_api_key():
    """Load API Key from user input or environment variables."""
    # if "api_key" not in st.session_state:
    #     st.session_state.api_key = ""
    
    
    # # Select provider
    # provider = st.sidebar.selectbox("Provider",["Cohere", "Gemini"])
    
    
    # st.sidebar.subheader("Choose your provider and Enter API Key:")
    # if provider == "Cohere":
    # # Input API key
    #     api_key = st.sidebar.text_input(
    #         "API key:", value=st.session_state.api_key, type="password", placeholder="Enter your API key"
    #     )
    #     st.session_state.api_key = api_key
    # elif provider == "Gemini":
    #     api_key = st.sidebar.text_input(
    #         "API key:", value=st.session_state.api_key, type="password", placeholder="Enter your API key"
    #     )
    #     st.session_state.api_key = api_key
    # # Validate API key
    # if not api_key:
    #     st.warning("Please enter the API key to continue.")
    # else:
    #     pass
    #     # st.success("API key has been entered.")
    
    # Initialize session state for API keys if not exists
    if "cohere_api_key" not in st.session_state:
        st.session_state.cohere_api_key = ""
    if "gemini_api_key" not in st.session_state:
        st.session_state.gemini_api_key = ""
    
    with st.sidebar.popover(label=" ☑️:violet[Provider Instruction]"):
        st.info("""
            **Read this before you choose the provider:**  
            ###### You can only choose one provider throughout our services:
            - To change the provider, please close this tab and open the website again. 
            
            ###### If you primarily want to use the tasks :blue[UserQuery Based Graph] or :blue[VizRecommend]:
            - **Cohere**: Can generate between 1 to 5 charts, but they are not as detailed.
            - **Gemini**: Generates only 1 chart, but with more detailed information.
        """)


    st.sidebar.subheader("Choose your provider and Enter API Key:")
    # Select provider
    provider = st.sidebar.selectbox("Provider", ["Cohere", "Gemini"])
    # Handle API key input based on provider
    if provider == "Cohere":
        api_key = st.sidebar.text_input(
            "Cohere API key:", 
            value=st.session_state.cohere_api_key, 
            type="password", 
            placeholder="Enter your Cohere API key"
        )
        st.session_state.cohere_api_key = api_key
    else:
        api_key = st.sidebar.text_input(
            "Gemini API key:", 
            value=st.session_state.gemini_api_key, 
            type="password", 
            placeholder="Enter your Gemini API key"
        )
        st.session_state.gemini_api_key = api_key

    # Validate API key
    if not api_key:
        st.warning("Please enter the API key to continue.")
        

    return api_key, provider






def upload_file():
    """
    This function:
    - Uploads a dataset file in .csv or .json format
    - Reads input data for subsequent tasks
    """
    uploaded_file = st.file_uploader("Upload a data file in .csv format:", type=["csv"])
    if uploaded_file is not None:
        # Process the uploaded file
        if uploaded_file.name.endswith(".csv"):
            # Read CSV file
            df = pd.read_csv(uploaded_file)
            st.success(f"Successfully uploaded a CSV file with {len(df)} rows of data.")
        else:
            st.error("This format is not supported.")
        
        return df
    else:
        st.error("No data file found. Please try again.")
        return None


def clean_df(df):
    """
    Goal: Automate the data cleaning process for tasks such as replacing missing values and removing duplicates.
    
    Args:
        df (DataFrame): The dataset provided by the user

    Returns:
        cleaned_df: The cleaned dataset
    """
    df = df.copy()
    
    # Fill missing values for numerical columns with the mean value
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())
        
    # Remove duplicate values
    df = df.drop_duplicates()
    
    return df

# Convert base64 string to image
def base64_to_image(base64_str):
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data))
    return img

# Function to output, display code, explain, and evaluate the chart
def display_charts(
    lida, 
    chart, 
    goal, 
    library='seaborn', 
    textgen_config=None
):
    """
    Display, explain, and evaluate a chart in detail.

    Args:
        lida (Manager): LIDA manager
        chart (object): The chart to analyze
        goal (str): The goal of the chart
        library (str, optional): Charting library. Default is 'matplotlib'.
        textgen_config (TextGenerationConfig, optional): Text generation configuration. 
                                                         Default is None.
    """
    with st.spinner('Wait for it...'):
        time.sleep(5)
        # Check if chart exists
        if not chart:
            st.warning("No chart to display.")
            return

        # Convert chart to image
        try:
            img = base64_to_image(chart.raster)
        except Exception as e:
            st.error(f"Error converting chart: {e}")
            return

        # Display the chart image
        st.image(img)

        # Download button
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:image/png;base64,{img_str}" download="chart.png"> ˚⋆ ʕっ• ᴥ • ʔっ Download Chart ˚⋆ </a>'
        st.markdown(href, unsafe_allow_html=True)

        
        # Display VizOps
        with st.popover(label=":grey[⚙️ VizOps]"):
            code, explain, evaluations = st.tabs(["Code", "Explaination", "Evaluation"])
        
            # Display code
            with code:
                st.code(chart.code, language="python")

            # Explain the chart
            with explain:
                try:
                    explanations = lida.explain(
                        code=chart.code, 
                        library=library, 
                        textgen_config=textgen_config
                    )
                    for row in explanations[0]:
                        st.write(row["section"], " ** ", row["explanation"])
                except Exception as e:
                    st.error(f"Cannot explain the chart: {e}")

            # Evaluate the chart
            with evaluations:
                try:
                    evaluations = lida.evaluate(
                        code=chart.code,
                        goal=goal,
                        textgen_config=textgen_config,
                        library=library
                    )[0]
                    
                    for eval in evaluations:
                        st.write(
                            eval["dimension"],
                            "Score",
                            eval["score"],
                            "/ 10"
                        )
                        st.write(eval["rationale"])
                except Exception as e:
                    st.error(f"Cannot evaluate the chart: {e}")
