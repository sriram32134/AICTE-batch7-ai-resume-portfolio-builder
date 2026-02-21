# utils/portfolio_templates.py

DARK_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{name}} | Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        body { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; scroll-behavior: smooth; }
        .glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 24px; }
        .skill-tag { background: rgba(14, 165, 233, 0.1); color: #38bdf8; padding: 6px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 600; border: 1px solid rgba(14, 165, 233, 0.2); }
        .avatar-img { width: 220px; height: 220px; border-radius: 50%; border: 4px solid #38bdf8; object-fit: cover; box-shadow: 0 0 30px rgba(56, 189, 248, 0.3); margin: 0 auto; display: block; }
        .avatar-placeholder { width: 220px; height: 220px; background: linear-gradient(135deg, #1e293b, #0f172a); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 5rem; margin: 0 auto; border: 4px solid #38bdf8; }
        .social-link { color: #38bdf8; text-decoration: none; font-weight: 600; border: 1px solid rgba(56, 189, 248, 0.3); padding: 8px 20px; border-radius: 12px; transition: 0.4s; display: inline-block; background: rgba(56, 189, 248, 0.05); }
        .social-link:hover { background: #38bdf8; color: #0f172a; transform: translateY(-3px); }
        .resume-btn { background: linear-gradient(135deg, #0ea5e9, #6366f1); color: white; padding: 12px 30px; border-radius: 12px; font-weight: 800; text-decoration: none; display: inline-block; transition: 0.4s; }
        .resume-btn:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4); }
    </style>
</head>
<body>
    <nav class="fixed top-0 w-full z-50 glass px-8 py-4 flex justify-between items-center" style="border-radius:0; border-top:0; border-left:0; border-right:0;">
        <span class="text-xl font-extrabold tracking-tighter text-sky-400">{{first_name}}</span>
        <div class="space-x-6 text-sm font-medium">
            <a href="#about" class="hover:text-sky-400 transition">About</a>
            <a href="#work" class="hover:text-sky-400 transition">Work</a>
            <a href="#details" class="hover:text-sky-400 transition">Details</a>
            <a href="#contact" class="hover:text-sky-400 transition">Contact</a>
        </div>
    </nav>

    <header class="pt-48 pb-20 text-center px-4">
        {{img_tag}}
        <h1 class="text-6xl md:text-8xl font-extrabold mt-8 mb-4 bg-gradient-to-r from-sky-400 via-indigo-400 to-purple-400 bg-clip-text text-transparent">{{name}}</h1>
        <p class="text-2xl text-sky-400 font-mono tracking-widest uppercase">{{role}}</p>
        <div class="mt-10">{{resume_link_html}}</div>
    </header>

    <main class="max-w-6xl mx-auto px-6 space-y-12 pb-20">
        <section id="about" class="glass p-10">
            <h2 class="text-3xl font-bold mb-6 text-sky-400 flex items-center"><i class="fas fa-user-circle mr-3"></i> About Me</h2>
            <p class="text-slate-300 leading-relaxed text-xl">{{bio}}</p>
            <div class="mt-8">
                <h4 class="text-sm font-bold uppercase tracking-widest text-slate-500 mb-4">Technical Stack</h4>
                <div class="flex flex-wrap gap-3">{{skills}}</div>
            </div>
        </section>

        <section id="work" class="grid md:grid-cols-2 gap-8">
            <div class="glass p-10 border border-transparent hover:border-sky-500/30 transition-all duration-500">
                <h3 class="text-2xl font-bold mb-6 text-sky-400"><i class="fas fa-briefcase mr-3"></i> Professional Experience</h3>
                <div class="text-slate-300 text-lg leading-relaxed whitespace-pre-line">{{experience}}</div>
            </div>
            <div class="glass p-10 border border-transparent hover:border-sky-500/30 transition-all duration-500">
                <h3 class="text-2xl font-bold mb-6 text-sky-400"><i class="fas fa-project-diagram mr-3"></i> Key Projects</h3>
                <div class="text-slate-300 text-lg leading-relaxed whitespace-pre-line">{{projects}}</div>
            </div>
        </section>

        <section id="details" class="grid md:grid-cols-3 gap-8">
            <div class="glass p-8">
                <h3 class="text-xl font-bold mb-4 text-indigo-400"><i class="fas fa-graduation-cap mr-2"></i> Education</h3>
                <div class="text-slate-400 text-sm whitespace-pre-line">{{education}}</div>
            </div>
            <div class="glass p-8">
                <h3 class="text-xl font-bold mb-4 text-emerald-400"><i class="fas fa-trophy mr-2"></i> Achievements</h3>
                <div class="text-slate-400 text-sm whitespace-pre-line">{{achievements}}</div>
            </div>
            <div class="glass p-8">
                <h3 class="text-xl font-bold mb-4 text-purple-400"><i class="fas fa-running mr-2"></i> Activities</h3>
                <div class="text-slate-400 text-sm whitespace-pre-line">{{activities}}</div>
            </div>
        </section>
    </main>

    <footer id="contact" class="py-20 text-center glass rounded-none border-t border-slate-800">
        <h2 class="text-4xl font-bold mb-8 bg-gradient-to-r from-sky-400 to-indigo-400 bg-clip-text text-transparent">Start a Conversation</h2>
        <p class="text-slate-400 text-lg mb-10">{{contact}}</p>
        <div class="flex justify-center flex-wrap gap-6">{{social_html}}</div>
        <p class="mt-16 text-xs text-slate-600 uppercase tracking-widest">Designed with AI &copy; {{year}} {{name}}</p>
    </footer>
</body>
</html>
"""

LIGHT_TEMPLATE = DARK_TEMPLATE # Logic simplified for primary dark theme updates