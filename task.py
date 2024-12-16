import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
from dotenv import load_dotenv

# Import thư viện LIDA
from lida import Manager, TextGenerationConfig, llm

# import hàm hỗ trợ từ thư mục helpers
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
    Khởi tạo LIDA và Cohere với cấu hình mặc định
    """
    try:
        # Khởi tạo Cohere với API Key và thiết lập với LIDA
        text_gen = llm("cohere", api_key=api_key)
        lida = Manager(text_gen=text_gen)
        
        # Cấu hình text generation cho Cohere
        with st.expander("Filter"):
            temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
            model = st.selectbox("Model", ["command-xlarge-nightly", "command-large", "command-base-nightly"])
            textgen_config = TextGenerationConfig(
                n=1, 
                temperature=temperature, 
                model=model,
                use_cache=True
            )
        
        st.sidebar.success("Kết nối với Cohere thành công!")
        return lida, textgen_config
    
    except Exception as e:
        st.sidebar.error(f"Không thể kết nối với Cohere: {e}")
        return None, None



def process_data_summary(df, lida, textgen_config):
    """
    Thực hiện tóm tắt và đặt mục tiêu cho dữ liệu
    """
    st.dataframe(df.head())
    
    # Kiểm tra và làm sạch dữ liệu
    null_values = df.isnull().sum()
    dup_values = df.duplicated().sum()
    
    if null_values.any() > 0 or dup_values > 0:  
        df = clean_df(df)
        st.success("Đã làm sạch dữ liệu!")
    else:
        st.success("Dữ liệu không có giá trị rỗng/trùng lặp.")
    
    summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
    goals = lida.goals(summary, n=5, textgen_config=textgen_config)
    
    st.subheader("Bảng tóm lược:")
    st.write(summary)
    
    st.subheader("Goals:")
    for goal in goals:
        st.write(goal)
    
    return summary, goals

def generate_visualizations(lida, summary, goals, textgen_config):
    """
    Tạo và hiển thị các biểu đồ theo mục tiêu
    """
    library = "seaborn"
    n = 5
    
    for i in range(n):
        try:
            charts = lida.visualize(summary=summary, goal=goals[i], library=library)
            
            for chart in charts:
                st.subheader(f"Goal {i+1}")
                display_charts(
                    lida, 
                    chart, 
                    goals[i], 
                    library, 
                    textgen_config
                )
        
        except Exception as e:
            st.error(f"Lỗi khi tạo biểu đồ cho Goal {i+1}: {e}")

def process_user_query_graphs(df, lida, textgen_config):
    """
    Tạo biểu đồ dựa trên truy vấn người dùng
    """
    user_query = st.text_area(label="User Query:")
    k = st.number_input(label="Số biểu đồ bạn muốn tạo:", min_value=1, max_value=5, step=1)
    
    if st.button("Tạo biểu đồ"):
        try:
            textgen_config.n = k
            summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
            query_charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)
            
            st.write(f"Số biểu đồ gợi ý: {len(query_charts)}")
            for chart in query_charts:
                display_charts(
                    lida, 
                    chart, 
                    user_query, 
                    "seaborn", 
                    textgen_config
                )
                    
        except Exception as e:
            st.error(f"Đã xảy ra lỗi khi khởi tạo LIDA hoặc Cohere: {e}")

def process_viz_recommend(df, lida, textgen_config):
    """
    Đề xuất biểu đồ dựa trên tóm tắt dữ liệu
    """
    k = st.number_input(label="Số biểu đồ bạn muốn tạo:", min_value=1, max_value=5, step=1)
    
    if st.button(label="Tạo biểu đồ"):
        try:
            textgen_config_recommend = TextGenerationConfig(
                n=1, 
                temperature=0.3,
                use_cache=True
            )
            
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
                
                st.write(f"Gợi ý: {len(recommended_charts)} charts")
                for chart in recommended_charts:
                    display_charts(
                        lida, 
                        chart, 
                        goals[0], 
                        "seaborn", 
                        textgen_config
                    )
            else:
                st.error("Không có biểu đồ nào được tạo.")
        
        except Exception as e:
            st.error(f"Lỗi trong quá trình đề xuất biểu đồ: {e}")

def show_task():
    """
    Chính của ứng dụng, điều phối các task
    """
    # Load API key
    api_key = load_api_key()
    
    # Khởi tạo LIDA và Cohere
    lida, textgen_config = initialize_lida_and_cohere(api_key) if api_key else (None, None)

    with st.sidebar.container():
        st.header("Tasks:")
        task = st.selectbox("Các chức năng:",["Summarize & Goal", 
                                            "UserQuery based graphs",
                                            "VizRecommend"
                                            ])

    # Nội dung tương ứng với từng lựa chọn
    df = upload_file()
    
    if df is not None:  
        if task == "Summarize & Goal" and lida:
            summary, goals = process_data_summary(df, lida, textgen_config)
            generate_visualizations(lida, summary, goals, textgen_config)
        
        elif task == "UserQuery based graphs" and lida:
            process_user_query_graphs(df, lida, textgen_config)
        
        elif task == "VizRecommend" and lida:
            process_viz_recommend(df, lida, textgen_config)



show_task()