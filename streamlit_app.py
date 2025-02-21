
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from PIL import Image
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
from st_pages import add_page_title, get_nav_from_toml

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

def main():
    # Load environment variables
    load_dotenv()
    # DESIGN implement changes to the standard streamlit UI/UX
    st.set_page_config(page_title="NTViz", page_icon="material/outlook/logo.jpg", layout="wide", initial_sidebar_state="expanded")
    sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

    nav = get_nav_from_toml(
        ".streamlit/pages_sections.toml" if sections else ".streamlit/pages.toml"
    )
    # Decor
    st.logo(image="material/outlook/logo.jpg", size="large",icon_image=None)
    pg = st.navigation(nav)

    add_page_title(pg)

    pg.run()
    
if __name__ == "__main__":
    main()