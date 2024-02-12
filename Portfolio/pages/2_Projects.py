import streamlit as st
import base64

st.set_page_config(page_title="Projects", page_icon="🔨")

st.markdown("<h1 style='text-align: center; color: green;'>Projects</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,150,1])

with col2:
    with st.container(border=True):
        st.header("DJ Turntable")
        st.subheader("http://areawebsites.org/mLeVardi/DJTurntable/index.html")
        st.markdown("#")
        st.header("Portals Site")
        st.subheader("http://areawebsites.org/mLeVardi/HtmlPortal/index.html")
        st.markdown("#")
        st.header("Netflix Movies Data")
        st.subheader("http://areawebsites.org/mlevardi/PHP/netflixMovies.php")
        st.markdown("#")
        st.header("Realestate Website")
        st.subheader("http://areawebsites.org/mlevardi/Realestate/index.php")
        st.markdown("#")
        st.header("FNaCK")
        st.subheader("http://areawebsites.org/mlevardi/fnack/index.html")
        st.markdown("#")