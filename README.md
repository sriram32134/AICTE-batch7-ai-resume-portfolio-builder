# 🚀 AI Career Pro

**AI Career Pro** is an all-in-one, AI-powered career toolkit designed to help students and professionals create high-impact job application materials. Powered by **Google Gemini AI**, the application automatically generates professional resumes, tailored cover letters, and premium portfolio websites using a single set of user details.

This project focuses on automation, personalization, and clean document design to improve job and internship opportunities.

---

## ✨ Key Features

### 1️⃣ Master Details Integration
- Enter personal information, contact details, skills, and target role **once**
- Reused across Resume, Cover Letter, and Portfolio
- Upload a profile photo for modern resume templates and portfolio websites

---

### 2️⃣ AI Resume Generator
- **Dynamic sections**: Add unlimited Experience, Education, and Project entries
- **AI-powered descriptions**:
  - Leave descriptions empty and let AI generate professional bullet points
- **Premium resume templates**:
  - Executive Elite  
  - Modern Centered  
  - Professional  
  - Classic  
  - Minimal  
  - Geometric Grid
- Export **print-ready PDF resumes**

---

### 3️⃣ AI Portfolio Builder
- Generate a complete personal portfolio website in seconds
- Multiple modern design themes:
  - Glassmorphism
  - Cyber Terminal
  - Earthy Minimalist
- Automatically includes:
  - Education
  - Projects
  - Skills
  - Social links

---

### 4️⃣ Cover Letter Pro
- Generates customized cover letters based on:
  - Company name
  - Job title
- Uses your background and skills to create a persuasive, professional narrative
- Eliminates manual drafting

---

## 🛠️ Tech Stack

- **Frontend & UI**: Streamlit  
- **AI Model**: Google Gemini (google-genai SDK)  
- **PDF Generation**: fpdf2  
- **Backend**: Python  
- **Deployment**: Streamlit Cloud  

---

## 📁 Project Structure
ai-resume-portfolio-builder/
│
├── app.py # Main Streamlit app
├── sections/ # Feature modules
│ ├── resume.py
│ ├── cover_letter.py
│ └── portfolio.py
│
├── utils/ # Core logic
│ ├── llm.py # Gemini AI integration
│ ├── generate_pdf.py # PDF generation
│ ├── sanitize.py
│ └── portfolio_templates.py
│
├── templates/ # HTML/CSS templates
│ ├── resume_.html
│ └── portfolio_.html
│
├── requirements.txt
├── .gitignore
└── README.md

---

## 🚀 Getting Started

### Prerequisites
- Python **3.10 or higher**
- Google **Gemini API Key**

---

### 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/sriram32134/ai-resume-portfolio-builder.git
cd ai-resume-portfolio-builder

Create and activate virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Set environment variable
GEMINI_API_KEY=your_api_key_here

Run the application
streamlit run app.py

How to Enter Details (Best Results)

1️⃣ Master Details

Email | Phone | Location
Enter separated by pipes:
email@example.com | +91XXXXXXXXXX | City, Country

Target Role
Be specific (e.g., Full-Stack Developer, Data Analyst)

Brief Experience
2–3 sentences describing focus areas and strengths

2️⃣ Education & Experience

Use + button to add entries
Experience:
Fill Role & Company
Leave description empty for AI-generated content

Education:
Degree
Institution
Percentage / CGPA
Year

3️⃣ Projects
Enter project name (e.g., Fake News Detection System)
Provide a one-line description
AI expands it into professional resume-ready content

Best Practices
AI avoids markdown stars to ensure clean PDF rendering
Use Download PDF for print-ready resumes
Portfolio links format: