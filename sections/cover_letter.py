import streamlit as st
from utils.llm import ai_text
from utils.generate_pdf import generate_cover_letter_pdf

def render():
    st.title("✉️ Cover Letter Generator")
    
    # Initialize session state for Education counter if not present
    if "edu_count_cl" not in st.session_state: st.session_state.edu_count_cl = 1

    # ── Inputs ──
    col1, col2 = st.columns(2)
    with col1:
        company = st.text_input("Company Name", placeholder="Google, Amazon...")
        job_title = st.text_input("Job Title (if different from Target Role)", placeholder="Leave blank to use target role")
    with col2:
        tone = st.selectbox("Tone", ["Professional", "Enthusiastic", "Concise", "Creative"])
        word_limit = st.slider("Approximate Word Count", 150, 500, 300, step=50)

    # ── Dynamic Education Section (Same as Resume) ──
    st.write("---")
    edu_c1, edu_c2 = st.columns([0.8, 0.2])
    edu_c1.subheader("Education Details")
    with edu_c2:
        ebtn_col1, ebtn_col2 = st.columns(2)
        if ebtn_col1.button("＋", key="add_edu_cl"): 
            st.session_state.edu_count_cl += 1
            st.rerun()
        if ebtn_col2.button("－", key="rem_edu_cl") and st.session_state.edu_count_cl > 1: 
            st.session_state.edu_count_cl -= 1
            st.rerun()

    edu_entries = []
    for i in range(st.session_state.edu_count_cl):
        with st.expander(f"Education {i+1}", expanded=True):
            study = st.text_input(f"Study/Degree {i+1}", key=f"cl_edu_study_{i}")
            college = st.text_input(f"College/University {i+1}", key=f"cl_edu_coll_{i}")
            col_a, col_b = st.columns(2)
            perc = col_a.text_input(f"Percentage/CGPA {i+1}", key=f"cl_edu_perc_{i}")
            year = col_b.text_input(f"Year {i+1}", key=f"cl_edu_year_{i}")
            edu_entries.append(f"{study} from {college} ({perc}) - {year}")

    st.write("---")
    highlights = st.text_area("Key Highlights / Achievements to Mention", height=150)

    # ── Generate ──
    if st.button("✍️ Generate Cover Letter", type="primary", use_container_width=True):
        with st.spinner("Writing your cover letter..."):
            master = st.session_state.get("master", {})
            role = job_title if job_title else master.get("role", "the position")
            edu_context = "\n".join(edu_entries)

            prompt = (
                f"Write a {tone.lower()} cover letter (~{word_limit} words) for {role} at {company}.\n"
                f"Applicant: {master.get('name', 'the applicant')}\n"
                f"Education Background:\n{edu_context}\n"
                f"Skills: {master.get('skills', '')}\n"
                f"Key highlights: {highlights}\n"
                f"Do NOT include the header/address block – just the body paragraphs. No stars (**)."
            )

            body = ai_text(prompt)
            data = {
                "name": master.get("name", "Your Name"), 
                "contact": master.get("contact", ""), 
                "company": company, 
                "body": body
            }
            pdf_bytes = generate_cover_letter_pdf(data)

            st.success("✅ Cover letter generated!")
            with st.expander("📖 Preview", expanded=True):
                st.write(body)

            st.download_button(
                "📥 Download Cover Letter PDF",
                pdf_bytes,
                file_name=f"CoverLetter_{company.replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )