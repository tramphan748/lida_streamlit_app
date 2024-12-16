import streamlit as st
from streamlit_option_menu import option_menu

def show_home():
    # Tạo menu với option_menu
    # selected = option_menu( 
    #     menu_title="NTViz Menu",
    #     options=["Home", "LIDA", "Contribute", "Source", "Support"],  # Các mục
    #     icons=["house", "bar-chart", "hand-thumbs-up", "book", "envelope"],  # Các biểu tượng
    #     menu_icon="cast",  # Biểu tượng menu
    #     default_index=0,  # Mục mặc định
    #     orientation="horizontal"  # Menu ngang
    # )

    home, lida, contr, source, contact = st.tabs(["Home", "LIDA", "Contribute", "Source", "Support"])
    # Hiển thị nội dung dựa trên mục đã chọn
    with home:
        st.title(" :violet[NTViz] _:gray[A Data Recommendation Systems For EveryOne]❤️!_")
        st.subheader(":grey[Tại sao chúng tôi xây dựng dự án này?]")
        st.markdown(""" 
                    _:blue[**"Dữ liệu là loại tiền tệ có giá trị nhất"**]_, là điều mà ta không thể nào phủ nhận được vì
                    chúng có các vai trò chủ chốt trong nhiều ngành nghề, lĩnh vực như:
                    - **Hỗ trợ ra quyết định:** cung cấp thông tin và phân tích để giúp tổ chức và cá nhân đưa ra các quyết định đáng tin cậy, từ chiến lược kinh doanh đến chi tiết về sản phẩm và dịch vụ.
                    - **Nâng cao hiệu quả hoạt động:** giúp tối ưu hóa hoạt động bằng cách cung cấp thông tin về hiệu suất, quy trình và khách hàng, giúp tổ chức điều chỉnh và cải thiện hoạt động để đạt hiệu quả cao hơn.
                    - **Phát triển sản phẩm và dịch vụ:** cung cấp thông tin về nhu cầu và phản hồi từ thị trường, giúp các doanh nghiệp hiểu rõ hơn về mong đợi của khách hàng và phát triển các sản phẩm và dịch vụ phù hợp.
                    - **Nghiên cứu và phát triển công nghệ:** là nguồn tài nguyên quan trọng cho các nghiên cứu khoa học và phát triển công nghệ, giúp nhà nghiên cứu phân tích và tạo ra các khám phá mới.
                    - **Tăng cường trải nghiệm khách hàng:** giúp cá nhân hóa trải nghiệm khách hàng, từ sản phẩm đến dịch vụ chăm sóc khách hàng, dựa trên thông tin cá nhân.                    
                    - **Giảm thiểu rủi ro và gian lận:** giúp phát hiện và ngăn chặn các hành vi gian lận và rủi ro trong kinh doanh và tài chính, thông qua phân tích các mô hình và xu hướng không bình thường. \n
                    ...và còn nhiều lợi ích khác từ dữ liệu có thể mang lại cho chúng ta. \n
                    Với số lượng dữ liệu ngày càng đa dạng và phức tạp, ta không thể nào hiểu chúng hết chỉ bằng cách đọc các dữ liệu thô được thu thập từ thực tế.
                    Với số lượng dữ liệu ngày càng đa dạng và phức tạp, việc chỉ đọc các dữ liệu thô thu thập từ thực tế không thể giúp chúng ta hiểu hết được giá trị của chúng. Làm thế nào để nắm bắt thông tin một cách nhanh chóng và dễ dàng nhất?\n
                    :point_right: Đáp án chính là :violet[**Trực quan hóa dữ liệu**], một công cụ mạnh mẽ giúp chúng ta chuyển hóa dữ liệu thành những hình ảnh dễ hiểu, từ đó đưa ra quyết định chính xác và hiệu quả hơn bao giờ hết. 
                    """)
        st.image("material/outlook/mhoa.jpg", caption="Hình 1. Minh họa",  use_container_width=True)    



        # Lí do vì sao trực quan hóa dữ liệu quan trọng
        st.markdown(""" 
                ### :grey[Mức độ quan trọng của :violet[Trực Quan Hóa Dữ Liệu]]:
                **1. Truyền tải thông tin một cách hiệu quả:**
                - Trực quan hóa giúp biểu diễn dữ liệu phức tạp dưới dạng hình ảnh dễ hiểu, giúp người xem nắm bắt nhanh thông tin mà không cần phân tích sâu các bảng số liệu.

                **2. Hỗ trợ ra quyết định:**
                - Các biểu đồ và hình ảnh trực quan giúp người ra quyết định nhận diện xu hướng, phát hiện vấn đề và đưa ra giải pháp phù hợp dựa trên dữ liệu cụ thể.

                **3. Phát hiện xu hướng và mối quan hệ:**
                - Trực quan hóa giúp làm nổi bật các xu hướng, mẫu hình (patterns), và mối quan hệ ẩn giữa các biến trong dữ liệu mà có thể bị bỏ qua khi chỉ nhìn vào dữ liệu thô.

                **4. Giao tiếp và thuyết phục:**
                - Các biểu đồ và hình ảnh trực quan hỗ trợ việc thuyết phục người khác, đặc biệt là trong các bài thuyết trình, báo cáo, hoặc tranh luận dựa trên dữ liệu.

                **5. Nâng cao khả năng phân tích dữ liệu:**
                - Giúp các nhà phân tích khám phá dữ liệu sâu hơn, phát hiện các giá trị bất thường (outliers) hoặc các khía cạnh chưa từng được xem xét, từ đó đưa ra những phân tích toàn diện hơn.
                
                **6. Tăng khả năng tương tác với dữ liệu:**
                -  Tương tác với dữ liệu thông qua hình ảnh, và các thông tin số liệu quan trọng như doanh số, phân phối,...
                
                **7. Tạo cảm giác hứng thú với dữ liệu:**
                - Hình ảnh sinh động và trực quan không chỉ làm cho dữ liệu bớt khô khan mà còn giúp người không chuyên có thể tìm hiểu sâu hơn về dữ liệu và các vấn đề liên quan 1 cách đơn giản, dễ hiểu hơn.
                
                """)
        st.image("material/outlook/ex_tquan.jpg", caption="Hình 2. Ví dụ Trực Quan")
        
        
        
        st.divider()
        st.markdown("### :grey[Bài Toán Chính:]")
        st.markdown("""
                    Tuy nhiên, nếu 1 người không có các kỹ năng lập trình muốn tìm hiểu sâu, rút trích thông tin từ bộ dữ liệu của mình thì họ sẽ vấp phải các khó khăn như:
                    - Nên trực quan hóa theo biến nào? Biểu đồ đó có ý nghĩa gì?
                    - Nên chọn biểu đồ nào để trực quan hóa cho bộ dữ liệu?
                    - Làm thế nào để hiện thực hóa biểu đồ đó khi không có kỹ năng lập trình? \n
                    Nhận thấy được điều đó, chúng tôi ấp ủ kế hoạch và tìm hiểu các tool có thể hỗ trợ :blue["Những người không chuyên về dữ liệu"] một cách đơn giản, và ít tốn kém nhất.
                    ##### :point_right: Bằng cách xây dựng :violet[Hệ Thống Gợi Ý Biểu Đồ] dựa trên bộ dữ liệu của người dùng.
                    """)
    

    with lida:
        st.header(":grey[LIDA: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models]")
        st.markdown("### *Tổng quan về LIDA:*")
        st.markdown(""" 
                    - LIDA là nền tảng tạo biểu đồ dựa trên LLM, thuộc sở hữu của Microsoft, gồm 4 module chính: Summarize, Goal Explorer, VisGenerator và Infographic
                    - Hệ thống sử dụng LLM để tóm tắt dữ liệu, tạo mục tiêu, sinh mã và tạo biểu đồ tự động
                    """)
        st.markdown(""" 
                    ##### Ưu điểm:
                    - Tự động tạo giả thuyết/mục tiêu từ dữ liệu, hỗ trợ nhiều ngữ pháp trực quan, và có khả năng tạo infographic
                    - Hiệu quả hơn các hệ thống hiện có, đơn giản hóa quá trình tạo biểu đồ phức tạp
                    - Giới thiệu các chỉ số đánh giá độ tin cậy (VER) và chất lượng trực quan hóa (SEVQ)
                    """)
        st.markdown(""" 
                    ##### Nhược điểm:
                    - Cần nghiên cứu thêm về tác động của độ phức tạp tác vụ và lựa chọn ngôn ngữ lập trình đến hiệu suất
                    - Yêu cầu nhiều tài nguyên tính toán, cần cải thiện về triển khai và độ trễ
                    - Cần phát triển các tiêu chuẩn đánh giá toàn diện hơn và nghiên cứu về khả năng giải thích hành vi của hệ thống
                    """)
        
        st.markdown("### *Chi tiết các hoạt động của LIDA:*")
        st.markdown(""" 
        1. **Summarize and Goals:** \n
            *a. Summarize dựa theo rule và LLM:*
            -    Dùng LLM để tạo nên một mô tả ngắn, cô đọng về cái tập dataset qua 2 stage process mà người dùng bỏ vào nhằm định hướng được mục tiêu, hoặc gợi ý, ví dụ như đối với tập dữ liệu này thì mình có thể làm được những gì, như thế nào. \n
            *b. Goal Explorer:*
            -    Nhìn chung trong step này, nó sẽ tạo ra 1 tập file .JSON gồm 3 đối tượng: “question”, “visualization”, “rationale”
            - Question:
                - LLM đóng vai trò như người dùng, người hướng dẫn, tự bản thân nó sẽ đi khám phá, tìm hiểu về tập dữ liệu này để đưa ra các giả thuyết như là các câu hỏi
            - Visualization:
                - Tên và loại biểu đồ
            - Rationale:
                - Biểu đồ mang ý nghĩa như thế nào? Đưa ra những "insight" gì?        
        """)
        st.image("material/lida/goals.png", caption="Hình 2. Cấu trúc của Goals",
                use_container_width=True)
        
        st.markdown("""
        2. **VisGenerator:**
        Tạo ra biểu đồ cụ thể, thực hiện dựa theo 3 module con: \n 
            *a. Code scaffold constructor:* \n
            Tiến hành thư viện mã scafffolds tương ứng với ngôn ngữ lập trình Scaffolds support `Matplotlib`, `GGPlot`, `Plotly`, `Altair`, `Seaborn`, và `Boken`
            
            *b. Code generator:* \n
            Lấy scaffold, bộ dữ liệu mà ta đã tóm tắt, mục tiêu trực quan và prompt mà ta đã dựng sẵn đưa vào LLM
            
            *c. Code executor:*  
            
            Thực hiện vẽ, tạo biểu đồ cụ thể.
        """)
        st.image("material/lida/example.png", caption="Hình 3. Biểu đồ tương ứng", 
                use_container_width=True)   
        st.markdown("""
        3. **Infographic:**
            - Module này được sử dụng để tạo ra những cái đồ thị dựa trên kết quả đầu ra của VisGenerator
            - Sử dụng text-conditioned image-to-image ( khả năng tạo ảnh từ văn bản trong các mô hình khuếch tán) (Rombach và cộng sự, 2022), được triển khai qua API của thư viện Peacasso (Dibia, 2022).
            """)
        
        st.image("material/lida/infograp.png", 
                caption="Hình 4: Minh họa infographic của LIDA",
                use_container_width=True)
        
        st.divider()
        
        # Thông tin LIDA hỗ trợ các nền tảng nào
        # Các điều kiện cần lưu ý
        st.markdown("### _:grey[📌 Những lưu ý quan trọng:]_")
        st.markdown(""" 
                    ##### 1. Python:
                    LIDA yêu cầu Python từ version 3.10 trở lên.
                    ##### 2. Dữ liệu: 
                    Phù hợp nhất với tập dữ liệu có <= 10 cột. Đối với dữ liệu lớn hơn, cần xử lý trước (chọn cột phù hợp).
                    ##### 3. Khả năng hoạt động: 
                    LIDA yêu cầu dữ liệu ở định dạng như .csv hoặc .json (danh sách đối tượng).
                    ##### 4. Hiệu quả: 
                    LIDA hoạt động tốt hơn với các LLM lớn (GPT-3.5, GPT-4). Các mô hình nhỏ hơn có thể không theo sát hướng dẫn tốt.
                    ##### 5. Độ chính xác: 
                    Tỷ lệ lỗi < 3.5% trên 2200 biểu đồ được tạo, thấp hơn mức cơ bản (>10%).
                    ##### 6. Large Language Model: 
                    LIDA sử dụng các mô hình ngôn ngữ lớn như 1 người quản lý giúp người dùng sử dụng các tác vụ của nó.
                    - OpenAI (sử dụng bằng cách kéo API KEY từ trang web)
                    - COHERE (là nền tảng chính mà chúng tôi sử dụng)
                    - Các LLM trên HUGGING FACE như là: [microsoft/Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) hoặc [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
                        - Lưu ý: 
                            - Nếu như máy tính của bạn không có GPU thì chúng tôi khuyên bạn hãy chạy trên các phần mềm thay thế như Google Colab, Kaggle.
                            - Nếu bạn muốn trải nghiệm các model trên HUGGING FACE thì các model cần đạt các điều kiện sau:
                                1. Được huấn luyện với tác vụ **text-generation**, đưa tập dữ liệu về định dạng **.json** thì mới hợp lệ.
                                2. **max_tokens_length > 1024**
                                3. **1B <=  Số parameters  <= 4B** (vì GPU P100 hoặc T4 chỉ có thể chạy được model có số parameters nhỏ hơn 4B)
                                4. Đặt thêm giới hạn cho số lượng tokens tạo mới, max_tokens cho nó, nếu không thì máy sẽ mất nhiều thời gian để có thể chạy ra kết quả.
                    """)

    with contr:
        st.subheader("_:grey[Sự Đóng góp của NTViz]_")
        st.markdown(""" 
                    Đề tài này đóng góp vào việc hỗ trợ những người làm trong các lĩnh vực cần nhiều thông tin, các tệp dữ liệu nhưng không chuyên, hoặc các bạn học sinh, sinh viên không có kiến thức nền về Phân Tích Dữ Liệu dễ dàng tiếp cận và trực quan hoá các tập tin của mình nhằm phục vụ cho mục đích của bản thân.
                    - **Hỗ trợ những người không chuyên về Phân tích Dữ liệu:** giúp làm sạch và dùng biểu đồ để trực quan hoá dữ liệu của họ.
                    - **Đề xuất các biểu đồ tự động:** giúp tối ưu hóa hiệu quả bằng cách tự động đề xuất các biểu đồ trực quan hóa theo các chủ đề mà người dùng muốn hướng tới.
                    - **Tiết kiệm thời gian:** Tự động hóa quy trình lựa chọn biểu đồ phù hợp, giúp người dùng tiết kiệm thời gian và giảm bớt việc thử-sai.
                    - **Cải thiện khả năng tiếp cận dữ liệu:** Giảm rào cản trong việc truy cập và trực quan hóa dữ liệu cho những người không có kỹ năng kỹ thuật, từ đó khuyến khích việc sử dụng dữ liệu trong quyết định kinh doanh hoặc nghiên cứu.
                    - **Công cụ học tập:** Từ việc đề xuất biểu đồ, hệ thống đóng vai trò như một công cụ học tập cho các học sinh, sinh viên hoặc người đi làm, giúp họ hiểu rõ các nguyên tắc trực quan, diễn giải, ý nghĩa của biểu đồ được đề xuất.   
                    - **Khả năng mở rộng và tích hợp:** Hệ thống có tiềm năng được mở rộng và tích hợp vào các nền tảng phân tích khác, giúp tối ưu hóa quy trình làm việc của nhiều doanh nghiệp và tổ chức.
                    """)
        
        st.divider()
        # Những cải tiến mới chúng tôi đề xuất
        st.subheader("_:grey[Cải tiến mới trong LIDA:]_")
        st.markdown(""" 
                    Sau khi tìm hiểu kĩ càng về các tác vụ trong LIDA, chúng tôi nhận thấy:
                    - Trong LIDA, khi nhập đầu vào bộ dữ liệu thì LIDA không có tính năng "Cleaning DATA" sẵn cho người dùng.
                    - Tính năng "summarize" của nó chưa đủ rõ ràng và trực diện. Ví dụ:
                    """)
        st.image("material/lida/summary.png", 
                caption="Hình 1. Ví dụ về bảng tóm tắt của 1 cột dữ liệu.",
                use_container_width=True)
        st.markdown(""" 
                    - Tính năng tạo biểu đồ dựa trên câu truy vấn có nhiều tiềm năng. Nó có thể tạo tốt từ 3 đến 5 biểu đồ chỉ dựa theo câu truy vấn mà người dùng đưa ra.
                    """)
        st.markdown("""
                    Do đó, chúng tôi đề xuất thêm:
                    - Tích hợp thư viện `ydata_profiling` để đưa ra những thông tin chung trực diện hơn cho bộ dữ liệu.
                    - Trước khi LIDA **"summarize"** và **"goals explorer"**, chúng tôi sẽ tích hợp thêm 1 hàm giúp người dùng kiểm tra dữ liệu đã sạch hay chưa, nếu chưa thì chúng tôi sẽ làm sạch giúp họ.
                    """)
        st.image("material/lida/overview.png", 
                caption="Hình 2. Minh Họa Overview",
                use_container_width=True)

    # Nguồn tham khảo
    with source:
        st.subheader("_:grey[Nguồn Tham Khảo và Ghi Nhận:]_")
        st.markdown("[LIDA: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models](https://aclanthology.org/2023.acl-demo.11) (Dibia, ACL 2023)")
        st.markdown("[COHERE, API KEY](https://dashboard.cohere.com/?_gl=1*5bkinq*_gcl_au*MTQ5NTExMTE3MS4xNzMwOTcxODg1*_ga*NTc0ODQ4NDk0LjE3MzA5NzE4ODI.*_ga_CRGS116RZS*MTczNDI0Njk5Ni4yMi4wLjE3MzQyNDY5OTYuNjAuMC4w)")
        st.write("_:violet[Chúng tôi xin trân trọng gửi lời cảm ơn chân thành đến :blue[LIDA] và :blue[COHERE] vì đã cung cấp các công cụ và dịch vụ tuyệt vời, giúp dự án này trở nên khả thi. Không có sự hỗ trợ của họ, chúng tôi không thể đạt được kết quả như hiện tại. ❤️]_")    

    with contact:
        st.subheader("📞 :grey[Liên hệ]")
        st.markdown("""
        - **Email**: support@ntviz.com
        - **Website**: [NTViz](https://ntviz.com)
        - **Hotline**: 0123-456-789
        """)


show_home()
