# 🚀 AI Career Pro

## ▶️ How to Run the Project (Quick Start)

### Prerequisites
- Python 3.10 or higher
- Google Gemini API Key

### Installation & Execution

1. Clone the repository :

git clone https://github.com/sriram32134/ai-resume-portfolio-builder.git
cd ai-resume-portfolio-builder

2. Create and activate a virtual environment :

python -m venv venv

Windows:
.\venv\Scripts\activate

macOS / Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set the Gemini API Key

Windows (PowerShell):
setx GEMINI_API_KEY "your_api_key_here"

macOS / Linux:
export GEMINI_API_KEY="your_api_key_here"

5. Run the application

streamlit run app.py

The application will open automatically in your browser.

--------------------------------------------------

## 📌 How to Enter Details (Best Results)

### 1️⃣ Master Details

Email | Phone | Location  
Enter using pipe separator:
email@example.com | +91XXXXXXXXXX | City, Country

Target Role  
Be specific (e.g., Full-Stack Developer, Data Analyst, System Engineer)

Brief Experience  
Write 2–3 sentences describing your skills and focus areas

--------------------------------------------------

### 2️⃣ Education & Experience

Use the + Add button to add multiple entries.

Experience:
- Role / Title
- Company Name
- Leave description empty for AI-generated content

Education:
- Degree
- Institution
- Percentage / CGPA
- Year

--------------------------------------------------

### 3️⃣ Projects

- Enter Project Name (e.g., Fake News Detection System)
- Provide a one-line description
- AI expands it into professional resume-ready content

--------------------------------------------------

### ✅ Best Practices
- AI avoids markdown symbols for clean PDF rendering
- Use Download PDF for print-ready resumes
- Portfolio links must be valid public URLs

--------------------------------------------------

## 🎯 About AI Career Pro

AI Career Pro is an all-in-one AI-powered career toolkit designed to help students and professionals build high-impact job application materials.

Powered by Google Gemini AI, the application automatically generates:
- Professional resumes
- Tailored cover letters
- Premium portfolio websites

All using a single set of user details.

--------------------------------------------------

## ✨ Key Features

### 1️⃣ Master Details Integration
- Enter personal details once
- Reused across Resume, Cover Letter, and Portfolio
- Upload profile photo for modern templates

### 2️⃣ AI Resume Generator
- Dynamic sections for Experience, Education, and Projects
- AI-generated descriptions when fields are left empty
- Premium resume templates:
  Executive Elite
  Modern Centered
  Professional
  Classic
  Minimal
  Geometric Grid
- Export print-ready PDF resumes

### 3️⃣ AI Portfolio Builder
- Generates a complete portfolio website in seconds
- Modern themes:
  Glassmorphism
  Cyber Terminal
  Earthy Minimalist
- Automatically includes:
  Education
  Projects
  Skills
  Social Links

### 4️⃣ Cover Letter Pro
- Generates customized cover letters using:
  Company Name
  Job Title
- Uses your profile to create persuasive professional narratives
- Eliminates manual drafting

--------------------------------------------------

## 🛠️ Tech Stack

Frontend & UI: Streamlit  
AI Model: Google Gemini (google-genai SDK)  
PDF Generation: fpdf2  
Backend: Python  
Deployment: Streamlit Cloud  

--------------------------------------------------

## 📁 Project Structure

ai-resume-portfolio-builder/
│
├── app.py
├── sections/
│   ├── resume.py
│   ├── cover_letter.py
│   └── portfolio.py
│
├── utils/
│   ├── llm.py
│   ├── generate_pdf.py
│   ├── sanitize.py
│   └── portfolio_templates.py
│
├── templates/
│   ├── resume_.html
│   └── portfolio_.html
│
├── requirements.txt
├── .gitignore
└── README.md

--------------------------------------------------

## 🌟 Why AI Career Pro?
- One-click professional documents
- ATS-friendly resumes
- Clean PDF output
- Modern portfolio websites
- Ideal for students, freshers, and professionals

--------------------------------------------------

## 📜 License
This project is open-source and available under the MIT License.