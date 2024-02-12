import streamlit as st
import base64

st.set_page_config(
    page_title="Portfolio",
    page_icon="👋",
)



col1, col2, col3 = st.columns([1,25,1])

with col2:
    st.markdown("<h1 style='text-align: center; color: red;'>Michael's Portfolio</h1>", unsafe_allow_html=True)
    st.subheader("Hi! I'm a Computer Programmer. Here you can find some projects I've worked on, as well as my resume.")
    
st.divider()

st.markdown('#')

with st.container(border=True):
    st.subheader("Languages I know:")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.image("images/htmlIcon.png")
    with col2:
        st.image("images/JSIcon.png")
    with col3:
        st.image("images/CSSIcon.png")
    with col4:
        st.image("images/PythonIcon.png")
    with col5:
        st.image("images/C#Icon.png")
    with col6:
        st.image("images/PHPIcon.png")

st.markdown('#')
st.markdown('#')

with st.container(border=True):
    col1, col2 = st.columns([3,3])
    with col1:
        st.header("I'm currently a Senior in Columbia Montour Vo-Tech, taking a Computer Technology Course.")
    with col2:
        st.image("Images/Rams.png")