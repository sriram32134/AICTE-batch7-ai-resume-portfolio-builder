import tempfile
import os
from fpdf import FPDF
from utils.sanitize import sanitize_text
from datetime import date

# ═══════════════════════════════════════════════════════════════
#  IMAGE & UTILITY HELPERS
# ═══════════════════════════════════════════════════════════════

def _save_temp_image(image_bytes: bytes) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    tmp.write(image_bytes)
    tmp.close()
    return tmp.name

def _place_round_image(pdf: FPDF, image_bytes: bytes, x: float, y: float, size: float):
    img_path = _save_temp_image(image_bytes)
    try:
        with pdf.local_context():
            pdf.clip_ellipse(x, y, size, size)
            pdf.image(img_path, x, y, size, size)
        pdf.set_draw_color(180, 180, 180)
        pdf.set_line_width(0.3)
        pdf.ellipse(x, y, size, size, style="D")
    except Exception as e:
        print(f"Error placing image: {e}")
    finally:
        if os.path.exists(img_path):
            os.unlink(img_path)

# ═══════════════════════════════════════════════════════════════
#  RESUME PDF CLASSES
# ═══════════════════════════════════════════════════════════════

class ResumeClassicPDF(FPDF):
    def build(self, data: dict) -> bytes:
        self.add_page()
        self.set_auto_page_break(auto=True, margin=10) 
        self.set_y(15)
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 12, sanitize_text(data["name"]).upper(), ln=True, align="C")
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 6, sanitize_text(data.get("role", "")), ln=True, align="C")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, sanitize_text(data["contact"]), ln=True, align="C")
        self.ln(2); self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y()); self.ln(4)
        self.set_text_color(0, 0, 0)

        sections = [
            ("PROFESSIONAL SUMMARY", data.get("summary", "")),
            ("SKILLS", data.get("skills", "")),
            ("EXPERIENCE", data.get("experience", "")),
            ("PROJECTS", data.get("projects", "")),
            ("EDUCATION", data.get("education", "")),
            ("CERTIFICATIONS", data.get("certifications", "")),
            ("ACHIEVEMENTS", data.get("achievements", "")),
            ("INTEREST AREA", data.get("interests", "")),
        ]
        for title, content in sections:
            if content and content.strip():
                self.set_font("Helvetica", "B", 11); self.set_fill_color(245, 245, 245)
                self.cell(0, 7, f"  {title}", ln=True, fill=True); self.ln(1)
                self.set_font("Helvetica", "", 10)
                self.multi_cell(0, 4, sanitize_text(content)); self.ln(2)
        return bytes(self.output(dest="S"))

class ResumeModernPDF(FPDF):
    SIDEBAR_W = 65
    ACCENT = (14, 165, 233)
    def build(self, data: dict) -> bytes:
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_fill_color(*self.ACCENT); self.rect(0, 0, self.SIDEBAR_W, 297, "F")
        self.set_xy(5, 20); self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 16); self.multi_cell(self.SIDEBAR_W - 10, 7, sanitize_text(data["name"]))
        self.set_font("Helvetica", "", 9); self.multi_cell(self.SIDEBAR_W - 10, 5, sanitize_text(data.get("role", "")))
        self.ln(10)
        sidebar = [("CONTACT", data.get("contact", "")), ("SKILLS", data.get("skills", "")), ("EDUCATION", data.get("education", "")), ("INTERESTS", data.get("interests", ""))]
        for title, content in sidebar:
            if content and content.strip():
                self.set_x(5); self.set_font("Helvetica", "B", 10); self.cell(self.SIDEBAR_W - 10, 7, title, ln=True)
                self.set_x(5); self.set_font("Helvetica", "", 8); self.multi_cell(self.SIDEBAR_W - 10, 4, sanitize_text(content)); self.ln(5)
        main_x = self.SIDEBAR_W + 10; self.set_xy(main_x, 20); self.set_text_color(30, 30, 30)
        main = [("SUMMARY", data.get("summary", "")), ("EXPERIENCE", data.get("experience", "")), ("PROJECTS", data.get("projects", "")), ("CERTIFICATIONS", data.get("certifications", "")), ("ACHIEVEMENTS", data.get("achievements", ""))]
        for title, content in main:
            if content and content.strip():
                self.set_x(main_x); self.set_font("Helvetica", "B", 12); self.set_text_color(*self.ACCENT); self.cell(0, 8, title, ln=True)
                self.set_x(main_x); self.set_font("Helvetica", "", 10); self.set_text_color(50, 50, 50); self.multi_cell(0, 5, sanitize_text(content)); self.ln(6)
        return bytes(self.output(dest="S"))

class ResumeProfessionalPDF(FPDF):
    def build(self, data: dict) -> bytes:
        self.add_page(); self.set_auto_page_break(auto=True, margin=15)
        self.set_fill_color(34, 40, 49); self.rect(0, 0, 210, 45, "F")
        self.set_xy(15, 12); self.set_text_color(255, 255, 255); self.set_font("Times", "B", 26); self.cell(0, 10, sanitize_text(data["name"]).upper(), ln=True)
        self.set_x(15); self.set_font("Helvetica", "", 11); self.cell(0, 6, sanitize_text(data.get("role", "")), ln=True)
        self.set_text_color(0, 0, 0); self.set_y(50); self.set_font("Helvetica", "", 9); self.cell(0, 6, sanitize_text(data.get("contact", "")), ln=True, align="C"); self.ln(10)
        sections = [("SUMMARY", data.get("summary", "")), ("EXPERIENCE", data.get("experience", "")), ("PROJECTS", data.get("projects", "")), ("SKILLS", data.get("skills", "")), ("EDUCATION", data.get("education", "")), ("CERTIFICATIONS", data.get("certifications", "")), ("ACHIEVEMENTS", data.get("achievements", "")), ("INTERESTS", data.get("interests", ""))]
        for title, content in sections:
            if content and content.strip():
                self.set_font("Times", "B", 13); self.set_text_color(34, 40, 49); self.cell(0, 8, title, ln=True)
                self.set_draw_color(34, 40, 49); self.line(self.get_x(), self.get_y(), self.get_x() + 80, self.get_y()); self.ln(2)
                self.set_font("Helvetica", "", 10); self.set_text_color(50, 50, 50); self.multi_cell(0, 5, sanitize_text(content)); self.ln(6)
        return bytes(self.output(dest="S"))

# ── PREMIUM TEMPLATES (FIXED) ──

class ResumeExecutiveElitePDF(FPDF):
    SIDEBAR_W = 70
    PRIMARY_COLOR = (44, 62, 80)
    def build(self, data: dict) -> bytes:
        self.add_page(); self.set_auto_page_break(auto=True, margin=15)
        self.set_fill_color(*self.PRIMARY_COLOR); self.rect(0, 0, self.SIDEBAR_W, 297, "F")
        self.set_text_color(255, 255, 255); self.set_xy(10, 20); self.set_font("Helvetica", "B", 18); self.multi_cell(self.SIDEBAR_W - 20, 10, sanitize_text(data["name"]).upper())
        self.ln(5); self.set_font("Helvetica", "B", 10); self.set_text_color(189, 195, 199); self.set_x(10); self.cell(0, 5, sanitize_text(data.get("role", "")).upper(), ln=True)
        
        sidebar = [("CONTACT", data.get("contact", "")), ("TECHNICAL SKILLS", data.get("skills", "")), ("EDUCATION", data.get("education", "")), ("INTERESTS", data.get("interests", ""))]
        for title, content in sidebar:
            if content and content.strip():
                self.ln(10); self.set_x(10); self.set_font("Helvetica", "B", 10); self.set_text_color(255, 255, 255); self.cell(0, 6, title, ln=True); self.set_draw_color(255, 255, 255); self.line(10, self.get_y(), self.SIDEBAR_W - 10, self.get_y()); self.ln(2); self.set_x(10); self.set_font("Helvetica", "", 9); self.multi_cell(self.SIDEBAR_W - 20, 4, sanitize_text(content))

        self.set_text_color(40, 40, 40); main_x = self.SIDEBAR_W + 10; self.set_xy(main_x, 20)
        main = [("EXECUTIVE SUMMARY", data.get("summary", "")), ("PROFESSIONAL EXPERIENCE", data.get("experience", "")), ("NOTABLE PROJECTS", data.get("projects", "")), ("CERTIFICATIONS", data.get("certifications", "")), ("ACHIEVEMENTS", data.get("achievements", ""))]
        for title, content in main:
            if content and content.strip():
                self.set_x(main_x); self.set_font("Helvetica", "B", 12); self.set_text_color(*self.PRIMARY_COLOR); self.cell(0, 8, title, ln=True); self.ln(1); self.set_x(main_x); self.set_font("Helvetica", "", 10); self.set_text_color(60, 60, 60); self.multi_cell(0, 5, sanitize_text(content)); self.ln(4)
        return bytes(self.output(dest="S"))

class ResumeModernCenteredPDF(FPDF):
    ACCENT = (52, 73, 94)
    def build(self, data: dict) -> bytes:
        self.add_page(); self.set_auto_page_break(auto=True, margin=20)
        self.set_y(20); self.set_font("Helvetica", "B", 26); self.set_text_color(*self.ACCENT); self.cell(0, 15, sanitize_text(data["name"]).upper(), ln=True, align="C")
        self.set_font("Helvetica", "", 12); self.set_text_color(100, 100, 100); self.cell(0, 6, sanitize_text(data.get("role", "")).upper(), ln=True, align="C")
        self.set_font("Helvetica", "", 9); self.cell(0, 5, sanitize_text(data.get("contact", "")), ln=True, align="C"); self.ln(5)
        self.set_draw_color(200, 200, 200); self.line(40, self.get_y(), 170, self.get_y()); self.ln(8)
        
        sections = [("PROFILE SUMMARY", data.get("summary", "")), ("CORE EXPERTISE", data.get("skills", "")), ("WORK HISTORY", data.get("experience", "")), ("KEY PROJECTS", data.get("projects", "")), ("CERTIFICATIONS", data.get("certifications", "")), ("ACADEMIC BACKGROUND", data.get("education", "")), ("ACHIEVEMENTS", data.get("achievements", "")), ("INTERESTS", data.get("interests", ""))]
        for title, content in sections:
            if content and content.strip():
                self.set_font("Helvetica", "B", 11); self.set_text_color(*self.ACCENT); self.cell(0, 8, title, ln=True)
                self.set_font("Helvetica", "", 10); self.set_text_color(50, 50, 50); self.multi_cell(0, 5, sanitize_text(content)); self.ln(5)
        return bytes(self.output(dest="S"))

class ResumeGeometricPDF(FPDF):
    HEADER_BG = (236, 240, 241)
    ACCENT = (231, 76, 60)
    def build(self, data: dict) -> bytes:
        self.add_page(); self.set_auto_page_break(auto=True, margin=15)
        self.set_fill_color(*self.HEADER_BG); self.rect(0, 0, 210, 50, "F")
        self.set_y(15); self.set_font("Helvetica", "B", 24); self.set_text_color(44, 62, 80); self.cell(0, 12, f"  {sanitize_text(data['name'])}", ln=True)
        self.set_font("Helvetica", "B", 12); self.set_text_color(*self.ACCENT); self.cell(0, 8, f"   {sanitize_text(data.get('role', '')).upper()}", ln=True)
        self.set_y(35); self.set_font("Helvetica", "", 9); self.set_text_color(80, 80, 80); self.cell(0, 6, f"   {sanitize_text(data.get('contact', ''))}", ln=True)
        self.set_y(60); self.set_draw_color(*self.ACCENT); self.set_line_width(0.8); self.line(18, 60, 18, 280)
        
        sections = [("SUMMARY", data.get("summary", "")), ("SKILLS", data.get("skills", "")), ("EXPERIENCE", data.get("experience", "")), ("PROJECTS", data.get("projects", "")), ("CERTIFICATIONS", data.get("certifications", "")), ("EDUCATION", data.get("education", "")), ("ACHIEVEMENTS", data.get("achievements", "")), ("INTERESTS", data.get("interests", ""))]
        for title, content in sections:
            if content and content.strip():
                self.set_x(25); self.set_font("Helvetica", "B", 11); self.set_text_color(44, 62, 80); self.cell(0, 8, title, ln=True); self.set_x(25); self.set_font("Helvetica", "", 10); self.set_text_color(60, 60, 60); self.multi_cell(0, 4.5, sanitize_text(content)); self.ln(4)
        return bytes(self.output(dest="S"))

# ═══════════════════════════════════════════════════════════════
#  FACTORY HELPERS
# ═══════════════════════════════════════════════════════════════

class CoverLetterPDF(FPDF):
    def build(self, data: dict) -> bytes:
        self.add_page(); self.set_font("Helvetica", "B", 14); self.cell(0, 8, sanitize_text(data["name"]), ln=True)
        self.set_font("Helvetica", "", 10); self.cell(0, 5, sanitize_text(data.get("contact", "")), ln=True); self.ln(10)
        self.cell(0, 5, date.today().strftime("%B %d, %Y"), ln=True); self.ln(10)
        if data.get("company"):
            self.set_font("Helvetica", "B", 11); self.cell(0, 6, f"To: Hiring Manager, {sanitize_text(data['company'])}", ln=True); self.ln(5)
        self.set_font("Helvetica", "", 11); self.multi_cell(0, 6, sanitize_text(data.get("body", ""))); self.ln(10)
        self.cell(0, 6, "Sincerely,", ln=True); self.cell(0, 6, sanitize_text(data["name"]), ln=True)
        return bytes(self.output(dest="S"))

RESUME_TEMPLATES = {
    "Classic": ResumeClassicPDF,
    "Modern": ResumeModernPDF,
    "Professional": ResumeProfessionalPDF,
    "Executive Elite": ResumeExecutiveElitePDF,
    "Modern Centered": ResumeModernCenteredPDF,
    "Geometric Grid": ResumeGeometricPDF,
}

def generate_resume_pdf(data: dict, template: str = "Classic") -> bytes:
    pdf_class = RESUME_TEMPLATES.get(template, ResumeClassicPDF)
    pdf = pdf_class()
    return pdf.build(data)

def generate_cover_letter_pdf(data: dict) -> bytes:
    pdf = CoverLetterPDF()
    return pdf.build(data)