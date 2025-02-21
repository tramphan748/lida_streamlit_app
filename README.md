### 📊 Giới thiệu
Dự án [NTViz](https://ntviz-site.streamlit.app/) triển khai một ứng dụng Streamlit để thực hiện nhiều tác vụ phân tích, trực quan hóa dữ liệu và tương tác với mô hình ngôn ngữ lớn (LLM) thông qua framework [LIDA](https://github.com/microsoft/lida).

### 🛠️ Yêu cầu & Cài đặt

#### Cách 1: Sử dụng trên trang web
Truy cập trực tiếp [NTViz](https://ntviz-site.streamlit.app/) trên trình duyệt.

#### Cách 2: Chạy trên máy cục bộ
```bash
# Clone repository
git clone https://github.com/tramphan748/lida_streamlit_app.git
cd lida_streamlit_app

# Cài đặt các gói cần thiết
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run streamlit_app.py
```

**Lưu ý:** File `requirements.txt` bao gồm [llmx-gemini](https://github.com/tramphan748/llmx-gemini), một phiên bản tinh chỉnh của thư viện llmx hỗ trợ API Gemini. Nếu bạn đã cài đặt llmx thủ công ở chế độ editable, hãy đảm bảo cùng mã hoặc dòng git+... có trong requirements.txt.

### 📑 Tính năng

#### 1. Trang chủ (Dashboard)
Giới thiệu về dự án, tổng quan về khả năng và giao diện người dùng.

#### 2. Hướng dẫn lấy API Key
Hướng dẫn chi tiết để lấy API key từ hai nhà cung cấp chính:
- Cohere
- Gemini (sử dụng thư viện [llmx-gemini](https://github.com/tramphan748/llmx-gemini) đã được tùy chỉnh)

#### 3. Báo cáo dữ liệu (Data Report)
Tạo tổng quan toàn diện về dữ liệu:
- Tự động sinh các thống kê
- Biểu đồ và trực quan hóa
- Kiểm tra dữ liệu thiếu
- Phân tích tương quan
- Phân tích dữ liệu thăm dò cơ bản (EDA)

![Ví dụ về Data Report](/material/readme/data_overview.png)

#### 4. Các tác vụ LIDA

##### 4.1. Tóm tắt & Mục tiêu (Summarize & Goal)
Tận dụng LLM để tự động tạo:
- Tóm tắt dữ liệu
- Top 5 mục tiêu phân tích

![Ví dụ về Goal](/material/readme/insight0.png)
![Biểu đồ tương ứng](/material/readme/chart_insight0.png)
![Giao diện VizOps](/material/readme/Vizops.png)

##### 4.2. Biểu đồ dựa trên truy vấn người dùng
Tạo trực quan hóa dựa trên câu hỏi ngôn ngữ tự nhiên của người dùng.

![Ví dụ về truy vấn người dùng](/material/readme/userQuery_based_graphs.png)

##### 4.3. Đề xuất (Recommend)
Dựa trên tóm tắt, mục tiêu, mã nguồn và trực quan hóa đã tạo, hệ thống tự động đề xuất thêm 1-5 biểu đồ.

![Ví dụ về tác vụ VizRecommend](/material/readme/recommend.png)

### 📚 Tài liệu tham khảo
- [LIDA Github](https://github.com/microsoft/lida) – Framework LIDA gốc
- [llmx-gemini](https://github.com/tramphan748/llmx-gemini) – Tích hợp Gemini tùy chỉnh cho llmx
- [YData Profiling](https://docs.profiling.ydata.ai/latest/) – Thư viện lập hồ sơ dữ liệu
- [Streamlit Documentation](https://docs.streamlit.io/) – Xây dựng ứng dụng dữ liệu tương tác bằng Python

### 📖 Tài liệu và Trích dẫn
Bài báo mô tả LIDA (được chấp nhận tại Hội nghị ACL 2023) có thể xem [tại đây](https://arxiv.org/abs/2303.02927).

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
