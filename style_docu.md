# Sanskrit Library HTML Template — Design & Features Documentation

**Version:** 1.0  
**Last Updated:** July 23, 2026  
**Purpose:** Reference blueprint for generating consistent, feature-rich HTML editions of Sanskrit texts (with or without commentaries) for the Sanskrit Library project.

---

## 1. Overview

This template is a **single-file, self-contained HTML document** designed for offline/mobile reading of Sanskrit texts. It requires **no external dependencies** — all CSS and JavaScript are embedded. The design prioritizes:

- **Readability** of Devanāgarī script
- **Accessibility** on mobile devices
- **Customizability** (font size, theme)
- **Navigability** across long texts (30+ chapters)
- **Searchability** within the document

---

## 2. File Structure

```
text-name.html
├── <head>
│   ├── Meta tags (charset, viewport, title)
│   ├── Embedded <style> block
│   └── CSS variables for theming
├── <body>
│   ├── <header class="toolbar">        ← Sticky navigation bar
│   ├── <main>
│   │   ├── <div class="metadata">      ← Book info card
│   │   ├── <div class="search-box">    ← Search input
│   │   ├── <nav class="toc">           ← Table of Contents
│   │   └── <section class="verse-block"> ← Repeated per verse/chapter
│   │       ├── <h3 class="verse-header">
│   │       └── <div class="verse-content">
│   │           ├── <div class="moola">       ← Root text (optional)
│   │           └── <div class="vyakhya">     ← Commentary
│   ├── <aside class="footnotes">       ← Footnotes section
│   └── <footer>
└── <script>                            ← Embedded JS
```

---

## 3. Visual Design System

### 3.1 Color Palette (CSS Variables)

Two themes are supported via `data-theme` attribute on `<body>`:

| Variable         | Light Theme | Dark Theme | Purpose                       |
|------------------|-------------|------------|-------------------------------|
| `--bg`           | `#fdfbf7`   | `#1a1a1a`  | Page background               |
| `--text`         | `#333`      | `#d4d4d4`  | Body text                     |
| `--heading`      | `#8b0000`   | `#ff6b6b`  | Headings, accents (deep red)  |
| `--border`       | `#d2691e`   | `#ff8c00`  | Borders, dividers (ochre)     |
| `--card`         | `#fff`      | `#252525`  | Card backgrounds              |
| `--moola-bg`     | `#fffaf0`   | `#2a2a2a`  | Root text background (cream)  |
| `--vyakhya-bg`   | `#f9f9f9`   | `#222`     | Commentary quote background   |
| `--link`         | `#0055aa`   | `#66b3ff`  | Hyperlinks                    |
| `--base-font`    | `18px`      | `18px`     | Base font size (dynamic)      |

### 3.2 Typography

- **Font stack:** `'Noto Serif Devanagari', 'Noto Serif', 'Times New Roman', serif`
- **Line height:** `1.8` (optimized for long-form Sanskrit reading)
- **Max width:** `900px` (centered, comfortable reading measure)

### 3.3 Layout

- **Sticky toolbar** at top with `z-index: 100` and subtle shadow
- **Card-based** verse blocks with `border-radius: 4px` and `margin-bottom: 20px`
- **Two-column** TOC and footnotes on desktop, single-column on mobile (`@media max-width: 600px`)

---

## 4. Features & Functionality

### 4.1 Sticky Toolbar

Fixed at the top during scroll. Contains:

```html
<header class="toolbar">
    <a href="../index.html">☰ Sanskrit Library</a>
    <div>
        <button onclick="toggleAll()">Collapse/Expand All</button>
        <button onclick="changeFontSize(-1)">A−</button>
        <button onclick="changeFontSize(1)">A+</button>
        <button onclick="toggleDarkMode()">☾</button>
        <select onchange="scrollToChapter(this.value)">
            <option value="">Chapters ▾</option>
            <!-- Dynamic options -->
        </select>
    </div>
</header>
```

### 4.2 Theme Toggle (Dark/Light Mode)

- Toggles `data-theme` attribute on `<body>` between `light` and `dark`
- CSS variables automatically switch palette
- Smooth transition via `transition: background 0.3s, color 0.3s` on `body`

```javascript
function toggleDarkMode() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    body.setAttribute('data-theme', currentTheme === 'dark' ? 'light' : 'dark');
}
```

### 4.3 Dynamic Font Size (Zoom In/Out)

- Adjusts `--base-font` CSS variable in increments of `1px`
- **Bounds:** minimum `14px`, maximum `28px`
- Persists only for the current session

```javascript
function changeFontSize(delta) {
    const root = document.documentElement;
    let currentSize = parseFloat(getComputedStyle(root).getPropertyValue('--base-font')) || 18;
    currentSize += delta;
    if (currentSize < 14) currentSize = 14;
    if (currentSize > 28) currentSize = 28;
    root.style.setProperty('--base-font', currentSize + 'px');
}
```

> **Note:** Earlier versions had a bug where `--base-font-size` was used instead of `--base-font`. Ensure variable names match between CSS and JS.

### 4.4 Collapse/Expand All

Toggles visibility of all `.verse-content` divs simultaneously. Updates toggle button labels (`[-]` / `[+]`).

```javascript
function toggleAll() {
    const contents = document.querySelectorAll('.verse-content');
    const isCollapsed = contents[0] && contents[0].style.display === 'none';
    contents.forEach(c => c.style.display = isCollapsed ? 'block' : 'none');
    document.querySelectorAll('.toggle-btn').forEach(btn => 
        btn.textContent = isCollapsed ? '[-]' : '[+]');
}
```

### 4.5 Individual Verse Collapse

Each verse block has a clickable header with a toggle button:

```html
<section class="verse-block" id="ch-1">
    <h3 class="verse-header">
        1. Chapter Title 
        <span class="toggle-btn" onclick="toggleVerse(this)">[-]</span>
    </h3>
    <div class="verse-content">
        <!-- Content -->
    </div>
</section>
```

### 4.6 Chapter Navigation Dropdown

`<select>` element with all chapters as options. Smooth scroll on selection:

```javascript
function scrollToChapter(id) {
    if (id) {
        document.getElementById(id).scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start' 
        });
    }
}
```

### 4.7 Full-Text Search

Real-time search across all verse blocks. Hides non-matching verses and shows a "No results" message when empty.

```javascript
function searchVerses() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const verses = document.querySelectorAll('.verse-block');
    let matchCount = 0;
    verses.forEach(v => {
        const text = v.textContent.toLowerCase();
        if (text.includes(input)) {
            v.style.display = 'block';
            matchCount++;
        } else {
            v.style.display = 'none';
        }
    });
    document.getElementById('noResults').style.display = 
        matchCount === 0 && input.length > 0 ? 'block' : 'none';
}
```

### 4.8 Table of Contents (TOC)

Two-column ordered list with anchor links to each chapter/verse:

```html
<nav class="toc">
    <h3>विषयसूची (Table of Contents)</h3>
    <ol>
        <li><a href="#ch-1">1. Chapter Title</a></li>
        <!-- ... -->
    </ol>
</nav>
```

### 4.9 Metadata Card

Displays book information in a visually distinct card:

```html
<div class="metadata">
    <h1>Book Title</h1>
    <p><strong>Author:</strong> Name | <strong>Composed:</strong> Year</p>
    <p><strong>Category:</strong> Vedānta | <strong>Language:</strong> Sanskrit</p>
    <p><em>Description text</em></p>
</div>
```

---

## 5. Content Organization Patterns

### 5.1 Verse Block Structure (with Commentary)

Used for texts with root text + commentary (e.g., Śrībhāṣyabhāvaprakāśaḥ):

```html
<section class="verse-block" id="ch-N">
    <h3 class="verse-header">
        N. Chapter/Verse Title 
        <span class="toggle-btn" onclick="toggleVerse(this)">[-]</span>
    </h3>
    <div class="verse-content">
        <div class="moola">
            <!-- Root text in Devanāgarī -->
        </div>
        <div class="vyakhya">
            <p>Commentary paragraphs...</p>
            <blockquote class="quote">
                <!-- Quoted passages from other texts -->
            </blockquote>
        </div>
    </div>
</section>
```

### 5.2 Verse Block Structure (with Prakāśikā)

Used for texts with verse + detailed gloss (e.g., Kaṭha Upaniṣad):

```html
<section class="verse-block" id="ch-N">
    <h3 class="verse-header">
        Verse N 
        <span class="toggle-btn" onclick="toggleVerse(this)">[-]</span>
    </h3>
    <div class="verse-content">
        <!-- Verse text directly -->
        <p>Author's Prakāśikā commentary...</p>
    </div>
</section>
```

### 5.3 Collapsible Sub-sections

For complex commentaries with nested discussions:

```html
<details>
    <summary>पूर्वपक्षः (द्रष्टुं नोद्यम्)</summary>
    <!-- Hidden content -->
</details>
```

### 5.4 Footnotes

Numbered list at document end with back-links:

```html
<aside class="footnotes">
    <h3>टिप्पण्यः (Footnotes)</h3>
    <ol>
        <li id="fn1"><a href="#fnref1">↩</a> Source reference</li>
    </ol>
</aside>
```

Inline references use superscript anchors:
```html
<sup><a href="#fn1" id="fnref1">1</a></sup>
```

### 5.5 Colophon

Centered closing section with traditional Sanskrit colophon format:

```html
<div class="colophon">
    <h2>॥ इति ग्रन्थः संपूर्णः ॥</h2>
    <p>Closing verses / publication info</p>
</div>
```

---

## 6. Responsive Design

### Breakpoints

| Screen Width | Behavior                                           |
|--------------|----------------------------------------------------|
| `> 600px`    | Two-column TOC and footnotes, full toolbar         |
| `≤ 600px`    | Single-column TOC/footnotes, centered toolbar      |

### Mobile Considerations

- Touch-friendly button sizes (`padding: 5px 10px`)
- No horizontal scrolling
- Sticky toolbar remains accessible
- Font size adjustable for small screens

---

## 7. Accessibility Features

- Semantic HTML5 tags (`<header>`, `<main>`, `<nav>`, `<section>`, `<aside>`, `<footer>`)
- `lang="sa"` attribute on `<html>` for Sanskrit
- Proper heading hierarchy (h1 → h2 → h3)
- Anchor links for navigation
- Sufficient color contrast in both themes
- Keyboard-navigable buttons and dropdowns

---

## 8. Performance Characteristics

- **Zero external requests** — fully self-contained
- **No frameworks** — vanilla HTML/CSS/JS
- **Small file size** — typically 100-500 KB per text
- **Fast rendering** — no JavaScript required for basic reading
- **Offline-capable** — works without internet connection

---

## 9. Customization Guide

### 9.1 Adding a New Text

1. Copy the template HTML file
2. Update `<title>` and metadata card
3. Replace TOC `<ol>` items with new chapter list
4. Replace `<select>` options in toolbar
5. Replace verse blocks with new content
6. Update footer text

### 9.2 Changing the Color Scheme

Modify CSS variables in `:root` and `[data-theme="dark"]`:

```css
:root {
    --heading: #your-color;
    --border: #your-color;
    /* etc. */
}
```

### 9.3 Adjusting Font Size Bounds

In `changeFontSize()` function:

```javascript
if (currentSize < 12) currentSize = 12;  // New minimum
if (currentSize > 32) currentSize = 32;  // New maximum
```

### 9.4 Adding Print Styles

```css
@media print {
    .toolbar, .search-box, .toggle-btn { display: none; }
    .verse-content { display: block !important; }
    body { background: white; color: black; }
}
```

---

## 10. Known Limitations & Future Enhancements

### Current Limitations

- No persistent state (theme/font size reset on reload)
- No audio recitation support
- No word-by-word parsing
- No parallel translation display
- Search is case-sensitive for Devanāgarī (works, but no fuzzy matching)

### Potential Enhancements

- **LocalStorage** for theme/font persistence
- **Audio integration** for mantra recitation
- **Transliteration toggle** (Devanāgarī ↔ IAST)
- **Cross-reference linking** between related texts
- **Progressive disclosure** for very long commentaries
- **Export to PDF** button
- **Bookmark** specific verses

---

## 11. Usage Examples in the Project

This template has been successfully applied to:

| Text                              | Chapters | Verses | Commentary Type        |
|-----------------------------------|----------|--------|------------------------|
| Śrībhāṣyabhāvaprakāśaḥ           | 31       | 31     | Scholarly discussion   |
| Śrīnyāsaviṃśatiḥ (with Vyākhyā)  | 22       | 22     | Traditional Vyākhyā    |
| Kaṭha Upaniṣad (with Prakāśikā)  | 6        | 120    | Verse-by-verse gloss   |

---

## 12. Quick-Start Checklist

When generating a new HTML file from this template:

- [ ] Update `<title>` tag
- [ ] Update `<h1>` in metadata card
- [ ] Fill in author, date, category, verse count
- [ ] Replace TOC list with actual chapters
- [ ] Replace `<select>` dropdown options
- [ ] Add all verse blocks with unique `id` attributes
- [ ] Verify all anchor links work
- [ ] Test dark mode toggle
- [ ] Test font size buttons
- [ ] Test search functionality
- [ ] Test on mobile viewport
- [ ] Add footnotes section if needed
- [ ] Update footer text

---

## 13. File Naming Convention

```
{text-name-short}.html
```

Examples:
- `katha-upanishad.html`
- `bhavaprakasha-ked.html`
- `nyasavimshati.html`

Use lowercase, hyphen-separated names for URL compatibility.

---

## 14. Contact & Maintenance

This template is maintained as part of the Sanskrit Library project. For modifications or bug reports, refer to the project repository.

---

**End of Documentation**
