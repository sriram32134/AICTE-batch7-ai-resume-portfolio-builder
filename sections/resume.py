import streamlit as st
from utils.llm import ai_text
from utils.generate_pdf import generate_resume_pdf, RESUME_TEMPLATES

def render():
    st.title("📄 AI Resume Generator")
    
    if "edu_count" not in st.session_state: st.session_state.edu_count = 1
    if "exp_count" not in st.session_state: st.session_state.exp_count = 1
    if "proj_count" not in st.session_state: st.session_state.proj_count = 1

    template = st.selectbox("Choose Resume Template", list(RESUME_TEMPLATES.keys()))
    master = st.session_state.get("master", {})
    target_role = master.get('role', 'Professional')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Summary & Experience")
        summary = st.text_area(
            "Professional Summary", 
            placeholder=f"Leave blank to auto-generate a summary for a {target_role} role..."
        )

        st.write("---")
        exp_c1, exp_c2 = st.columns([0.8, 0.2])
        exp_c1.write("**Experience Entries**")
        with exp_c2:
            btn_col1, btn_col2 = st.columns(2)
            if btn_col1.button("＋", key="add_exp"): 
                st.session_state.exp_count += 1
                st.rerun()
            if btn_col2.button("－", key="rem_exp") and st.session_state.exp_count > 1: 
                st.session_state.exp_count -= 1
                st.rerun()

        exp_entries = []
        for i in range(st.session_state.exp_count):
            with st.expander(f"Experience {i+1}", expanded=True):
                role = st.text_input(f"Role/Title {i+1}", key=f"exp_role_{i}")
                comp = st.text_input(f"Company & Dates {i+1}", key=f"exp_comp_{i}")
                desc = st.text_area(f"Description {i+1} (Leave blank for AI)", key=f"exp_desc_{i}")
                exp_entries.append({"role": role, "comp": comp, "desc": desc})

    with col2:
        st.subheader("Education & Projects")
        
        edu_c1, edu_c2 = st.columns([0.8, 0.2])
        edu_c1.write("**Education Entries**")
        with edu_c2:
            ebtn_col1, ebtn_col2 = st.columns(2)
            if ebtn_col1.button("＋", key="add_edu"): 
                st.session_state.edu_count += 1
                st.rerun()
            if ebtn_col2.button("－", key="rem_edu") and st.session_state.edu_count > 1: 
                st.session_state.edu_count -= 1
                st.rerun()

        edu_entries = []
        for i in range(st.session_state.edu_count):
            with st.expander(f"Education {i+1}", expanded=True):
                study = st.text_input(f"Study/Degree {i+1}", key=f"edu_study_{i}")
                college = st.text_input(f"College/University {i+1}", key=f"edu_coll_{i}")
                col_a, col_b = st.columns(2)
                perc = col_a.text_input(f"Percentage/CGPA {i+1}", key=f"edu_perc_{i}")
                year = col_b.text_input(f"Year {i+1}", key=f"edu_year_{i}")
                edu_entries.append(f"{study} - {college} ({perc}) - {year}")

        # Update Master State with latest Education for Portfolio/Cover Letter
        st.session_state["master"]["education_list"] = "\n".join(edu_entries)

        st.write("---")
        proj_c1, proj_c2 = st.columns([0.8, 0.2])
        proj_c1.write("**Project Entries**")
        with proj_c2:
            pbtn_col1, pbtn_col2 = st.columns(2)
            if pbtn_col1.button("＋", key="add_proj"): 
                st.session_state.proj_count += 1
                st.rerun()
            if pbtn_col2.button("－", key="rem_proj") and st.session_state.proj_count > 1: 
                st.session_state.proj_count -= 1
                st.rerun()

        proj_entries = []
        for i in range(st.session_state.proj_count):
            with st.expander(f"Project {i+1}", expanded=True):
                p_name = st.text_input(f"Project Name {i+1}", key=f"p_name_{i}")
                p_desc = st.text_area(f"Description {i+1} (Leave blank for AI)", key=f"p_desc_{i}")
                p_link = st.text_input(f"Link {i+1} (Optional)", key=f"p_link_{i}")
                proj_entries.append({"name": p_name, "desc": p_desc, "link": p_link})

    st.write("---")
    c3, c4 = st.columns(2)
    certs = c3.text_area("Certifications", placeholder="Cert Name - Provider")
    achieve = c4.text_area("Achievements", placeholder="Honors, Awards...")
    interests = st.text_input("Interests (Comma separated)")

    if st.button("🚀 Generate Professional Resume", type="primary", use_container_width=True):
        with st.spinner("Gemini is crafting your professional story..."):
            no_star_rule = " Do NOT use bolding or markdown stars (**)."
            summary_input = summary if summary.strip() else f"I am a {target_role} with skills in {master.get('skills', '')}."
            ai_summary = ai_text(f"Write a 2-line high-impact resume summary for a {target_role}. Input: {summary_input}" + no_star_rule)

            formatted_exp = ""
            for ent in exp_entries:
                if ent['role']:
                    desc_to_use = ent['desc']
                    if not desc_to_use.strip():
                        desc_to_use = ai_text(f"Generate 2 professional bullet points for the role: {ent['role']} at {ent['comp']}. Use plain text, no stars." + no_star_rule)
                    formatted_exp += f"{ent['role']} | {ent['comp']}\n{desc_to_use}\n\n"

            formatted_proj = ""
            for p in proj_entries:
                if p['name']:
                    ai_p_desc = ai_text(f"Given project name '{p['name']}' and description '{p['desc']}', provide a professional 3-line description. Use plain text only." + no_star_rule)
                    link_part = f"\nLink: {p['link']}" if p['link'].strip() else ""
                    formatted_proj += f"{p['name']}\n{ai_p_desc}{link_part}\n\n"

            data = {
                "name": master.get("name", "Your Name"),
                "contact": master.get("contact", ""),
                "role": target_role,
                "skills": master.get("skills", ""),
                "summary": ai_summary,
                "experience": formatted_exp,
                "projects": formatted_proj,
                "education": "\n".join(edu_entries),
                "certifications": certs,
                "achievements": achieve,
                "interests": interests,
                "image_bytes": None, 
            }

            pdf_bytes = generate_resume_pdf(data, template)
            st.success("✅ Resume Generated!")
            st.download_button("📥 Download Resume PDF", pdf_bytes, f"Resume_{template}.pdf", "application/pdf", use_container_width=True)