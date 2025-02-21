## Giới thiệu
Dự án [NTViz](https://ntviz-site.streamlit.app/) triển khai một ứng dụng Streamlit để thực hiện nhiều tác vụ phân tích, trực quan hóa dữ liệu và tương tác với mô hình ngôn ngữ (LLM) thông qua framework [LIDA](https://github.com/microsoft/lida).
## Prerequisites & Installation
#### 1. Sử dụng trên trang web:
Truy cập [NTViz](https://ntviz-site.streamlit.app/)
#### 2. Chạy local:
##### Clone the repository:
```
git clone https://github.com/tramphan748/lida_streamlit_app.git
cd lida_streamlit_app
```
##### Install the required packages:
```
pip install -r requirements.txt
```
The file requirements.txt includes an install line for  [llmx-gemini](https://github.com/tramphan748/llmx-gemini)
This ensures you have the correct version of the llmx library that can call the Gemini API.
If you manually installed llmx in editable mode on your local machine, you’ll need to ensure that the same code or git+... line is present in requirements.txt (which it is in this repo).

##### Usage
```
streamlit run streamlit_app.py
```
## Mục lục
#### 1. Dashboard: Giới thiệu về project.
#### 2. Instruction to get API KEY: Hướng dẫn lấy API key từ 2 provider chính là Cohere và Gemini.
(Lưu ý: vì [llmx](https://github.com/victordibia/llmx) không hỗ trợ provider Gemini nên chúng tôi đã tinh chỉnh thư viện thành [llmx-gemini](https://github.com/tramphan748/llmx-gemini) để có thể call API từ Gemini).
#### 3. Data Report: Tạo báo cáo tổng quan về dữ liệu (tự động sinh các thống kê, biểu đồ, kiểm tra missing values, correlation,…), EDA cơ bản.
![Ví dụ về Data Report](/material/readme/data_overview.png)
#### 4. LIDA tasks:
##### 4.1. Summerize & Goal: Dựa vào LLM để tự động tạo Summerize và top 5 Goals cho dữ liệu.
![Ví dụ về 1 Goal](/material/readme/insight0.png)
![Biểu đồ của Goal tương ứng](/material/readme/chart_insight0.png)
![VizOps](/material/readme/Vizops.png)

##### 4.2. User Query Based Graphs: Tạo biểu đồ dựa trên câu hỏi của người dùng.
  
![Ví dụ về 1 user query](/material/readme/userQuery_based_graphs.png)

##### 4.3. Recommend: Dựa trên summerize, goal, code, các biểu đồ đã được tạo, hệ thống sẽ tự động gợi ý thêm từ 1 đến 5 biểu đồ.
![Ví dụ về task VizRecommend](/material/readme/recommend.png)

### References
[LIDA Github] (https://github.com/microsoft/lida) – Original LIDA framework.
[llmx-gemini](https://github.com/tramphan748/llmx-gemini) – Custom Gemini integration for llmx.
[YData Profiling](https://docs.profiling.ydata.ai/latest/) – Data profiling library used for generating quick data overviews.
[Streamlit Documentation](https://docs.streamlit.io/) – Building interactive data apps in Python.

###  Documentation and Citation

A short paper describing LIDA (Accepted at ACL 2023 Conference) is available [here](https://arxiv.org/abs/2303.02927).

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
