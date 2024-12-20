import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import time

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

def initialize_lida_and_cohere(api_key):
    """
    Initialize LIDA and Cohere with default configuration.
    
    Args:
        api_key (object): The user's API key for the Cohere platform.
    """
    try:
        # Initialize Cohere with the API key and set up with LIDA
        text_gen = llm("cohere", api_key=api_key)
        lida = Manager(text_gen=text_gen)
        
        filter, requirements = st.tabs(["👩‍🏫 Filter Instruction", "🛑 Requirements"])
        # Configure text generation for Cohere
        with filter:
            with st.popover("Instruction:"):
                st.markdown(""" 
                            Choose the model you would like to use for your dataset:
                            - "command-xlarge-nightly": The largest model with the most details, able to learn complex patterns and relationships in data.
                            - "command-large: Smaller than xlarge but still powerful, offering a good mix of performance and efficiency.
                            - "command-base-nightly" : The smallest and lightest model, designed for quick use and easy deployment.
                            \n
                            Set the temperature (creativity level):
                            - Lower values (e.g., 0.1–0.3): The model produces simple and predictable results.
                            - Higher values (e.g., 0.7–1.0): The model becomes more creative and complex, but the results might be less focused.
                            - Recommended range: Choose a temperature between 0.5 and 0.7 for a good balance between accuracy and creativity.
                            """)
            # Upload a file to perform tasks
            with requirements:
                st.markdown(""" 
                **The requirements of your dataset:**
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
            temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
            model = st.selectbox("Model", ["command-xlarge-nightly", "command-large", "command-base-nightly"])
            textgen_config = TextGenerationConfig(
                n=1, 
                temperature=temperature, 
                model=model,
                use_cache=True
            )
        
        st.sidebar.success("Successfully connected to Cohere!")
        return lida, textgen_config
    
    except Exception as e:
        st.sidebar.error(f"Unable to connect to Cohere: {e}")
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

def process_user_query_graphs(df, lida, textgen_config):
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
    k = st.number_input(label="Top Charts:", min_value=1, max_value=5, step=1)
    
    if st.button("Generate Charts"):
        try:
            textgen_config.n = k
            summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
            query_charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)
            
            st.write(f"Suggested number of charts: {len(query_charts)}")
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
                    
        except Exception as e:
            st.error(f"Error initializing LIDA or Cohere: {e}")

def process_viz_recommend(df, lida, textgen_config):
    """
    Recommend charts based on data summary.
    
    Args:
        df (DataFrame): Input dataset.
        lida: LIDA library to handle tasks.
        textgen_config: TextGeneration configuration for LIDA.
    
    Returns:
        Recommended visualizations based on user requests.
    """
    k = st.number_input(label="Number of charts to generate:", min_value=1, max_value=5, step=1)
    
    if st.button(label="Generate Charts"):
        try:
            textgen_config_recommend = TextGenerationConfig(
                n=1, 
                temperature=0.3,
                use_cache=True
            )
            
            with st.spinner('Wait for it...'):
                time.sleep(5)
                summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
                goals = lida.goals(summary, n=1, textgen_config=textgen_config)
                
                charts = lida.visualize(summary=summary, goal=goals[0], library="seaborn")
                
                if charts:
                    textgen_config_recommend.n = k
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
                else:
                    st.error("No charts were generated.")
        
        except Exception as e:
            st.error(f"Error during chart recommendation: {e}")

def show_task():
    """
    Main function to coordinate tasks in the app.
    """
    # Load API key
    api_key = load_api_key()
    
    # Initialize LIDA and Cohere
    lida, textgen_config = initialize_lida_and_cohere(api_key) if api_key else (None, None)

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
            process_user_query_graphs(df, lida, textgen_config)
        
        elif task == "VizRecommend" and lida:
            process_viz_recommend(df, lida, textgen_config)

show_task()
