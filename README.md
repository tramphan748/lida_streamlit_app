### 📊 Introduction
[NTViz](https://ntviz-site.streamlit.app/) is a Streamlit application that performs various data analysis, visualization tasks and interacts with Large Language Models (LLMs) through the [LIDA](https://github.com/microsoft/lida) framework.

### 🛠️ Prerequisites & Installation

#### Option 1: Use the Web Application
Access [NTViz](https://ntviz-site.streamlit.app/) directly in your browser.

#### Option 2: Run Locally
```bash
# Clone the repository
git clone https://github.com/tramphan748/lida_streamlit_app.git
cd lida_streamlit_app

# Install the required packages
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py
```

**Note:** The `requirements.txt` file includes [llmx-gemini](https://github.com/tramphan748/llmx-gemini), a customized version of the llmx library that supports the Gemini API. If you manually installed llmx in editable mode, ensure that the same code or git+... line is present in requirements.txt.

### 📑 Features

#### 1. Dashboard
Introduction to the project, overview of capabilities, and user interface.

#### 2. API Key Instructions
Step-by-step guide to obtain API keys from two main providers:
- Cohere
- Gemini (using our customized [llmx-gemini](https://github.com/tramphan748/llmx-gemini) library)

#### 3. Data Reports
Generate comprehensive data overviews:
- Automatic statistics generation
- Charts and visualizations
- Missing value detection
- Correlation analysis
- Basic exploratory data analysis (EDA)

![Data Report Example](/material/readme/data_overview.png)

#### 4. LIDA Tasks

##### 4.1. Summarize & Goal
Leverage LLMs to automatically generate:
- Data summaries
- Top 5 analytical goals

![Goal Example](/material/readme/insight0.png)
![Corresponding Chart](/material/readme/chart_insight0.png)
![VizOps Interface](/material/readme/Vizops.png)

##### 4.2. User Query Based Graphs
Create visualizations based on natural language user queries.

![User Query Example](/material/readme/userQuery_based_graphs.png)

##### 4.3. Recommendations
Based on summaries, goals, code, and generated visualizations, the system automatically suggests 1-5 additional charts.

![VizRecommend Task Example](/material/readme/recommend.png)

### 📚 References
- [LIDA Github](https://github.com/microsoft/lida) – Original LIDA framework
- [llmx-gemini](https://github.com/tramphan748/llmx-gemini) – Custom Gemini integration for [llmx](https://github.com/victordibia/llmx)
- [YData Profiling](https://docs.profiling.ydata.ai/latest/) – Data profiling library for quick overviews
- [Streamlit Documentation](https://docs.streamlit.io/) – Building interactive data apps in Python

### 📖 Documentation and Citation
A paper describing LIDA (Accepted at ACL 2023 Conference) is available [here](https://arxiv.org/abs/2303.02927).

```bibtex
@inproceedings{dibia2023lida,
    title = "{LIDA}: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models",
    author = "Dibia, Victor",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-demo.11",
    doi = "10.18653/v1/2023.acl-demo.11",
    pages = "113--126",
}
```
