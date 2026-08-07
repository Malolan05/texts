▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
✦ Sanskrit Library Digital Editions

  Standardized, zero-dependency, offline-first classical Sanskrit texts with interactive multi-tiered commentaries, dynamic font adjustments, persistent dark mode, and instant client-side search.

  ---

  ![License: CC BY-NC-SA 4.0 (https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
  ![HTML5 (https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](#)
  ![CSS3 (https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](#)
  ![JavaScript (https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](#)

  📖 Mission & Design Philosophy

  The Sanskrit Library Digital Editions project aims to digitize, preserve, and distribute classical Sanskrit literature in a format that is universally accessible, academically rigorous, and extremely durable. 

  Traditional digitization projects often rely on heavy web frameworks, external database queries, or active internet connections. This repository takes the opposite approach, adopting a Single-File, Zero-Dependency Architecture. Each
  text is packaged into an individual, completely self-contained .html file containing all structural content, visual stylesheets, responsive media definitions, and interactive JavaScript engines. 

  Why This Architecture?
   * Absolute Offline Portability: Perfect for remote areas, mobile reading, or offline scholarly environments. Download a file once, and it will run with 100% feature parity anywhere.
   * Archival Longevity: By strictly avoiding external frameworks (React, Tailwind, Bootstrap), web fonts, or database APIs, these files remain immune to breaking changes, server deprecations, or security vulnerabilities over decades.
   * Superior Devanāgarī Readability: Optimized letter-spacing, line-heights (1.8–2.0), and fallback typography stacks designed specifically to prevent Devanāgarī vowel accents (mātrās) and consonant conjuncts (halantas) from colliding.

  ---

  ✨ Features

   - 🌓 Persistent Theme Switcher: Smoothly toggle between Light and Dark modes. The user's preference is saved to localStorage and applied instantly on subsequent page loads before rendering to prevent layout flashing.
   - 🔍 Instant client-side Search: Fast, real-time filtering of verses and commentaries using Devanāgarī or English transliteration (IAST). Non-matching blocks are automatically hidden, and matched sections expand dynamically.
   - 🔍 Interactive Accordions: Expand or collapse individual chapters/verses with responsive button toggles, or use the master control to toggle everything on screen.
   - 📱 Responsive & Accessible UI: Dynamic CSS Grid structure adaptively adjusts between widescreen desktops and mobile viewports. Layouts meet strict WCAG 2.1 AA accessibility contrast guidelines.
   - 🔤 Dynamic Typography Scaler: Dynamically scale text sizing between 14px and 28px to support a wide range of devices and visual needs.
   - 📚 Bidirectional Scholarly Footnotes: Link inline superscript anchors to bibliographic references at the bottom of the document, with quick return links that highlight the target item's active state.
   - 🖨️ Academic Print Engine: A specialized @media print layout stylesheet automatically strips out UI toolbars, search boxes, navigation selects, and layout cards, formatting the text into clean, printable pages with strict pagination
     rules.

  ---

  📂 Repository Structure

  The workspace is organized to keep raw templates separate from verified, ready-to-read text editions:

    1 sanskrit-library-editions/
    2 ├── LICENSE                    # CC BY-NC-SA 4.0 License
    3 ├── README.md                  # This documentation file
    4 ├── index.html                 # Main portal / Table of Contents of the library
    5 ├── template-blueprint.html    # Core, unpopulated single-file HTML blueprint
    6 ├── texts/                     # Production-ready digitized Sanskrit texts
    7 │   ├── katha-upanishad.html   # Kaṭha Upaniṣad (with Prakāśikā)
    8 │   ├── nyasavimshati.html     # Śrīnyāsaviṃśatiḥ (with Vyākhyā)
    9 │   └── bhavaprakasha-ked.html # Śrībhāṣyabhāvaprakāśaḥ
   10 └── tools/                     # Automation & validation scripts
   11     └── validate_ids.py        # Python script to check HTML structural integrity

  ---

  🚀 Getting Started

  For Readers
  To read any text in this library offline:
   1. Navigate to the texts/ folder in this repository.
   2. Click on the text file you wish to read (e.g., katha-upanishad.html).
   3. Click the Download (Raw) button.
   4. Open the downloaded file in any modern browser on your desktop, tablet, or smartphone. No internet connection is required.

  ---

  ✍️ Contribution Guide (Adding a New Text)

  We welcome digitized contributions! To convert a Sanskrit text with its commentaries into our standardized single-file format, follow these steps:

  Step 1: Copy the Blueprint
  Copy the template-blueprint.html file into the texts/ directory and rename it according to our file naming convention.

  File Naming Convention:
   * lowercase, hyphen-separated string of the transliterated text name.
   * Format: {text-name-short}.html
   * Example: katha-upanishad.html, bhavaprakasha-ked.html

  Step 2: Update Metadata & Header
  Open the file in a code editor and modify:
   1. The <title> tag in the <head>.
   2. The <h1> title, author, date, and category inside the <section class="metadata"> card.
   3. The table of contents list <nav class="toc">.
   4. The <select> options in the sticky toolbar header to match your document chapters.

  Step 3: Populate Content Blocks
  Use the following HTML structure for each verse or chapter block:

    1 <section class="verse-block" id="ch-1.1">
    2     <h3 class="verse-header" onclick="toggleSingleVerse('ch-1.1')">
    3         १. मङ्गलश्लोकः (Verse 1.1)
    4         <span class="toggle-btn" id="btn-ch-1.1">[-]</span>
    5     </h3>
    6     <div class="verse-content" id="content-ch-1.1">
    7         <!-- Root Devanāgarī Verse -->
    8         <div class="moola">
    9             नारायणं नमस्कृत्य नरं चैव नरोत्तमम् ।<br>
   10             देवीं सरस्वतीं व्यासं ततो जयमुदीरयेत् ॥ १.१ ॥
   11         </div>
   12         <!-- Commentary Section -->
   13         <div class="vyakhya">
   14             <p><strong>भाष्यम्:</strong> नारायणं जगत्प्रभवं देवं नमस्कृत्य...</p>
   15             <blockquote class="quote">
   16                 <strong>प्रमाणम्:</strong> "नारायणः परोऽव्यक्तात्" इति श्रुतिसिद्धान्तः।<sup><a href="#fn1" id="fnref1">1</a></sup>
   17             </blockquote>
   18         </div>
   19     </div>
   20 </section>

  Step 4: Map Your Identifiers
  To ensure the interactive accordion and search features function properly, you must align your element IDs precisely. For each verse block, verify the following elements share matching IDs:

   * Container block ID: id="ch-X"
   * Header onclick target: onclick="toggleSingleVerse('ch-X')"
   * Content container ID: id="content-ch-X"
   * Toggle button ID: id="btn-ch-X"

  Step 5: Test and Validate
  Run the validation script before submitting a Pull Request to check for missing IDs, malformed anchor tags, or duplicate identifiers:

   1 python tools/validate_ids.py texts/your-new-text.html

  ---

  🛠️ Quality & Coding Standards

  To maintain the long-term reliability and compatibility of the library, all contributions must adhere to these rules:

   1. Zero External Frameworks: Under no circumstances should dependencies like Tailwind CSS, Bootstrap, jQuery, Google Fonts, or React be injected. All script and style blocks must reside completely inside the file.
   2. Standard Fallback Typography: Always include the standard typography stack in the page style declarations to ensure clean fallback behavior if a system does not have Noto Devanagari installed:

   1    font-family: 'Noto Serif Devanagari', 'Noto Serif', 'Times New Roman', serif;
   3. Valid HTML5 Semantics: Leverage semantic landmarks exclusively (<header>, <main>, <nav>, <section>, <aside>, <footer>) to facilitate smooth screen reader operations.
   4. Offline Compatibility: Double-click the completed file to test its execution locally with all internet connectivity disabled. Dynamic scaling, dark mode, navigation, and text filtering must remain fully functional.

  ---

  ⚖️ License

  The text editions and coding structures contained in this repository are distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

  You are free to:
   * Share — Copy and redistribute the material in any medium or format.
   * Adapt — Remix, transform, and build upon the material.

  Under the following terms:
   * Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
   * NonCommercial — You may not use the material for commercial purposes.
   * ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
