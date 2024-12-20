import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import matplotlib.pyplot as plt
from helpers.helpers import upload_file, base64_to_image  # Assuming these are defined in helpers/helpers.py
from io import BytesIO
import base64

# Function to convert plot to image
def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

# Display an overview of the dataset
df = upload_file()
st.title(":grey[Dataset Overview:]")
if df is not None:
    # Generate and display the profiling report
    report = ProfileReport(df, 
                           missing_diagrams=None,
                           explorative=True,
                           samples=None)
    st_profile_report(report)
    
    st.subheader("Distribution values of numeric variables:")

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns  # Select numeric columns

    if not numeric_cols.empty:
        # Use a selectbox to choose a numeric column for the boxplot
        with st.popover("Select columns"):
            selected_col = st.selectbox("",options=numeric_cols)
    
        if selected_col:
            # Create a boxplot for the selected column
            fig, ax = plt.subplots(figsize=(8, 6))  # Set a smaller size
            sns.boxplot(data=df, x=selected_col, ax=ax)
            ax.set_title(f"Box Plot: {selected_col}", fontsize=14)
            
            # Convert the plot to base64
            img_base64 = fig_to_base64(fig)

            # Display the image with a specified size and center it using HTML
            st.markdown(f'''
                <div style="display: flex; justify-content: center;">
                    <img src="data:image/png;base64,{img_base64}" width="500" height="350" />
                </div>
            ''', unsafe_allow_html=True)
        else:
            st.warning("No column selected.")
    else:
        st.warning("No numeric columns found in the dataset.")
else:
    st.warning("Please upload a data file to view the overview.")
