import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Cấu hình giao diện Streamlit rộng toàn màn hình và đặt tiêu đề tab trình duyệt
st.set_page_config(
    page_title="Academic Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Sử dụng CSS để ẩn các thành phần mặc định của Streamlit (Menu góc phải, Footer)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
    </style>
""", unsafe_allow_html=True)

# 3. Hàm đọc nội dung file HTML
def load_html_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    return None

# Đọc file HTML của bạn (đặt tên file chính xác là index.html)
html_content = load_html_file("index.html")

if html_content:
    # 4. Nhúng toàn bộ giao diện HTML/CSS/JS vào Streamlit 
    # Chiều cao (height) được đặt lớn (ví dụ 1200px hoặc cao hơn) để chứa trọn vẹn dashboard mà không bị scroll 2 lần
    components.html(html_content, height=1500, scrolling=True)
else:
    st.error("Không tìm thấy file 'index.html'. Vui lòng kiểm tra lại thư mục dự án của bạn!")