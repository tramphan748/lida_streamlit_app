import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import cohere
import sys
import os

# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import các hàm hỗ trợ từ thư mục helpers
from helpers.helpers import upload_file
from helpers.helpers import clean_df

"""
Hiển thị tổng quan về bộ dữ liệu
"""
df = upload_file()
st.title(":grey[Tổng quan về bộ dữ liệu:]")
if df is not None:
    report = ProfileReport(df)
    st_profile_report(report)
else:
    st.warning("Vui lòng tải lên tệp dữ liệu để xem tổng quan.")
