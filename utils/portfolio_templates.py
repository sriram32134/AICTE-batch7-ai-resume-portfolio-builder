DARK_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{{name}} | Portfolio</title>

<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');

body {
  font-family: 'Inter', sans-serif;
  background: radial-gradient(circle at top, #0f172a, #020617);
  color: #e5e7eb;
}

.glass {
  background: rgba(255,255,255,0.04);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
}

.section-title {
  font-size: 1.9rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
}

.skill-tag {
  background: rgba(56,189,248,0.15);
  border: 1px solid rgba(56,189,248,0.25);
  color: #7dd3fc;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
}

.avatar-img {
  width: 260px;
  height: 260px;
  border-radius: 50%;
  border: 4px solid #38bdf8;
  object-fit: cover;
  box-shadow: 0 0 50px rgba(56,189,248,0.4);
}

.avatar-placeholder {
  width: 260px;
  height: 260px;
  border-radius: 50%;
  background: linear-gradient(135deg,#0ea5e9,#6366f1);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:5rem;
}

.social-link {
  padding: 10px 22px;
  border-radius: 14px;
  border: 1px solid rgba(56,189,248,0.4);
  color: #38bdf8;
  font-weight: 600;
  transition: 0.3s;
}

.social-link:hover {
  background: #38bdf8;
  color: #020617;
  transform: translateY(-3px);
}

.resume-btn {
  background: linear-gradient(135deg,#38bdf8,#6366f1);
  padding: 14px 34px;
  border-radius: 16px;
  font-weight: 800;
  color: white;
  transition: 0.3s;
}

.resume-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 15px 40px rgba(99,102,241,0.4);
}
</style>
</head>

<body>

<!-- NAV -->
<nav class="fixed top-0 w-full z-50 glass px-10 py-4 flex justify-between items-center rounded-none">
  <span class="text-xl font-extrabold tracking-tight text-sky-400">{{first_name}}</span>
  <div class="space-x-6 text-sm font-medium">
    <a href="#about" class="hover:text-sky-400">About</a>
    <a href="#work" class="hover:text-sky-400">Work</a>
    <a href="#details" class="hover:text-sky-400">Details</a>
    <a href="#contact" class="hover:text-sky-400">Contact</a>
  </div>
</nav>

<!-- HERO -->
<section class="pt-44 pb-28 max-w-7xl mx-auto px-6 grid md:grid-cols-2 gap-16 items-center">
  <div>
    <h1 class="text-5xl md:text-7xl font-black leading-tight bg-gradient-to-r from-sky-400 to-indigo-400 bg-clip-text text-transparent">
      {{name}}
    </h1>
    <p class="mt-4 text-xl text-sky-400 uppercase tracking-widest font-mono">{{role}}</p>
    <p class="mt-8 text-slate-300 text-lg leading-relaxed">{{bio}}</p>
    <div class="mt-10 flex flex-wrap gap-4">
      {{resume_link_html}}
    </div>
  </div>
  <div class="flex justify-center">
    {{img_tag}}
  </div>
</section>

<!-- ABOUT -->
<section id="about" class="max-w-6xl mx-auto px-6 mb-20">
  <div class="glass p-12">
    <h2 class="section-title text-sky-400"><i class="fa-solid fa-user mr-3"></i>About Me</h2>
    <p class="text-lg leading-relaxed text-slate-300">{{bio}}</p>
    <div class="mt-8 flex flex-wrap gap-3">{{skills}}</div>
  </div>
</section>

<!-- WORK -->
<section id="work" class="max-w-6xl mx-auto px-6 mb-20 grid md:grid-cols-2 gap-10">
  <div class="glass p-10">
    <h3 class="section-title text-sky-400"><i class="fa-solid fa-briefcase mr-2"></i>Experience</h3>
    <div class="text-slate-300 whitespace-pre-line">{{experience}}</div>
  </div>
  <div class="glass p-10">
    <h3 class="section-title text-sky-400"><i class="fa-solid fa-diagram-project mr-2"></i>Projects</h3>
    <div class="text-slate-300 whitespace-pre-line">{{projects}}</div>
  </div>
</section>

<!-- DETAILS -->
<section id="details" class="max-w-6xl mx-auto px-6 mb-24 grid md:grid-cols-3 gap-8">
  <div class="glass p-8">
    <h3 class="text-xl font-bold text-indigo-400 mb-4"><i class="fa-solid fa-graduation-cap mr-2"></i>Education</h3>
    <div class="text-slate-400 whitespace-pre-line">{{education}}</div>
  </div>
  <div class="glass p-8">
    <h3 class="text-xl font-bold text-emerald-400 mb-4"><i class="fa-solid fa-trophy mr-2"></i>Achievements</h3>
    <div class="text-slate-400 whitespace-pre-line">{{achievements}}</div>
  </div>
  <div class="glass p-8">
    <h3 class="text-xl font-bold text-purple-400 mb-4"><i class="fa-solid fa-person-running mr-2"></i>Activities</h3>
    <div class="text-slate-400 whitespace-pre-line">{{activities}}</div>
  </div>
</section>

<!-- FOOTER -->
<footer id="contact" class="glass rounded-none border-t border-slate-800 py-20 text-center">
  <h2 class="text-4xl font-black mb-6 bg-gradient-to-r from-sky-400 to-indigo-400 bg-clip-text text-transparent">
    Let’s Build Something Amazing
  </h2>
  <p class="text-slate-400 text-lg mb-10">{{contact}}</p>
  <div class="flex justify-center flex-wrap gap-6">{{social_html}}</div>
  <p class="mt-16 text-xs tracking-widest uppercase text-slate-600">
    © {{year}} {{name}} • Crafted with AI
  </p>
</footer>

</body>
</html>
"""