# Changes Log - Work Package 4: Small Feature Upgrades

## Summary of Changes

### 1. Image Optimization & Lazy Loading (`index.html`)
- Added `loading="lazy"` attribute to portrait profile image (`image/profile.jpeg`) to defer off-screen image decoding and reduce initial page weight / Largest Contentful Paint (LCP) contention.

### 2. Viewport Meta Verification (`index.html`)
- Verified standard responsive viewport configuration `<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">` ensures responsive scaling across mobile, tablet, and desktop form factors.

### 3. Font Rendering Performance (`index.html`)
- Injected `@font-face` declarations with `font-display: swap;` inside `<style>` for `Bricolage Grotesque` and `DM Sans` web fonts, eliminating flash of invisible text (FOIT) during web font loading.

### 4. Automated Test Suite Validation
- Executed `python -m unittest tests/test_portfolio.py`.
- All 7 tests pass 100% (`Ran 7 tests in 0.005s ... OK`).

## Items Skipped & Rationale
- None.

## Manual Steps Needed
- None. Open `index.html` in any browser or launch local HTTP server to preview.
