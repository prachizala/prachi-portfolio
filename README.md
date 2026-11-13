# Prachi Zala — Personal Engineering Portfolio Website

[![Live Preview](https://img.shields.io/badge/Live_Site-GitHub_Pages-blue.svg?style=flat-square&logo=google-chrome&logoColor=white)](https://prachizala.github.io/prachi-portfolio/)
[![HTML5](https://img.shields.io/badge/HTML5-Semantic_Accessible-E34F26.svg?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Modern_Responsive-1572B6.svg?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E.svg?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

> **High-performance, accessibility-focused, mobile-responsive personal engineering portfolio website deployed on GitHub Pages.**

---

## 🌐 Live Preview

* **Live URL:** [https://prachizala.github.io/prachi-portfolio/](https://prachizala.github.io/prachi-portfolio/)
* **Hosted on:** GitHub Pages (Automatic CI/CD deployment on push to `master`)

---

## 🎯 The Problem It Solves

* **Bloated Portfolio Sites:** Many modern portfolios rely on heavy JavaScript framework runtimes (Next.js/React bundles exceeding 2-3MB), resulting in slow initial load times, sluggish mobile navigation, and poor lighthouse scores.
* **Our Solution:** A **zero-dependency, pure semantic architecture**:
  * Ultra-fast First Contentful Paint (sub-400ms FCP).
  * 100% responsive fluid layout scaling from mobile viewports (320px) up to 4K displays using CSS `clamp()` and CSS Grid.
  * Native dark/light theme awareness adhering to system preferences.

---

## 🚀 Key Features

* ⚡ **Lightning Fast Performance:** Zero external framework overhead; clean native HTML5, modern CSS3 variables, and lightweight ES6+ JavaScript.
* 🌓 **Adaptive Theming:** Automatic theme switching via CSS `prefers-color-scheme: dark` with curated color tokens (`--paper`, `--surface`, `--ink`, `--accent`).
* ♿ **Accessibility (WCAG AA Compliant):**
  * Explicit keyboard `:focus-visible` ring indicators.
  * High-contrast color ratios ensuring legibility.
  * Semantic landmark tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
* 📱 **Showcase of 11 Production Engineering Projects:**
  * Distributed Task Engine (Celery + Redis + FastAPI)
  * PulseSync (Offline-First Emergency Dispatch Engine)
  * Enterprise Knowledge Copilot (GraphRAG + Neo4j)
  * AI Smart Attendance System (GPS Haversine + OpenCV Face Verification)
  * 90-Day Workforce Attendance Analytics (XGBoost ROC-AUC 0.908)
  * Dharohar 4D, Qoneqt-ContentOS, MathSprint, WeatherGPT, CricketIQ, Mental Health Tracker.
* 📄 **Embedded Resume Integration:** Direct 1-click download link to up-to-date PDF resume.

---

## 🛠️ Tech Stack

| Layer | Technologies & Tools |
| :--- | :--- |
| **Markup & Semantics** | HTML5 (Semantic landmarks, Open Graph meta tags, Twitter Cards) |
| **Styling & Layout** | CSS3 (Custom properties, CSS Grid, Flexbox, Fluid `clamp()` typography) |
| **Interactivity** | Vanilla JavaScript (ES6+), smooth scroll, dynamic year injection |
| **Hosting & Deployment** | GitHub Pages, Custom domain ready |

---

## 📂 Project Structure

```
prachi-portfolio/
├── index.html                  # Single-page semantic portfolio architecture
├── style.css                   # Custom token design system & responsive bands
├── app.js                      # DOM interactions and smooth scrolling
├── resume.pdf                  # Downloadable curriculum vitae
└── README.md                   # Repository documentation
```

---

## 💻 Local Development & Run Guide (Tested)

### 1. Clone Repository
```bash
git clone https://github.com/prachizala/prachi-portfolio.git
cd prachi-portfolio
```

### 2. Launch Local Server
You can run this site using any local static file server:

* **Using Python 3:**
  ```bash
  python -m http.server 3000
  ```

* **Using Node.js:**
  ```bash
  npx serve .
  ```

* **Using VS Code:**
  Install the **Live Server** extension and click **"Go Live"**.

* Open `http://localhost:3000` in your web browser.

---

## 📸 Screenshots & Demo

| 💻 Desktop Overview | 📱 Mobile Responsiveness | ⚡ Projects Showcase |
| :---: | :---: | :---: |
| *(Placeholder: Desktop View)* | *(Placeholder: Mobile View)* | *(Placeholder: Projects Grid)* |

---

## 🔮 Future Improvements

1. **Interactive Terminal Mode:** Add a retro hacker terminal modal allowing recruiters to run CLI commands (e.g. `skills`, `projects`, `contact`).
2. **Dynamic GitHub Activity Feed:** Fetch live repository commit stats and pull request telemetry via GitHub REST API.
3. **PWA Offline Support:** Add a service worker (`sw.js`) and manifest file for offline viewing.

---

## 👩‍💻 Author & Maintainer

**Prachi Zala**  
*BCA Student | Python, Distributed Systems & Applied AI Developer*  
*Shanti Business School, Ahmedabad, Gujarat, India*  

* **LinkedIn:** [linkedin.com/in/prachi-zala-74a08b334](https://www.linkedin.com/in/prachi-zala-74a08b334)  
* **GitHub:** [github.com/prachizala](https://github.com/prachizala)  
* **Live Site:** [prachizala.github.io/prachi-portfolio](https://prachizala.github.io/prachi-portfolio/)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
