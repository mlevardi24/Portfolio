import streamlit as st
import base64

st.set_page_config(page_title="Resume", page_icon="📄")

st.markdown("<h1 style='text-align: center; color: blue;'>Resume</h1>", unsafe_allow_html=True)


def ViewPDF(wch_fl):
    with open(wch_fl,"rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        pdf_display = f'<center><embed style="text-align:center; margin: 0 auto;" src="data:application/pdf;base64,{base64_pdf}" width="1000" height="750" type="application/pdf"></center>' 
        st.markdown(pdf_display, unsafe_allow_html=True)

ViewPDF("Portfolio/Resume.pdf") 
