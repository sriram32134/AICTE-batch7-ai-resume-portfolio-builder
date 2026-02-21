import streamlit as st
from sections import resume, cover_letter, portfolio

# ═══════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="AI Career Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); }
    [data-testid="stSidebar"] * { color: #f8fafc !important; }
    .main-header {
        background: linear-gradient(135deg, #0ea5e9, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .sub-header { color: #64748b; font-size: 1rem; margin-bottom: 24px; }
    /* Style for smaller dynamic buttons */
    .stButton>button {
        padding: 2px 10px !important;
        font-size: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🛠️ Career Suite")
    st.markdown("---")
    tool = st.radio(
        "Select Tool",
        ["📄 Resume Generator", "✉️ Cover Letter Pro", "🌐 Portfolio Builder"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("Powered by Gemini AI ✨")

st.markdown('<p class="main-header">AI Career Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your all-in-one AI-powered career toolkit</p>', unsafe_allow_html=True)

with st.expander("📝 Master Details — fill these once, use everywhere", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", value="Sri Ram", placeholder="John Doe")
        contact = st.text_input("Email | Phone | Location", value="jnanasriramubbisetti@gmail.com", placeholder="john@email.com | +91 ...")
        role = st.text_input("Target Role", value="system engineer", placeholder="e.g. Full-Stack Developer")
    with col2:
        skills = st.text_area("Skills (comma separated)", value="python,java,mern full stack", placeholder="Python, Java, React, SQL...")
        image = st.file_uploader("📸 Profile Photo (Required for Portfolio Only)", type=["jpg", "png", "jpeg"])

st.session_state["master"] = {
    "name": name, 
    "contact": contact, 
    "role": role, 
    "skills": skills,
    "image": image,
}

if tool == "📄 Resume Generator":
    resume.render()
elif tool == "✉️ Cover Letter Pro":
    cover_letter.render()
elif tool == "🌐 Portfolio Builder":
    portfolio.render()