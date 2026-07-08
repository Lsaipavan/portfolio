import streamlit as st
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Sai Pavan",
    page_icon="💻",
    layout="wide"
)

# ---------------- LINKS ---------------- #

github = "https://github.com/Lsaipavan"

linkedin = "https://www.linkedin.com/in/saipavan-lingampelly-337a58257?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"

gmail = "mailto:saipavanlingampelly@gmail.com"

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#081b29,#0d2b45,#081b29);
}
.card{
    background:#112e42;
    padding:25px;
    border-radius:18px;
    border:1px solid #00abf0;
    box-shadow:0px 4px 15px rgba(0,171,240,0.25);
    margin-bottom:20px;
}

.title{
    text-align:center;
    color:#00abf0;
    font-size:42px;
    font-weight:bold;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:20px;
    padding-left:50px;
    padding-right:50px;
}

.big{
    font-size:70px;
    font-weight:bold;
    color:white;
}

.role{
    font-size:35px;
    color:#00abf0;
}

.summary{
    font-size:18px;
    color:#d8d8d8;
    line-height:1.8;
}

.stDownloadButton button{
    background:#00abf0;
    color:white;
    border-radius:30px;
    border:none;
    font-size:18px;
    padding:12px 35px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ---------------- #

selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "About",
        "Skills",
        "Projects",
        "Contact"
    ],
    icons=[
        "house",
        "person",
        "code-slash",
        "folder",
        "telephone"
    ],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":

    st.write("")
    st.write("")

    left, right = st.columns([2.2,1])

    with left:

        st.write("## Hello, I'M")

        st.markdown("""
        <div class="big">
        SAI PAVAN LINGAMPELLI
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="role">
        Data Scientist | Data Analyst | Python Developer
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="summary">

        Passionate Data Science Fresher with strong knowledge in
        Python, SQL, Machine Learning, Data Analysis,
        Power BI and Streamlit.

        I enjoy solving real-world problems using AI,
        building Machine Learning models,
        and transforming data into business insights.

        Currently looking for opportunities as a

        ✔ Data Analyst

        ✔ Data Scientist

        ✔ Python Developer

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div style="display:flex;gap:18px;">

        <a href="{github}" target="_blank">
        <img src="https://img.icons8.com/fluency/48/github.png" width="45">
        </a>

        <a href="{linkedin}" target="_blank">
        <img src="https://img.icons8.com/color/48/linkedin.png" width="45">
        </a>

        <a href="{gmail}">
        <img src="https://img.icons8.com/color/48/gmail-new.png" width="45">
        </a>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        with open("assets/PAVAN.pdf", "rb") as pdf:

            st.download_button(
                "⬇ Download Resume",
                pdf,
                file_name="PAVAN.pdf"
            )

    with right:

        st.image("assets/image.png", width=330)

elif selected == "About":

    st.markdown(
        "<div class='title'>About Me</div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown("""
<div class="card">

<h2>👋 Hi, I'm Sai Pavan</h2>

<p>

I am a passionate <b>Data Science Fresher</b> with a strong interest in
Python, SQL, Machine Learning, Data Analytics, Streamlit and Power BI.

I enjoy building practical projects, solving real-world problems using data,
and continuously learning new technologies.

Currently looking for opportunities as a
<b>Data Analyst, Data Scientist, or Python Developer.</b>

</p>

</div>
""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
    <div class="card">
    <h3>📌 Personal Details</h3>

    <p>
    📍 Hyderabad<br><br>
    💼 Experience : Fresher<br><br>
    🌍 Languages : English, Telugu, Hindi
    </p>

    </div>
    """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
    <div class="card">
    <h3>🏆 Certifications</h3>

    <p>
    ✔ Python Programming<br><br>
    ✔ SQL for Data Analysis<br><br>
    ✔ Power BI Fundamentals<br><br>
    ✔ Machine Learning Basics
    </p>

    </div>
    """, unsafe_allow_html=True)
            st.write("")
            st.subheader("📊 Quick Facts")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Projects", "3+")
            m2.metric("Skills", "10+")
            m3.metric("CGPA", "8.42")
            m4.metric("Experience", "Fresher")
elif selected == "Skills":

    st.markdown("""
    <div class='title'>
    Technical Skills
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ================= TWO COLUMNS =================

    left, right = st.columns(2)

    with left:

        st.markdown("""
        <div class="card">
        <h3>💻 Programming Skills</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("Python")
        st.progress(90)

        st.write("SQL")
        st.progress(85)

        st.write("HTML")
        st.progress(75)

        st.write("CSS")
        st.progress(70)

    with right:

        st.markdown("""
        <div class="card">
        <h3>📊 Data Science Skills</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("Machine Learning")
        st.progress(85)

        st.write("Data Analysis")
        st.progress(90)

        st.write("Power BI")
        st.progress(80)

        st.write("Streamlit")
        st.progress(85)

    st.write("")

    # ================= LIBRARIES =================

    st.markdown("""
    <div class="card">
    <h3>📚 Libraries & Frameworks</h3>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("🐼 Pandas")
        st.success("📈 Matplotlib")

    with c2:
        st.success("🔢 NumPy")
        st.success("📊 Seaborn")

    with c3:
        st.success("🤖 Scikit-Learn")
        st.success("🌐 Streamlit")

    with c4:
        st.success("📓 Jupyter")
        st.success("⚡ VS Code")

    st.write("")

    # ================= TOOLS =================

    st.markdown("""
    <div class="card">
    <h3>🛠 Tools & Technologies</h3>
    </div>
    """, unsafe_allow_html=True)

    t1, t2, t3 = st.columns(3)

    with t1:
        st.info("💻 Python")
        st.info("🐙 GitHub")
        st.info("📄 Excel")

    with t2:
        st.info("📊 Power BI")
        st.info("🗄 SQL Server")
        st.info("📓 Jupyter")

    with t3:
        st.info("🌐 Streamlit")
        st.info("💻 VS Code")
        st.info("🔗 Git")

    st.write("")

    # ================= SOFT SKILLS =================

    st.markdown("""
    <div class="card">
    <h3>🌟 Soft Skills</h3>
    </div>
    """, unsafe_allow_html=True)

    s1, s2 = st.columns(2)

    with s1:
        st.success("✔ Problem Solving")
        st.success("✔ Communication")
        st.success("✔ Team Work")

    with s2:
        st.success("✔ Time Management")
        st.success("✔ Quick Learner")
        st.success("✔ Critical Thinking")

    st.write("")

    # ================= CURRENT LEARNING =================

    st.markdown("""
    <div class="card">
    <h3>🚀 Currently Learning</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    • Deep Learning

    • Generative AI

    • Advanced SQL

    • NLP

    • End-to-End Machine Learning

    • Model Deployment using Streamlit
    """)

elif selected == "Projects":
    st.markdown("""
<div class="title">

My Projects

</div>
""", unsafe_allow_html=True)
    st.write("")
    st.markdown("""
<div class="card">

<h2>🏦 Loan Approval Prediction Using Machine Learning</h2>

<p>

<b>Technologies Used:</b><br>

Python • Pandas • NumPy • Scikit-Learn • Streamlit

<br><br>

<b>Project Overview</b><br>

Developed a machine learning solution that predicts whether a loan
application is likely to be approved based on applicant information
such as income, credit history, education, and loan amount.

The project included data preprocessing, feature engineering,
model training, hyperparameter tuning, and performance evaluation.

<br><br>

<b>Result</b><br>

✅ Achieved <b>87% prediction accuracy</b>

<br><br>

<b>Business Impact</b><br>

Helped demonstrate how machine learning can support banks in making
faster and more consistent loan approval decisions while reducing
manual evaluation time.

</p>

</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="card">

<h2>🎗 BreastCare AI – Breast Cancer Risk Prediction</h2>

<p>

<b>Technologies Used:</b><br>

Python • CNN • Random Forest • Logistic Regression • SHAP • LIME

<br><br>

<b>Project Overview</b><br>

Designed an AI-powered application capable of predicting breast cancer
risk using machine learning and deep learning models.

Implemented Explainable AI techniques to improve model transparency
and assist users in understanding prediction results.

<br><br>

<b>Result</b><br>

✅ Achieved <b>91% validation accuracy</b>

<br><br>

<b>Real-World Impact</b><br>

Demonstrates how AI can assist healthcare professionals by supporting
early risk assessment and improving decision-making with explainable predictions.

</p>

</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="card">

<h2>🌍 Smart Smog – Air Pollution Monitoring System</h2>

<p>

<b>Technologies Used:</b><br>

Arduino • MQ135 Sensor • IoT

<br><br>

<b>Project Overview</b><br>

Developed a low-cost IoT-based air quality monitoring system capable
of detecting harmful gases in real time.

The system continuously monitors environmental conditions and
generates alerts whenever pollution exceeds safe levels.

<br><br>

<b>Key Features</b><br>

✔ Real-time air quality monitoring

✔ Pollution alerts

✔ Health risk notifications

✔ Low-cost implementation

<br><br>

<b>Real-World Impact</b><br>

Provides an affordable solution that can help individuals and local
authorities monitor pollution levels and encourage timely preventive action.

</p>

</div>
""", unsafe_allow_html=True)
    st.write("")
    st.success("More projects are currently under development.")

elif selected == "Contact":
    st.markdown("""
<div class='title'>
Contact Me
</div>
""", unsafe_allow_html=True)
    st.write("")
    left, right = st.columns([1.2,1])
    with left:
        st.markdown("""
    <div class="card">

    <h2>Let's Work Together 🤝</h2>

    <p>

    Thank you for visiting my portfolio.

    I'm currently looking for opportunities as a

    ✔ Data Analyst

    ✔ Data Scientist

    ✔ Python Developer

    I would be happy to discuss internships,
    full-time opportunities, freelance work,
    or collaborative projects.

    </p>

    </div>
    """, unsafe_allow_html=True)
        st.write("📧 **Email**")
        st.write("saipavanlingampelly@gmail.com")
        st.write("")
        st.write("📱 **Phone**")
        st.write("+91 7995800747")
        st.write("")
        st.write("📍 **Location**")
        st.write("Hyderabad, Telangana, India")
        with right:
            st.markdown("""
    <div class="card">

    <h3>Connect With Me</h3>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "💻 GitHub",
        github
    )

    st.link_button(
        "💼 LinkedIn",
        linkedin
    )

    st.link_button(
        "📧 Email",
        gmail
    )

    st.write("")
    st.write("")
    st.markdown("""
<div class="card">

<h2>Send a Message</h2>

</div>
""", unsafe_allow_html=True)
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    if st.button("Send"):
        st.success("Thank you! Your message has been recorded.")
        st.write("")
    with open("assets/PAVAN.pdf","rb") as pdf:
        st.download_button(

        "⬇ Download Resume",

        pdf,

        file_name="PAVAN.pdf"

    )
        st.write("")
        st.divider()
        st.markdown("""
<center>

<h3 style="color:#00abf0;">

Thank You For Visiting My Portfolio ❤️

</h3>

<p style="color:white;">

Designed & Developed by Sai Pavan

</p>

</center>
""", unsafe_allow_html=True)