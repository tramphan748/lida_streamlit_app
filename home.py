import streamlit as st
import base64
from streamlit_option_menu import option_menu

# import cover page
file_ = open("material/outlook/Global.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:material/outlook/Global.gif;base64,{data_url}" alt="cover">',
    unsafe_allow_html=True,
)

# Homepage
def show_home():
    home, lida, innova, contr, source, contact = st.tabs(["Home", "LIDA", "Innovation", "Contribute", "Source", "Support"])
    
    # Display content based on the selected tab
    with home:
        st.subheader(" :violet[NTViz] _:gray[A Data Recommendation System For Everyone]_ 🦾")
        st.markdown("##### _Why did we build this project?_")
        st.markdown(""" 
                    _:blue[**"Data is the most valuable currency"**]_, is an undeniable truth as it plays a key role in various industries and fields, such as:
                    - **Decision-making support:** Providing information and analysis to help organizations and individuals make reliable decisions, from business strategies to product and service details.
                    - **Improving operational efficiency:** Helping optimize processes by providing insights into performance, procedures, and customer data, enabling organizations to adjust and enhance efficiency.
                    - **Developing products and services:** Offering insights into market demand and feedback, aiding businesses in understanding customer expectations and developing suitable products and services.
                    - **Research and technological development:** Serving as a vital resource for scientific research and technological advancements, enabling researchers to analyze and create new discoveries.
                    - **Enhancing customer experience:** Personalizing customer experiences, from product design to customer service, based on individual information.
                    - **Risk and fraud minimization:** Detecting and preventing fraudulent activities and risks in business and finance through analyzing abnormal patterns and trends.\n
                    ...and many more benefits that data can bring us.\n
                    With increasingly diverse and complex data, it is impossible to fully understand it just by reading the raw data collected from reality.
                    How can we quickly and easily grasp the information? \n
                    :point_right: The answer lies in :violet[**Data Visualization**], a powerful tool that helps transform data into comprehensible visuals, enabling us to make accurate and effective decisions faster than ever.
                    """)
        st.image("material/outlook/mhoa.jpg", caption="Figure 1. Illustration", use_container_width=True)    

        # Why data visualization is important
        st.markdown(""" 
                ### 📍 :grey[The Importance of :violet[Data Visualization]]:
                **1. Conveying information effectively:**
                - Visualization represents complex data in easy-to-understand images, allowing viewers to quickly grasp information without analyzing detailed data tables.

                **2. Supporting decision-making:**
                - Charts and visuals help decision-makers recognize trends, identify issues, and provide suitable solutions based on specific data.

                **3. Discovering trends and relationships:**
                - Visualization highlights trends, patterns, and hidden relationships between variables in data that may be overlooked when only examining raw data.

                **4. Communicating and persuading:**
                - Charts and visuals assist in persuading others, particularly in presentations, reports, or data-driven arguments.

                **5. Enhancing data analysis capabilities:**
                - Helps analysts delve deeper into data, detect anomalies (outliers), or explore aspects previously unconsidered, leading to more comprehensive analyses.

                **6. Increasing data interaction:**
                - Enables interaction with data through visuals and vital numerical information such as sales, distributions, etc.

                **7. Creating excitement about data:**
                - Vibrant and intuitive visuals not only make data less dry but also help non-specialists delve deeper into data and related issues simply and understandably.
                """)
        st.image("material/outlook/ex_tquan.jpg", caption="Figure 2. Visualization Example")
        
        st.divider()
        st.markdown("### 🔴 :grey[The Main Problem:]")
        st.markdown(""" 
                    However, if someone without programming skills wants to explore and extract insights from their dataset, they might face challenges such as:
                    - Which variables should be visualized? What does that chart signify?
                    - Which chart should be chosen for the dataset?
                    - How to create that chart without programming skills? \n
                    Recognizing these difficulties, we aim to build and explore tools that can support :blue["non-data professionals"] in the simplest and most cost-effective way possible.
                    ##### :point_right: By developing a :violet[Chart Recommendation System] based on user-provided datasets.
                    """)
    
    with lida:
        st.header(" ♛:grey[LIDA: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models]")
        st.markdown("### *Overview of LIDA:*")
        st.markdown(""" 
                    - LIDA is a chart-generation platform powered by LLM, owned by Microsoft, consisting of four main modules: Summarize, Goal Explorer, VisGenerator, and Infographic.
                    - The system uses LLM to summarize data, generate objectives, produce code, and create visualizations automatically.
                    """)
        st.markdown(""" 
                    ##### Advantages:
                    - Automatically generates hypotheses/objectives from data, supports multiple visualization grammars, and can create infographics.
                    - More efficient than existing systems, simplifying the creation of complex charts.
                    - Introduces metrics to evaluate reliability (VER) and visualization quality (SEVQ).
                    """)
        st.markdown(""" 
                    ##### Disadvantages:
                    - Requires further research on task complexity and programming language choices for better performance.
                    - Demands substantial computational resources, with room for improvement in implementation and latency.
                    - Needs more comprehensive evaluation standards and research on explaining system behaviors.
                    """)
        
        st.markdown("### ✪ *Details of LIDA's activities:*")
        st.markdown(""" 
        1. **Summarize and Goals:** \n
            *a. Summarize based on rules and LLM:*
            - Utilizes LLM to generate concise summaries of datasets through a two-stage process, providing guidance or suggestions on what can be achieved with the dataset. \n
            *b. Goal Explorer:*
            - This step creates a JSON file comprising three objects: “question,” “visualization,” “rationale.”
            - **Question:**
                - LLM acts as a user or guide, exploring the dataset to propose hypotheses in the form of questions.
            - **Visualization:**
                - Specifies chart names and types.
            - **Rationale:**
                - Explains the significance of the chart and provides insights.
        """)
        st.image("material/lida/goals.png", caption="Figure 2. Structure of Goals", use_container_width=True)
        
        st.markdown(""" 
        2. **VisGenerator:**
        Generates specific charts through three submodules: \n 
            *a. Code scaffold constructor:* \n
            Creates scaffold libraries corresponding to supported programming languages (e.g., `Matplotlib`, `GGPlot`, `Plotly`, `Altair`, `Seaborn`, and `Bokeh`).
            
            *b. Code generator:* \n
            Inputs the scaffold, summarized dataset, visualization goals, and prepared prompts into the LLM.
            
            *c. Code executor:* \n
            Executes and generates specific charts.
        """)
        st.image("material/lida/example.png", caption="Figure 3. Corresponding Chart", use_container_width=True)   
        st.markdown(""" 
        3. **Infographic:**
            - This module generates charts based on the output of VisGenerator.
            - Utilizes text-conditioned image-to-image models (e.g., diffusion models) implemented through the Peacasso library (Dibia, 2022).
            """)
        
        st.image("material/lida/infograp.png", caption="Figure 4: LIDA's Infographic Example", use_container_width=True)
        
        st.divider()
        
        # Information on LIDA-supported platforms
        
        with st.expander(label="_:grey[📌 Important Notes:]_"):
            st.markdown(""" 
                    ##### 1. Python:
                    LIDA requires Python version 3.10 or higher.
                    ##### 2. Data: 
                    Best suited for datasets with ≤ 10 columns. For larger datasets, preprocessing is necessary (select relevant columns).
                    ##### 3. Functionality: 
                    LIDA works with .csv or .json format datasets.
                    ##### 4. Efficiency: 
                    LIDA performs best with large LLMs (GPT-3.5, GPT-4). Smaller models may not follow instructions as effectively.
                    ##### 5. Accuracy: 
                    Error rate < 3.5% across 2200 generated charts, significantly lower than the baseline (>10%).
                    ##### 6. Large Language Model: 
                    LIDA leverages large language models as managers to assist users in executing its tasks.
                """)
            
            
            
    with innova:
        # Proposed New Improvements
        st.subheader("_:grey[New Improvements in LIDA:]_")
        st.markdown(""" 
                    After thoroughly exploring the tasks in LIDA, we noticed:
                    - In LIDA, when inputting a dataset, it lacks a built-in "Data Cleaning" feature for users.
                    - The "summarize" feature is not clear and direct enough.
                    - Google stops providing API key :blue["palm"] by October 2024. Therefore, users can't use the provider "Palm" anymore.
                    """)
        st.markdown(""" 
                    - The chart generation feature based on user queries has significant potential. It can effectively create 3 to 5 charts solely based on the queries provided by users.
                    """)
        st.markdown("""
                    Therefore, we propose the following additions:
                    - Integrate the `ydata_profiling` library to provide clearer and more direct insights about the dataset.
                    - Before LIDA performs **"summarize"** and **"goals explorer"**, we will integrate a function to check if the data is clean. If not, we will clean the data for the user.
                    - We leveraged the [:red[llmx]](https://github.com/tramphan748/llmx-gemini) GitHub code to integrate the :blue[Gemini] API key into our NTViz platform, enabling users to choose between the :violet[Cohere] and :blue[Gemini] providers.
                                       """)
        st.image("material/lida/overview.png", 
                caption="Figure 2. Overview Illustration",
                use_container_width=True)

        
        
        
    with contr:
        st.header("💡:grey[Why contribute to NTviz?]")
        st.markdown(""" 
                    #### Your contributions help:
                    - Make NTviz a practical and user-friendly system for everyone.
                    - Enhance the system's features, ensuring it meets user needs in real-world scenarios.
                    - Bridge the gap between data and non-technical users, empowering them to make better decisions using their own datasets.
                    - Foster a community where data is accessible and understandable for all.\n
                    :point_right: If you have expertise in **programming, data analysis, UI/UX design**, or even if you’re an **enthusiastic user**, we welcome your contributions to NTviz.
                    """)
        st.markdown("#### 🤝 Ways to Contribute:")
        st.markdown(""" 
                    - **Suggest new features:** Share ideas that can make NTviz more intuitive and effective.
                    - **Report bugs:** Let us know about any issues you encounter.
                    - **Help with documentation:** Improve user guides or provide detailed examples.
                    - **Join as a collaborator:** Actively develop and enhance the project.
                    - **Spread the word:** Share NTviz with friends and colleagues who might benefit from it.
                    """)
        st.markdown("#### :link: **Contact us to contribute:**")
        st.markdown("Email: [ntviz.support@example.com](mailto:ntviz.support@example.com)")

    with source:
        st.header("📂:grey[Source Code & Resources]")
        st.markdown(""" 
                    NTviz is open-source! Feel free to explore, modify, and contribute to our project.
                    #### Where to find our code:
                    - GitHub: [NTviz Repository](https://github.com/ntviz-project)  
                    
                    #### Open Source License:
                    - NTviz is licensed under the MIT License. This means you're free to use, modify, and distribute the software, as long as proper attribution is given.
                    """)

    with contact:
        st.header("📞:grey[Contact Support]")
        st.markdown(""" 
                    Have questions, suggestions, or need help?  
                    Our team is here to assist you! Reach out to us via the following channels:  
                    
                    - **Email:** ntviz.support@example.com  
                    
                    #### Business Inquiries:  
                    For partnerships or collaborations, please email: business.ntviz@example.com
                    """)
        st.markdown(""" 
                    ### FAQs:
                    **Q: Who is NTviz for?**  
                    A: NTviz is designed for non-technical users who need a simple, intuitive tool to visualize and understand their data.

                    **Q: Can I use NTviz for free?**  
                    A: Yes, NTviz is completely free. We believe in democratizing access to data visualization for everyone.

                    **Q: What file formats does NTviz support?**  
                    A: NTviz currently supports `.csv` file formats.
                    """)
        st.markdown("""
                    ### Acknowledgments:  
                    Our project is inspired by groundbreaking work from leading tools and research:

                    - **LIDA**: *A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models* (Dibia, ACL 2023).  
                    - **Cohere**: Providing cutting-edge NLP APIs for data-driven applications.
                    - **Gemini**: Providing cutting-edge NLP APIs for our NTViz.
                    We greatly appreciate the contributions and advancements made by these tools, enabling us to develop NTviz for a broader audience.

                    """)
        
show_home()
