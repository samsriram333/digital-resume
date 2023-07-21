from pathlib import Path
import streamlit as st
from PIL import Image

#Path settings

current_dir =  Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file    = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"sriram.pdf"
profile_pic = current_dir/"assets"/"profile-pic (3).png"

#General settings

PAGE_TITLE = "Digital CV | Sriram Jayavel"
PAGE_ICON = ":wave:"
NAME = "Sriram Jayavel"
DESCRIPTION = """
Junior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "samsriram333@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sriram-jayavel-b9822711b/",
    "GitHub": "https://github.com/samsriram333",
}
PROJECTS = {
    "🏆 Worked on increase the number of users rentention" ,
    "🏆 Worked on increase the app average time" ,
    "🏆 Worked on Mental health well being at pandamic time project",
}
st.set_page_config(page_title = PAGE_TITLE , page_icon = PAGE_ICON )

st.title("Hello there!")

#Load Css,Profile Pic and Pdf

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file,'rb') as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

#Hero Section
col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.write("📫",EMAIL)
#Social_links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#Experience and qualification:
st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
- ✔️ 1 Year experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Tableau and SQL
- ✔️ Good understanding of statistical principles and their respective applications 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
""")

st.write("#")
st.subheader("Hard Skills")
st.write("""
        
    - 👩‍💻 Programming: Python (Pandas , Numpy , SK learn, Matplotlib) , SQl 
    - 📊 Data Visulization: Tableau , PowerBI
    - 🗄️ Databases: Postgres , MySQL
""")
#Work History
st.write("#")
st.subheader("Work Experience")
st.write("""___""")
#Job - 1
st.write("🚧","Data Analyst | Pepul")
st.write("Aug 2022 - Present")
st.write("""
-  ► During my one year of experience as a Data Analyst, I demonstrated proficiency in various areas.
-  ► I utilized Tableau to build interactive dashboards tailored for different teams such as Creators, Growth, Content Moderation, AI-ML and Finance
-  ► Additionally, I established end-to-end pipelines, fetching data from databases, creating Tableau dashboards, publishing them to Tableau Cloud, and setting up scheduled refreshes and subscriptions to send reports via email to team heads.
-  ► I actively communicated insights by sending daily reports to the CEO and CTO through email and Slack.
-  ► My skillset extended to SQL for database querying, Python for exploratory data analysis (EDA), and Excel for reporting. Lastly, I incorporated statistical concepts to enhance the analytical process and deliver data-driven insights for informed decision-making across the organization.
""")

# Job - 2
st.write("#")
st.write("🚧", "Junior - Data Scientist | Innodatatics ")
st.write("Jan 2022 - May 2022")
st.write("""
-  ► During my internship at Innoatatics, our team worked together on a project called "Mental Health Wellbeing at Pandemic Times." We used machine learning algorithms to predict mental health-related outcomes.
-  ► Alongside that, we collaborated on building a website using HTML, CSS, and Flask.    
    """)

# Job - 3
st.write("#")
st.write("🚧", "Fraud Analyst | TCS ")
st.write("May 2016 - Aug 2022")
st.write("""

   -  ►  I have done an excellent job as a Credit Card Chargeback Analyst, specializing in important areas.
   -  ►  My tasks included managing chargeback processes, implementing strong measures to prevent fraud, and representing clients in resolving disputes.
   -  ►  I understand MasterVisa and Visa card procedures well and can handle Amex card chargebacks effectively.
   -  ►  I always focus on being accurate, efficient, and following industry rules, which consistently leads to positive results for clients and the company.
   -  ►  With a proven track record of successfully solving complex chargeback cases and reducing financial losses, I am ready to handle the ever- changing challenges of credit card chargeback analysis.
       
       """)

#Projects & Accomplishments
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("___")
for project in PROJECTS:
    st.write(f"{project}")
