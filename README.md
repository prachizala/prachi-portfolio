# Prachi Zala — Personal Engineering Portfolio 🌐

[![Live Site](https://img.shields.io/badge/Live_Site-GitHub_Pages-2563EB?style=for-the-badge&logo=githubpages&logoColor=white)](https://prachizala.github.io/prachi-portfolio/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Tests Passing](https://img.shields.io/badge/Tests-7%20Passing-10B981?style=for-the-badge&logo=pytest&logoColor=white)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](LICENSE)

> **High-performance, zero-framework personal developer portfolio showcasing production backends, computer vision applications, and data analytics systems.**

Live Deployment: **[https://prachizala.github.io/prachi-portfolio/](https://prachizala.github.io/prachi-portfolio/)**

---

## 🎯 The Problem & Purpose

Recruiters and engineering managers often struggle to evaluate student portfolios due to heavy, bloated website templates that take seconds to load, broken navigation links, and lack of verifiable technical depth.

This portfolio is hand-crafted with pure semantic HTML5, modern CSS3, and vanilla JavaScript to deliver:
- **Instant sub-second loading** (zero megabyte-heavy JS bundles or framework overhead).
- **Universal responsiveness** across mobile phones, tablets, laptops, and ultra-wide displays.
- **Strict accessibility (WCAG 2.1 AA compliant)** with high contrast ratios, distinct `:focus-visible` states, and full screen-reader readability.

---

## 📸 Visual Preview & Interface

```
+-------------------------------------------------------------------------+
| [P] Prachi Zala                  [About] [Skills] [Projects] [Contact]  |
+-------------------------------------------------------------------------+
|                                                                         |
|  👋 Hi, I'm Prachi Zala                                                 |
|  Python Developer | AI & Data Analytics Engineer                        |
|  BCA Student @ Ahmedabad, Gujarat                                       |
|                                                                         |
|  [View Featured Projects]    [Download Resume (PDF)]                    |
|                                                                         |
+-------------------------------------------------------------------------+
|  PROJECT SHOWCASE:                                                      |
|  * AI Smart Attendance System (OpenCV + Geofencing + Streamlit)          |
|  * Student Performance Predictor (Pandas + Scikit-Learn Dashboard)      |
|  * Mood Tracker with NLP (Sentiment Analysis + VADER + Streamlit)        |
|  * Sales & Expense Analytics (Plotly + Data Cleaning Pipeline)          |
+-------------------------------------------------------------------------+
```
*(Screenshot placeholder: `./image/portfolio-preview.png`)*

---

## 🚀 Key Features

* ⚡ **Ultra-Fast First Contentful Paint (FCP):** 100% vanilla code with zero external runtime dependencies.
* 🌓 **Automatic Day/Night Dark Mode:** Listens to system preferences via CSS `prefers-color-scheme: dark` with carefully selected CSS custom property tokens.
* 📐 **Fluid Typography & Adaptive Layouts:** Utilizes CSS `clamp()` and CSS Grid/Flexbox for seamless transitions without layout clipping.
* 📱 **SEO & Rich Social Cards:** Pre-configured OpenGraph (`og:title`, `og:description`, `og:image`) and Twitter Cards for rich link previews when shared on LinkedIn, Twitter, or Discord.
* 🧪 **Automated Test Suite:** Built-in Python test suite (`tests/test_portfolio.py`) validating HTML structure, accessibility attributes, internal anchor integrity, and assets.

---

## 🛠️ Tech Stack & Architecture

- **Markup:** Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`)
- **Styling:** Modern CSS3 (CSS Variables, Flexbox, CSS Grid, Media Queries)
- **Scripting:** Vanilla JavaScript (ES6+ for smooth interactions and active section detection)
- **Testing:** Python `unittest` (`html.parser` for AST-like DOM validation)
- **Hosting:** GitHub Pages with custom CNAME / HTTPS enforcement

---

## 📂 Project Structure

```
prachi-portfolio/
│
├── .gitignore              # Ignored local editor configs and OS artifacts
├── CHANGELOG_EXPLAINED.md  # Detailed release history and rationale
├── index.html              # Main single-page application and markup
├── LICENSE                 # MIT Open Source License
├── README.md               # Comprehensive documentation and developer guide
├── resume.pdf              # Verified downloadable ATS-friendly resume
│
├── image/                  # Optimized visual assets and profile photos
│   └── profile.jpeg
│
└── tests/                  # Automated validation tests
    ├── __init__.py
    └── test_portfolio.py   # DOM, SEO, a11y, and anchor integrity checks
```

---

## 💻 Local Setup & Running Tests

### 1. Clone the repository
```bash
git clone https://github.com/prachizala/prachi-portfolio.git
cd prachi-portfolio
```

### 2. Run Locally
Because this project uses pure web standards, no compilation or npm installations are needed. Simply open `index.html` in any modern web browser or start a lightweight local web server:

```bash
# Using Python's built-in HTTP server:
python -m http.server 8000
```
Then visit: `http://localhost:8000`

### 3. Run Automated Tests
```bash
python -m unittest tests/test_portfolio.py
```

---

## 🔮 Future Enhancements
- [ ] Add an interactive terminal / command-line easter egg for visiting engineers.
- [ ] Add a dynamic blog/technical writing section pulling posts from Hashnode or Dev.to via RSS.
- [ ] Add Lighthouse CI automated workflow on every git push.

---

## 👤 Author & Contact

**Prachi Zala**  
- **Location:** Ahmedabad, Gujarat, India  
- **GitHub:** [@prachizala](https://github.com/prachizala)  
- **LinkedIn:** [Prachi Zala](https://www.linkedin.com/in/prachi-zala-74a08b334/)  
- **Email:** `[ADD CONTACT EMAIL]`
