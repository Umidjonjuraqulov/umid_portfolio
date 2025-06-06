import streamlit as st 


st.title("Umidjon Juraqulov")

st.sidebar.image("images/umid_image.png")
st.sidebar.write("📞 **Phone**: +998 93 331 33 48")
st.sidebar.write("[✉️ **Email**](juraqulovumidjon0210@gmail.com)")
#col1, col2 = sidebar.columns((1, 7))
st.sidebar.write("[**GitHub**](https://github.com/Umidjonjuraqulov)")
#col1.sidebar.image("images/git_hup_logo.png",width=30)
st.sidebar.write("[**Instagram**](https://instagram.com/juraqulov_umidjon2003)")
#col1.sidebar.image("images/instagram_logo.png",width=30)
st.sidebar.write("[**Facebook**](https://www.facebook.com/profile.php?id=100079703570952&mibextid=ZbWKwL)")
#col1.sidebar.image("images/facebook_logo.avif",width=30)


st.subheader("Backend Developer")
st.markdown("***")
st.subheader("Education")

col1, col2 = st.columns((1, 7))
col1.image("https://uzfi.uz/static/assets/images/uzfi.png", width=80)
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
col2.write("Sep, 2023 - Sep, 2024")

st.write("")

col1, col2 = st.columns((1, 7))
col1.image("images/raccoons_logo.png", width=80)
col2.write("**Raccoons AI**") 
col2.write("Backend Developer Intern")
col2.write("Jan, 2025 - Present")
st.markdown("***")

st.subheader("Certificates")
st.write("HackerRank")
st.image("images/hackerrank.PNG")
st.write("Data: 05 nov, 2023")

st.write("HackerRank")
st.image("images/hackerrank.PNG")
st.write("Data: 05 nov, 2023")

