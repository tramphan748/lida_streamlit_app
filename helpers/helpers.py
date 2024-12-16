import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
# from dataprep.clean import clean_headers, clean_missing, clean_date, clean_columns

# Import thư viện LIDA
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
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    
    # Input API key
    st.sidebar.subheader("Nhập mã API key:")
    api_key = st.sidebar.text_input(
        "API key:", value=st.session_state.api_key, type="password", placeholder="Nhập mã API của bạn"
    )
    st.session_state.api_key = api_key

    # Validate API key
    if not api_key:
        st.warning("Vui lòng nhập API key để tiếp tục.")
    else:
        pass
        # st.success("API key đã được nhập.")

    return api_key


def upload_file():
    """
    Hàm này dùng để:
    - Tải tệp dữ liệu với 2 định dạng csv và json
    - Đọc dữ liệu đầu vào cho các tác vụ tiếp theo
    """
    # Tải tệp lên để thực hiện các tác vụ
    uploaded_file = st.file_uploader("Tải tệp dữ liệu với định dạng .csv/.json:", type=["csv", "json"])
    if uploaded_file is not None:
        # Xử lý tệp đã tải lên
        if uploaded_file.name.endswith(".csv"):
            # Đọc file CSV
            df = pd.read_csv(uploaded_file)
            st.success(f"Đã tải tệp CSV có {len(df)} dòng dữ liệu.")
        elif uploaded_file.name.endswith(".json"):
            # Đọc file văn bản
            df = pd.read_json(uploaded_file)
            st.success(f"Đã tải tệp JSON.")
        else:
            st.error("Định dạng này không được hỗ trợ.")
        
        return df
    else:
        st.error("Không tồn tại tệp dữ liệu nào. Vui lòng thử lại.")
        return None


def clean_df(df):
    """
    Mục tiêu: Tự động hóa quá trình làm sạch data cho dữ liệu như thay thế giá trị rỗng, xóa dữ liệu trùng lặp
    
    Args:
        df (_type_): bộ dữ liệu người dùng đưa vào

    Returns:
        cleaned_df: bộ dữ liệu đã được xử lý
    """
    df = df.copy()
    
    # Điền giá trị thiếu cho các cột số bằng giá trị trung bình
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())
        
    # Xóa bỏ các giá trị trùng lặp
    df = df.drop_duplicates()
    
    return df

# Convert base64 string to image
def base64_to_image(base64_str):
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data))
    return img

# Hàm output, hiển thị code, explain, evalute biểu đồ
def display_charts(
    lida, 
    chart, 
    goal, 
    library='seaborn', 
    textgen_config=None
):
    """
    Hiển thị, giải thích và đánh giá chi tiết cho một biểu đồ.

    Args:
        lida (Manager): LIDA manager
        chart (object): Biểu đồ cần phân tích
        goal (str): Mục tiêu của biểu đồ
        library (str, optional): Thư viện vẽ biểu đồ. Mặc định là 'matplotlib'.
        textgen_config (TextGenerationConfig, optional): Cấu hình sinh văn bản. 
                                                         Mặc định là None.
    """
    # Kiểm tra nếu chart không tồn tại
    if not chart:
        st.warning("Không có biểu đồ để hiển thị.")
        return

    # Chuyển đổi biểu đồ sang ảnh
    try:
        img = base64_to_image(chart.raster)
    except Exception as e:
        st.error(f"Lỗi chuyển đổi biểu đồ: {e}")
        return

    # Hiển thị ảnh biểu đồ
    st.image(img)

    # Nút tải xuống
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{img_str}" download="chart.png">˚⋆ ʕっ• ᴥ • ʔっ Download Chart ˚⋆</a>'
    st.markdown(href, unsafe_allow_html=True)

    # Hiển thị code
    with st.expander("Code"):
        st.code(chart.code, language="python")

    # Giải thích biểu đồ
    with st.expander("Explain"):
        try:
            explanations = lida.explain(
                code=chart.code, 
                library=library, 
                textgen_config=textgen_config
            )
            for row in explanations[0]:
                st.write(row["section"], " ** ", row["explanation"])
        except Exception as e:
            st.error(f"Không thể giải thích biểu đồ: {e}")

    # Đánh giá biểu đồ
    with st.expander("Evaluate"):
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
            st.error(f"Không thể đánh giá biểu đồ: {e}")
