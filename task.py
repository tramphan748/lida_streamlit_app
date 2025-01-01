import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import time
import os

# Import LIDA library
from lida import Manager, TextGenerationConfig, llm

# Import helper functions from the helpers directory
from helpers.helpers import (
    upload_file,
    clean_df,
    load_api_key,
    base64_to_image,
    display_charts
)

# Load environment variables
load_dotenv()




# Set up textgen config
def setup_model_textgen(models, provider):
    filter, requirements = st.tabs(["👩‍🏫 Filter Instruction", "🛑 Requirements"])
    # Configure text generation for Cohere
    with filter:
        with st.popover("Instruction:"):
            st.markdown(""" 
                        Set the temperature (creativity level):
                        - Lower values (e.g., 0.1–0.3): The model produces simple and predictable results.
                        - Higher values (e.g., 0.7–1.0): The model becomes more creative and complex, but the results might be less focused.
                        - Recommended range: Choose a temperature between 0.5 and 0.7 for a good balance between accuracy and creativity.
                                """)
            if provider == "Cohere":
                st.markdown(""" 
                                Choose the model you would like to use for your dataset:
                                - "command-xlarge-nightly": The largest model with the most details, able to learn complex patterns and relationships in data.
                                - "command-large: Smaller than xlarge but still powerful, offering a good mix of performance and efficiency.
                                - "command-base-nightly" : The smallest and lightest model, designed for quick use and easy deployment.
                            """)
            if provider == "Gemini":
                st.markdown(""" 
                                Choose the model you would like to use for your dataset:
                                - "Gemini 2.0 Flash-exp:" The largest and most powerful model in the Gemini family, designed for complex tasks that require a high level of creativity and understanding.
                                - "Gemini 1.5 Flash:" This model offers a good balance between size and performance. It can handle a wide range of tasks and is suitable for many applications.
                                - "Gemini 1.5 Flash-8B:" The smallest model in the Gemini family, designed for simpler tasks and devices with limited resources.
                                - "Gemini 1.5 Pro:" This model is optimized for specific tasks, such as code generation or technical translation.
                            """)
    with requirements:
            st.markdown(""" 
                    **NTViz works best with the datasets:**
                    - Columns: ≤ 10  
                    - Rows: ≤ 1000  
                    - File Size: ≤ 500KB  

                    **Correct CSV Format:**  
                    Your file should contain only the variable names as column headers and the corresponding values.  
                    Avoid including unrelated information such as titles, notes, or daily reports in the file.  
                    """)
                    
            with st.popover("📋 Example:"):
                    st.markdown(""" 
                        **✅ Correct Input Example:**
                        ```csv
                        Name, Age, Country, Salary
                        John, 25, USA, 50000
                        Anna, 30, Canada, 60000
                        Mark, 28, UK, 45000
                        ```

                        **❌ Incorrect Input Example:**
                        ```csv
                        ,Daily Report,,
                        Date,12/16/2024 20:38,,
                        Tên,Phiến,,
                        ,,,
                        ID,Name,Category,Date
                        1,A,BCV,12/16/2024 20:38
                        2,B,B1,12/16/2024 20:38
                        3,A,B2,12/16/2024 20:38
                        ```
                        - Extra rows like "Daily Report" or empty cells will cause errors.  
                        - Remove unnecessary information before uploading.  
                        """)
                    
    # Choose the model and the temperature
    # Model and temperature selection
    temperature = st.slider("Temperature", 
                            min_value=0.0, 
                            max_value=1.0, 
                            value=0.5, 
                            step=0.1)
    model = st.selectbox("Select Model:", models)
    textgen_config = TextGenerationConfig(
                    n=1, 
                    temperature=temperature, 
                    model=model,
                    use_cache=True
                )
    return textgen_config
            
        
def initialize_lida_and_api(api_key, provider):
    """
    Initialize LIDA with default configuration.
    
    Args:
        api_key (object): The user's API key for the Cohere platform.
    """
    try:
        # Cohere provider
        # Initialize Cohere with the API key and set up with LIDA
        if provider == "Cohere":
            text_gen = llm("cohere", api_key=api_key)
            lida = Manager(text_gen=text_gen)
            
            models =  ["command-xlarge-nightly", 
                        "command-large", 
                        "command-base-nightly"]
            config = setup_model_textgen(models, provider=provider)   
            textgen_config = config
            
        
            st.sidebar.success("Successfully connected to Cohere!")
     
        
        if provider == "Gemini":
            text_gen = llm("gemini", api_key = api_key)
            lida = Manager(text_gen=text_gen)
            models =["gemini-2.0-flash-exp", 
                    "gemini-1.5-flash", 
                    "gemini-1.5-flash-8b"]
                
            config = setup_model_textgen(models, provider=provider)   
            textgen_config = config
            
            st.sidebar.success("Successfully connected to Gemini!")
            
        return lida, textgen_config
    
    except Exception as e:
        st.sidebar.error(f"Unable to connect to {provider}: {e}")
        return None, None

def process_data_summary(df, lida, textgen_config):
    """
    Perform data summarization and goal setting.
    
    Args:
        df (DataFrame): Input dataset.
        lida: LIDA library to handle tasks.
        textgen_config: TextGeneration configuration for LIDA.
    
    Returns:
        Summary and goals based on user requirements.
    """
    st.dataframe(df.head())
    
    # Check and clean data
    null_values = df.isnull().sum()
    dup_values = df.duplicated().sum()
    
    if null_values.any() > 0 or dup_values > 0:  
        df = clean_df(df)
        st.success("Data cleaned!")
    else:
        st.success("No missing or duplicate values found in the data.")
    with st.spinner('Wait for it...'):
        time.sleep(5)
        summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
        goals = lida.goals(summary, n=5, textgen_config=textgen_config)

    return summary, goals

def generate_visualizations(lida, summary, goals, textgen_config):
    """
    Create and display visualizations based on goals.
    
    Args:
        lida: LIDA library to handle tasks.
        summary: Data summary.
        goals: Goals for visualization.
        textgen_config: TextGeneration configuration for LIDA.
    
    Returns:
        Visualizations based on user requirements.
    """
    
    if st.button("Generated Charts"):
        library = "seaborn"
        n = 5
        
        for i in range(n):
            try:
                st.subheader(f"✷ :grey[Insight {i}:]")
                st.write(goals[i])
                charts = lida.visualize(summary=summary, goal=goals[i], library=library)
                
                for chart in charts:
                    display_charts(
                        lida, 
                        chart, 
                        goals[i], 
                        library, 
                        textgen_config
                    )
                st.divider()
                st.write("\n")
            except Exception as e:
                st.error(f"Error generating chart for Goal {i+1}: {e}")

def process_user_query_graphs(df, lida, textgen_config, provider):
    """
    Generate visualizations based on user queries.
    
    Args:
        df (DataFrame): Input dataset.
        lida: LIDA library to handle tasks.
        textgen_config: TextGeneration configuration for LIDA.
    
    Returns:
        Visualizations based on user queries.
    """
    user_query = st.text_area(label="Type Your Question Here:")
    
    if provider == "Cohere":
        k = st.number_input(label="Top Charts:", min_value=1, max_value=5, step=1)
    else:
        k = 1
        st.info("Gemini can only generate one chart at a time because the chat functionality does not support a candidate_count greater than 1.")
        
    if st.button("Generate Charts"):
        try:
            textgen_config.n = k
            summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
            query_charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)
            
            st.write(f"Top {len(query_charts)} charts ")
            for chart in query_charts:
                display_charts(
                    lida, 
                    chart, 
                    user_query, 
                    "seaborn", 
                    textgen_config
                )
            if len(query_charts) < k:
                st.error(f"Sorry, we could only suggest {len(query_charts)} charts at the moment.")
                st.warning("We suggest you to change your temperature and try again. Thank you.")

                    
        except Exception as e:
            st.error(f"Error initializing LIDA or Cohere: {e}")

def process_viz_recommend(df, lida, textgen_config, provider):
    """
    Recommend charts based on data summary.
    
    Args:
        df (DataFrame): Input dataset.
        lida: LIDA library to handle tasks.
        textgen_config: TextGeneration configuration for LIDA.
    
    Returns:
        Recommended visualizations based on user requests.
    """
    if provider == "Cohere":
        k = st.number_input(label="Top Charts:", min_value=1, max_value=5, step=1)
    else:
        k = 1
        st.info("Gemini can only generate one chart at a time because the chat functionality does not support a candidate_count greater than 1.")
    
    if st.button(label="Generate Charts"):
        try:
            
            with st.spinner('Wait for it...'):
                time.sleep(5)
                summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
                goals = lida.goals(summary, n=1, textgen_config=textgen_config)
                
                charts = lida.visualize(summary=summary, goal=goals[0], library="seaborn")
                
                if charts:
                    textgen_config.n = k
                    recommended_charts = lida.recommend(
                        code=charts[0].code, 
                        summary=summary, 
                        n=k,  
                        textgen_config=textgen_config
                    )
                    
                    st.write(f"Suggested number of charts: {len(recommended_charts)}")
                    for chart in recommended_charts:
                        display_charts(
                            lida, 
                            chart, 
                            goals[0], 
                            "seaborn", 
                            textgen_config
                        )
                    if len(recommended_charts) < k:
                        st.error(f"Sorry, we could only suggest {len(recommended_charts)} charts at the moment.")
                        st.warning("We suggest you to change your temperature and try again. Thank you.")
                else:
                    st.error("No charts were generated.")
                    st.warning("We suggest you to change your temperature and try again. Thank you.")
        
        except Exception as e:
            st.error(f"Error during chart recommendation: {e}")



# Additional helper function to get the current provider's API key
def get_current_api_key():
    """Get the API key for the currently selected provider."""
    provider = st.session_state.get("provider", "Cohere")
    if provider == "Cohere":
        return st.session_state.cohere_api_key
    else:
        return st.session_state.gemini_api_key
    

def show_task():
    """
    Main function to coordinate tasks in the app.
    """
    # Load API key
    api_key, provider = load_api_key()
            
    # Initialize LIDA and Cohere
    lida, textgen_config = initialize_lida_and_api(api_key, provider) if api_key else (None, None)

    with st.sidebar.container():
        st.header("Tasks:")
        task = st.selectbox("Functions:", ["Summarize & Goal", 
                                           "UserQuery based graphs",
                                           "VizRecommend"
                                           ])

    # Task-specific content
    df = upload_file()
    
    if df is not None:  
        if task == "Summarize & Goal" and lida:
            summary, goals = process_data_summary(df, lida, textgen_config)
            generate_visualizations(lida, summary, goals, textgen_config)
        
        elif task == "UserQuery based graphs" and lida:
            df = clean_df(df)
            process_user_query_graphs(df, lida, textgen_config, provider)
        
        elif task == "VizRecommend" and lida:
            process_viz_recommend(df, lida, textgen_config, provider)
        else:
            st.error("Please select a valid task or ensure LIDA is initialized correctly.")

show_task()
