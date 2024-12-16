import streamlit as st

def show_API_key():
    st.header("_:blue[COHERE API KEY:]_")
    st.markdown("""
                Sau khi thử nghiệm với nhiều model :blue-background[large language model] khác nhau. Chúng tôi nhận thấy model từ nền tảng cohere :violet[command-xlarge-nightly] có hiệu suất tốt nhất. 
                Do đó chúng tôi sẽ hướng dẫn các bạn *step-by-step* kéo api cohere về.
                """)
    st.divider()
    st.markdown("#### Bước 1: Truy cập vào đường dẫn sau: *[cohere website](https://dashboard.cohere.com/welcome/login)* và đăng ký nếu bạn chưa có tài khoản.")
    st.image("C:/Users/PC/Desktop/SEMINAR/streamlit_app/assets/cohere-web/log_in.png", caption="Hình 1.Giao diện đăng nhập")

    st.markdown("""
                Sau khi đăng nhập thành công, cohere sẽ hiện giao diện *dashboard* như sau:
                """)
    st.image("C:/Users/PC/Desktop/SEMINAR/streamlit_app/assets/cohere-web/cohere-dashboard.png", caption="Hình 2.Giao diện dashboard")

    st.divider()
    st.markdown("#### Bước 2: Ở bên trái dashboard ta sẽ thấy mục :gray[API KEY]. Chọn vào mục đó: ")
    st.image("C:/Users/PC/Desktop/SEMINAR/streamlit_app/assets/cohere-web/cohere-b2.png", caption="Hình 3.API KEY")

    st.divider()
    st.markdown("#### Bước 3: Lưu :blue[API KEY] của mình về và nhập nó vào phần :blue[Nhập API KEY:] ở trang :red[Chức năng]" )
    st.image("C:/Users/PC/Desktop/SEMINAR/streamlit_app/assets/cohere-web/cohere-b3.png", caption="Hình 4. Lưu key về để sử dụng cho các tác vụ tiếp theo.")

    st.warning("""
            **Một số lưu ý khi sử dụng :violet[COHERE]:**  \n
            Vì đây là dự án dành cho những bạn không chuyên về ngành dữ liệu do đó:
            - Ưu tiên cho các giải pháp ít tốn kém nhất.
            - Đối với dự án của chúng tôi, :violet[COHERE] cho người dùng gửi yêu cầu tối đa 1000 lần mỗi tháng.
            """)

show_API_key()