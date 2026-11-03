# Prachi Zala — Personal Portfolio

[![Live Site](https://img.shields.io/badge/Live_Site-GitHub_Pages-blue.svg)](https://prachizala.github.io/prachi-portfolio/)
[![HTML5](https://img.shields.io/badge/HTML5-Semantic-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Modern_Responsive-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/CSS)

A clean, responsive personal portfolio website showcasing software development projects, technical skills, and academic achievements. Designed with accessibility, dark mode support, and typography in mind.

---

## 🌐 Live Preview

- **Live URL:** [https://prachizala.github.io/prachi-portfolio/](https://prachizala.github.io/prachi-portfolio/)
- **Author:** Prachi Zala (BCA Student, Ahmedabad)
- **LinkedIn:** [linkedin.com/in/prachi-zala-74a08b334](https://www.linkedin.com/in/prachi-zala-74a08b334/)

---

## 🚀 Key Highlights & Design Decisions

1. **Lightweight & Fast:** Zero heavy external frontend frameworks (no heavy React/Vue runtime). Pure semantic HTML5 and vanilla CSS for instant sub-second First Contentful Paint (FCP).
2. **Automatic Dark Mode:** Utilizes CSS `prefers-color-scheme: dark` with adaptive color variables (`--paper`, `--surface`, `--ink`, `--accent`) for seamless day/night theme transitions.
3. **Accessibility (WCAG Compliant):**
   - High color contrast ratios on all text elements.
   - Distinct `:focus-visible` outlines for full keyboard navigation.
   - Fluid typography using `clamp()` for responsive mobile-to-desktop scaling without layout overflow.
4. **Social & SEO Optimization:** Configured Open Graph (`og:title`, `og:description`, `og:url`) and Twitter Card metadata for rich previews when shared on LinkedIn or Twitter.

---

## 🛠️ Local Development

To run the portfolio locally:

```bash
# Clone the repository
git clone https://github.com/prachizala/prachi-portfolio.git
cd prachi-portfolio

# Start a simple HTTP server using Python:
python -m http.server 3000

# Or using Node.js:
npx serve .
```

Open `http://localhost:3000` in your web browser.

---

## 📄 License

Licensed under the [MIT License](LICENSE).
