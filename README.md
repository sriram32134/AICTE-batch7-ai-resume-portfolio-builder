🚀 AI Career Pro

AI-Powered Resume, Cover Letter & Portfolio Builder

AI Career Pro is an all-in-one career toolkit that uses Google Gemini AI to automatically generate professional resumes, customized cover letters, and modern portfolio websites from a single set of user details.

The goal of this project is to reduce manual effort, improve personalization, and deliver clean, job-ready documents for students and professionals.

🏁 How to Run the Application

Follow these steps to set up and run AI Career Pro locally.

✅ Prerequisites

Python 3.10 or higher

Google Gemini API Key

Git (optional, but recommended)

✅ Installation & Setup

Clone the Repository:
git clone https://github.com/sriram32134/ai-resume-portfolio-builder.git
cd ai-resume-portfolio-builder

Create and Activate Virtual Environment:
python -m venv venv
  Windows:
  .\venv\Scripts\activate
  macOS / Linux:
  source venv/bin/activate

Install Dependencies:
  pip install -r requirements.txt

Set Gemini API Key:
  setx GEMINI_API_KEY "your_api_key_here"

Run the Application:
  streamlit run app.py

📌 About the Application

AI Career Pro allows users to enter their details once and reuse them across:

AI-generated resumes

Customized cover letters

Fully responsive portfolio websites

This ensures consistency, speed, and professional quality.

✨ Key Features
1️⃣ Master Details (Single Source of Truth)

Enter personal details, skills, and career goals one time

Automatically reused across:
  Resume
  Cover Letter
  Portfolio

Upload a profile photo for:

Modern resume templates
Portfolio websites

2️⃣ AI Resume Generator
🔹 Dynamic Sections

  Add unlimited:

  Experience
  Education
  Projects

🔹 AI-Powered Descriptions
  Leave description fields empty
  Gemini AI generates professional, ATS-friendly bullet points

🔹 Premium Resume Templates

  Executive Elite
  Modern Centered
  Professional
  Classic
  Minimal

  Geometric Grid

🔹 Export Options

Print-ready PDF resumes
Clean formatting (no markdown symbols)


3️⃣ AI Portfolio Builder

Generates a complete personal portfolio website in seconds

Multiple modern design themes:

Glassmorphism

Automatically Includes

  About section
  Education
  Projects
  Skills

Social & portfolio links

4️⃣ Cover Letter Pro

Generates custom cover letters based on:

Company name

Job title

Uses your:
  Experience
  Skills
  Target role

Eliminates repetitive manual drafting

🛠️ Tech Stack

Frontend / UI: Streamlit
AI Model: Google Gemini (google-genai SDK)
Backend: Python
PDF Generation: fpdf2
Deployment: Streamlit Cloud

Cloud

📁 Project Structure

ai-resume-portfolio-builder/
│
├── app.py                 # Main Streamlit application
│
├── sections/              # Feature modules
│   ├── resume.py
│   ├── cover_letter.py
│   └── portfolio.py
│
├── utils/                 # Core logic
│   ├── llm.py             # Gemini AI integration
│   ├── generate_pdf.py    # PDF generation logic
│   ├── sanitize.py
│   └── portfolio_templates.py
│
├── templates/             # HTML/CSS templates
│   ├── resume_.html
│   └── portfolio_.html
│
├── requirements.txt
├── .gitignore
└── README.md


