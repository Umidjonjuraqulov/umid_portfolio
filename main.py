import streamlit as st 


st.title("Umidjon Juraqulov")

st.sidebar.image("images/umid_image.png")
st.sidebar.write("📞 **Phone**: +998 93 331 33 48")
st.sidebar.write("✉️ **Email**: juraqulovumidjon0210@gmail.com")
st.sidebar.write("**GitHub**: https://github.com/Umidjonjuraqulov")
st.sidebar.write("[**Umidjon Juraqulov**]( https://instagram.com/juraqulov_umidjon2003")


st.subheader("Backend Developer")
st.markdown("***")
st.subheader("Education")

col1, col2 = st.columns((1, 7))
col1.image("images/logouzfi.ico", width=80)
col2.write("**Uzbek-Finnish Pedagogical Institute**") 
col2.write("Bachelor, Mathematics and Informatics")
col2.write("2021-2025")

st.write("")

col1, col2 = st.columns((1, 7))
col1.image("images/samgasi.PNG", width=80)
col2.write("**Academic Lyceum under Samarkand State Architecture and Construction Institute**") 
col2.write("High School, Mathematics")
col2.write("2019-2021")
st.markdown("***")

st.subheader("Work")

col1, col2 = st.columns((1, 7))
col1.image("images/school_18.png", width=80)
col2.write("**School N-18**") 
col2.write("Mathematics Teacher")
col2.write("Sep, 2023 - Present")

st.write("")

col1, col2 = st.columns((1, 7))
col1.image("images/book_share_logo.png", width=80)
col2.write("**Book Share LLC**") 
col2.write("Backend Developer Intern")
col2.write("Sep, 2023 - Present")
st.markdown("***")