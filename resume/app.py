from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic_path = current_dir / "assets" / "pic.png"
poem_files = [current_dir / f"assets/poem{i}.pdf" for i in range(1, 8)]


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Reva Rochanaa"
PAGE_ICON = ":wave:"
NAME = "Reva Rochanaa"
DESCRIPTION = "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making."
EMAIL = "rrochanaa@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com"
}
EDUCATION = [
    "Mepco Schlenk Engineering College - Bachelor of Engineering in Computer Science",
    "Y.R.T.V Mat.Hr.Sec SCHOOL - Higher Secondary Certificate 2019-2021"
]
SYMPOSIUMS = [
    "KRETA 23 - Coder's den, Thiyagarajar College of Engineering Jan '23",
    "ORION 23 - Kongu Engineering College Dec '23",
    "SIH Internal Hackathon, Mepco Schlenk"
]
WORKSHOPS = [
    "Attended a three-day Capacity Building Programme on Computer Accessories and Network Installation and Troubleshooting by Mepco Schlenk Engineering",
    "Participated in a three-day boot camp workshop on startups and branding for marketing success by TN Startups",
    "Participated in a three-day Ethical Tech Summit at IIT Madras where IBM workshops emphasized AI ethics"
]
ACHIEVEMENTS = [
    "Published articles in college magazine Virtuoso Digest",
    "Shortlisted for TNSTG startup contest",
    "Shortlisted in national level doodle contest by ELTAI",
    "Academic Scholarship for the year 2021, GVN College",
    "Creative Writing winner and published article in the magazine"
]
PROJECTS = [
    "Datastructure project on college seat bookings using C",
    "Hospital management using DBMS",
    "Website ice cream portfolio project",
    "Microprocessor project a pedometer watch ⌚"
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
for edu in EDUCATION:
    st.write(f"- {edu}")

# --- SYMPOSIUMS ---
st.write('\n')
st.subheader("Symposiums")
for symposium in SYMPOSIUMS:
    st.write(f"- {symposium}")

# --- WORKSHOPS ---
st.write('\n')
st.subheader("Workshops")
for workshop in WORKSHOPS:
    st.write(f"- {workshop}")

# --- ACHIEVEMENTS ---
st.write('\n')
st.subheader("Achievements")
for achievement in ACHIEVEMENTS:
    st.write(f"- {achievement}")

# --- PROJECTS ---
st.write('\n')
st.subheader("Projects")
for project in PROJECTS:
    st.write(f"- {project}")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), VBA
- 📊 Data Visualization: MS Excel, Tableau
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: MySQL
"""
)
# --- POEMS ---
st.write('\n')
st.subheader("Poems")
for i, poem_file in enumerate(poem_files, 1):
    with open(poem_file, "rb") as file:
        poem_bytes = file.read()
        st.download_button(
            label=f"📄 Download Poem {i}",
            data=poem_bytes,
            file_name=f"poem{i}.pdf",
            mime="application/pdf",
        )
