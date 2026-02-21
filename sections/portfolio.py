import streamlit as st
import base64
from utils.llm import ai_text
from utils.portfolio_templates import DARK_TEMPLATE

def render():
    st.title("🌐 AI Portfolio Website Builder")
    master = st.session_state.get("master", {})

    # Initialize Education counter
    if "edu_count_pf" not in st.session_state: st.session_state.edu_count_pf = 1

    # ── Input Sections ──
    with st.expander("👤 About & Professional Link", expanded=True):
        about_me = st.text_area("Bio / Describe yourself", placeholder="A passionate developer...")
        resume_url = st.text_input("Resume Link (Google Drive / Dropbox)", placeholder="https://link-to-your-resume.pdf")

    # ── Dynamic Education Section (Same as Resume) ──
    with st.expander("🎓 Education Details", expanded=True):
        edu_c1, edu_c2 = st.columns([0.8, 0.2])
        edu_c1.write("**Add your educational background**")
        with edu_c2:
            ebtn_col1, ebtn_col2 = st.columns(2)
            if ebtn_col1.button("＋", key="add_edu_pf"): 
                st.session_state.edu_count_pf += 1
                st.rerun()
            if ebtn_col2.button("－", key="rem_edu_pf") and st.session_state.edu_count_pf > 1: 
                st.session_state.edu_count_pf -= 1
                st.rerun()

        edu_entries = []
        for i in range(st.session_state.edu_count_pf):
            st.markdown(f"**Entry {i+1}**")
            study = st.text_input(f"Study/Degree {i+1}", key=f"pf_edu_study_{i}")
            college = st.text_input(f"College/University {i+1}", key=f"pf_edu_coll_{i}")
            col_a, col_b = st.columns(2)
            perc = col_a.text_input(f"Percentage/CGPA {i+1}", key=f"pf_edu_perc_{i}")
            year = col_b.text_input(f"Year {i+1}", key=f"pf_edu_year_{i}")
            edu_entries.append(f"{study} from {college} ({perc}) - {year}")

    with st.expander("💼 Career & Socials"):
        experience = st.text_area("Experience (Additional details)", placeholder="Work History details...")
        projects = st.text_area("Projects (Additional details)", placeholder="Project details and links...")
        social_links = st.text_area("Social Links (Label: URL)", placeholder="GitHub: https://github.com/you\nLinkedIn: https://linkedin.com/in/you")

    with st.expander("🏆 Achievements & Activities"):
        achievements = st.text_area("Key Achievements", placeholder="Awards, Certifications, etc.")
        activities = st.text_area("Extra-Curricular Activities", placeholder="Clubs, Volunteering, Sports...")

    if st.button("✨ Generate Premium Portfolio", type="primary", use_container_width=True):
        with st.spinner("Building your digital presence..."):
            web_bio = ai_text(f"Create a 3-sentence captivating bio for a portfolio website. Input: {about_me}")
            image = master.get("image")
            img_tag = '<div class="avatar-placeholder">👤</div>'
            if image:
                img_str = base64.b64encode(image.getvalue()).decode()
                img_tag = f'<img src="data:image/png;base64,{img_str}" class="avatar-img" alt="{master.get("name")}">'

            social_html = ""
            if social_links:
                for line in social_links.split("\n"):
                    if ":" in line:
                        label, url = line.split(":", 1)
                        social_html += f'<a href="{url.strip()}" class="social-link" target="_blank">{label.strip()}</a>'

            resume_link_html = f'<a href="{resume_url}" class="resume-btn" target="_blank">View Resume</a>' if resume_url else ""

            data = {
                "name": master.get("name", "Your Name"),
                "first_name": master.get("name", "ME").split()[0].upper(),
                "role": master.get("role", "Professional"),
                "bio": web_bio,
                "skills": "".join([f'<span class="skill-tag">{s.strip()}</span>' for s in master.get("skills", "").split(",")]),
                "experience": experience.replace("\n", "<br>"),
                "projects": projects.replace("\n", "<br>"),
                "education": "<br>".join(edu_entries),
                "achievements": achievements.replace("\n", "<br>"),
                "activities": activities.replace("\n", "<br>"),
                "resume_link_html": resume_link_html,
                "contact": master.get("contact", ""),
                "social_html": social_html,
                "img_tag": img_tag,
                "year": "2026",
            }

            final_html = DARK_TEMPLATE
            for key, value in data.items():
                final_html = final_html.replace("{{" + key + "}}", str(value))

            st.success("✅ Portfolio successfully generated!")
            st.download_button(
                label="📥 Download Portfolio HTML",
                data=final_html,
                file_name=f"{master.get('name', 'Portfolio').replace(' ', '_')}.html",
                mime="text/html",
                use_container_width=True
            )