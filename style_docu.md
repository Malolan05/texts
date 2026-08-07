 #Sanskrit Library HTML Template — Design & Features Documentation

  Version: 1.1  
  Last Updated: August 7, 2026  
  Purpose: Comprehensive reference blueprint for generating consistent, feature-rich, high-performance HTML editions of Sanskrit texts (with or without commentaries) for the Sanskrit Library project.
  Scope: Single-file, self-contained, offline-first responsive design.

  ---

  1. Executive Summary & Design Philosophy

  The Sanskrit Library HTML template is an architectural blueprint for delivering classical Sanskrit texts digitally. It targets researchers, students, and practitioners who require distraction-free reading environments on both desktop
  and mobile screens, often in offline settings.

  Core Architectural Pillars
   1. Zero External Dependencies: To guarantee longevity, instant rendering, and absolute offline compatibility, the template forbids external CSS frameworks, JavaScript libraries, or third-party web fonts. Every asset must be inline or
      system-fallback.
   2. Devanāgarī Legibility First: Devanāgarī requires generous vertical breathing room compared to Latin scripts. The visual hierarchy utilizes large base font sizes, high line-heights (1.8–2.0), and strict contrast ratios to prevent eye
      strain during prolonged reading.
   3. Session-Level Persistence: User preferences for typography scaling and dark/light color themes persist seamlessly across sessions using modern browser features without bloating the file size.
   4. Offline Resilience: The single-file distribution pattern allows a user to save the document directly to a local disk or mobile device storage and run it with 100% feature parity.

  ---

  2. Document Architecture & File Structure

  The document is organized into clear HTML5 semantic landmarks. This guarantees excellent accessibility (screen readers, keyboard navigation) and allows modern search engines to parse the content with high precision.

    1 text-name.html
    2 ├── <!DOCTYPE html>
    3 ├── <html lang="sa">
    4 │   ├── <head>
    5 │   │   ├── UTF-8 Charset & Mobile Viewport Configuration
    6 │   │   ├── SEO & Social Metadata (OpenGraph/Schema.org)
    7 │   │   ├── CSS Variables (Light & Dark Themes)
    8 │   │   └── Main Embedded stylesheet (<style>)
    9 │   └── <body> (with optional data-theme attribute)
   10 │       ├── <header class="toolbar">        ← Fixed/Sticky control panel
   11 │       ├── <main class="container">
   12 │       │   ├── <section class="metadata">  ← Work details & provenance card
   13 │       │   ├── <section class="search-box">← Real-time instant-filter interface
   14 │       │   ├── <nav class="toc">           ← Table of Contents (2-column layout)
   15 │       │   └── <article class="content">   ← Primary body container
   16 │       │       ├── <section class="verse-block">  ← Repeating item (Chapter/Verse)
   17 │       │       │   ├── <h3 class="verse-header">  ← Interactive collapsor header
   18 │       │       │   └── <div class="verse-content">
   19 │       │       │       ├── <div class="moola">    ← Primary/Root text (Devanāgarī)
   20 │       │       │       └── <div class="vyakhya">  ← Commentary & glosses
   21 │       │       └── ...
   22 │       ├── <aside class="footnotes">       ← Footnotes section (bidirectional anchors)
   23 │       └── <footer class="footer">         ← Traditional Colophon & License notes
   24 │       └── <script>                        ← Core Event Handlers & State engine

  ---

  3. Visual Design System

  3.1 Color Palette (CSS Custom Properties)
  The system employs fluid CSS variables defined on :root and overridden under [data-theme="dark"]. The palette is based on warm, organic tones reminiscent of traditional palm-leaf manuscripts (ochre, deep red, cream, charcoal) to provide
  a warm reading aesthetic.

  ┌──────────────┬────────────────────────┬────────────────────────────┬──────────────────────────────────────────┐
  │ CSS Variable │ Light Theme (Default)  │ Dark Theme                 │ Purpose                                  │
  ├──────────────┼────────────────────────┼────────────────────────────┼──────────────────────────────────────────┤
  │ --bg         │ #fdfbf7 (Warm Cream)   │ #141414 (Off-black)        │ Primary body background                  │
  │ --text       │ #2c2a29 (Charcoal)     │ #e2dfda (Soft grey)        │ Primary readable text                    │
  │ --heading    │ #8b0000 (Deep Crimson) │ #ff7b7b (Light coral)      │ Headers, accents, structural markers     │
  │ --border     │ #d2691e (Ochre)        │ #a85f2c (Muted terracotta) │ Borders, section dividers, indicators    │
  │ --card       │ #ffffff (Pure White)   │ #1d1c1b (Dark brown-grey)  │ Verse block backgrounds, search card     │
  │ --moola-bg   │ #fffaf0 (Floral White) │ #252321 (Warm slate)       │ Root text block background               │
  │ --vyakhya-bg │ #fdfdfd (Off-white)    │ #1a1918 (Deep card)        │ Commentary quote container               │
  │ --link       │ #0055aa (Cobalt blue)  │ #66b3ff (Soft sky blue)    │ Interactive hyperlinks & back-references │
  │ --base-font  │ 18px                   │ 18px                       │ Dynamic root calculation baseline        │
  └──────────────┴────────────────────────┴────────────────────────────┴──────────────────────────────────────────┘

  3.2 Typography Engine
  To ensure high-quality text rendering, the CSS font stack prioritizes native and highly distributed open-source Devanāgarī fonts.

   * Devanāgarī Script: 'Noto Serif Devanagari', 'Yatra One', 'Siddharth', 'Kohinoor Devanagari', serif
   * Latin Script Translation/Transliteration (IAST): 'Noto Serif', 'Gentium Book Plus', 'Times New Roman', serif
   * Line Height: Must be set to at least 1.8 for Devanāgarī, as vowel diacritics above (mātrās) and conjuncts below (halanta clusters) require extra vertical spacing to avoid overlapping text.

  ---

  4. Production-Ready Template (Complete Blueprint)

  This is the standard copy-pasteable, single-file HTML implementation. It includes all CSS, responsive design styles, accessibility standards, and the optimized state-persistence script block.

     1 <!DOCTYPE html>
     2 <html lang="sa">
     3 <head>
     4     <meta charset="UTF-8">
     5     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     6     <title>ग्रन्थनाम - Sanskrit Text Title</title>
     7     
     8     <style>
     9         /* CSS Variables & Themes */
    10         :root {
    11             --bg: #fdfbf7;
    12             --text: #2c2a29;
    13             --heading: #8b0000;
    14             --border: #d2691e;
    15             --card: #ffffff;
    16             --moola-bg: #fffaf0;
    17             --vyakhya-bg: #fdfdfd;
    18             --link: #0055aa;
    19             --base-font: 18px;
    20             --transition-speed: 0.25s;
    21         }
    22
    23         [data-theme="dark"] {
    24             --bg: #141414;
    25             --text: #e2dfda;
    26             --heading: #ff7b7b;
    27             --border: #a85f2c;
    28             --card: #1d1c1b;
    29             --moola-bg: #252321;
    30             --vyakhya-bg: #1a1918;
    31             --link: #66b3ff;
    32         }
    33
    34         /* Reset & Base Styles */
    35         * {
    36             box-sizing: border-box;
    37             margin: 0;
    38             padding: 0;
    39         }
    40
    41         body {
    42             background-color: var(--bg);
    43             color: var(--text);
    44             font-family: 'Noto Serif Devanagari', 'Noto Serif', 'Times New Roman', serif;
    45             font-size: var(--base-font);
    46             line-height: 1.8;
    47             transition: background-color var(--transition-speed), color var(--transition-speed);
    48             padding-bottom: 60px;
    49         }
    50
    51         /* Layout Container */
    52         .container {
    53             max-width: 900px;
    54             margin: 0 auto;
    55             padding: 20px;
    56         }
    57
    58         /* Sticky Toolbar */
    59         .toolbar {
    60             position: sticky;
    61             top: 0;
    62             z-index: 100;
    63             background-color: var(--card);
    64             border-bottom: 2px solid var(--border);
    65             padding: 10px 20px;
    66             display: flex;
    67             justify-content: space-between;
    68             align-items: center;
    69             box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    70         }
    71
    72         .toolbar-brand {
    73             font-weight: bold;
    74             color: var(--heading);
    75             text-decoration: none;
    76             font-size: 1.1rem;
    77         }
    78
    79         .toolbar-controls {
    80             display: flex;
    81             align-items: center;
    82             gap: 8px;
    83         }
    84
    85         /* Interactive Controls */
    86         button, select {
    87             background-color: var(--bg);
    88             color: var(--text);
    89             border: 1px solid var(--border);
    90             padding: 6px 12px;
    91             font-family: inherit;
    92             font-size: 0.9rem;
    93             border-radius: 4px;
    94             cursor: pointer;
    95             transition: all var(--transition-speed);
    96         }
    97
    98         button:hover, select:hover {
    99             background-color: var(--border);
   100             color: white;
   101         }
   102
   103         select {
   104             padding-right: 20px;
   105         }
   106
   107         /* Metadata Card */
   108         .metadata {
   109             background-color: var(--card);
   110             border-left: 5px solid var(--heading);
   111             padding: 20px;
   112             margin-bottom: 25px;
   113             border-radius: 0 8px 8px 0;
   114             box-shadow: 0 2px 8px rgba(0,0,0,0.03);
   115         }
   116
   117         .metadata h1 {
   118             color: var(--heading);
   119             font-size: 2rem;
   120             margin-bottom: 10px;
   121         }
   122
   123         .metadata p {
   124             margin-bottom: 5px;
   125             font-size: 0.95rem;
   126         }
   127
   128         .metadata em {
   129             display: block;
   130             margin-top: 10px;
   131             font-style: italic;
   132             opacity: 0.9;
   133         }
   134
   135         /* Search Interface */
   136         .search-box {
   137             margin-bottom: 25px;
   138         }
   139
   140         .search-input {
   141             width: 100%;
   142             padding: 12px 16px;
   143             font-size: 1rem;
   144             border: 2px solid var(--border);
   145             background-color: var(--card);
   146             color: var(--text);
   147             border-radius: 6px;
   148             outline: none;
   149             font-family: inherit;
   150         }
   151
   152         .search-input:focus {
   153             box-shadow: 0 0 8px rgba(210, 105, 30, 0.4);
   154         }
   155
   156         .no-results {
   157             display: none;
   158             text-align: center;
   159             padding: 30px;
   160             color: var(--heading);
   161             font-weight: bold;
   162             background-color: var(--card);
   163             border-radius: 6px;
   164             border: 1px dashed var(--border);
   165         }
   166
   167         /* Table of Contents (TOC) */
   168         .toc {
   169             background-color: var(--card);
   170             border: 1px solid var(--border);
   171             border-radius: 6px;
   172             padding: 20px;
   173             margin-bottom: 30px;
   174         }
   175
   176         .toc h3 {
   177             color: var(--heading);
   178             margin-bottom: 15px;
   179             border-bottom: 1px solid var(--border);
   180             padding-bottom: 5px;
   181         }
   182
   183         .toc ol {
   184             display: grid;
   185             grid-template-columns: repeat(2, 1fr);
   186             gap: 10px 20px;
   187             padding-left: 20px;
   188         }
   189
   190         .toc li a {
   191             color: var(--link);
   192             text-decoration: none;
   193             transition: underline var(--transition-speed);
   194         }
   195
   196         .toc li a:hover {
   197             text-decoration: underline;
   198         }
   199
   200         /* Verse Blocks (Moola & Vyakhya) */
   201         .verse-block {
   202             background-color: var(--card);
   203             border: 1px solid var(--border);
   204             border-radius: 6px;
   205             margin-bottom: 25px;
   206             overflow: hidden;
   207             box-shadow: 0 2px 6px rgba(0,0,0,0.02);
   208         }
   209
   210         .verse-header {
   211             background-color: var(--bg);
   212             color: var(--heading);
   213             padding: 12px 20px;
   214             margin: 0;
   215             display: flex;
   216             justify-content: space-between;
   217             align-items: center;
   218             cursor: pointer;
   219             border-bottom: 1px solid var(--border);
   220             user-select: none;
   221         }
   222
   223         .toggle-btn {
   224             font-size: 0.85rem;
   225             color: var(--border);
   226             font-family: monospace;
   227             background: none;
   228             border: none;
   229             padding: 4px 8px;
   230         }
   231
   232         .verse-content {
   233             padding: 20px;
   234             display: block; /* Managed by JS */
   235         }
   236
   237         .moola {
   238             background-color: var(--moola-bg);
   239             border-left: 4px solid var(--border);
   240             padding: 15px 20px;
   241             margin-bottom: 15px;
   242             border-radius: 0 4px 4px 0;
   243             font-size: 1.15rem;
   244             font-weight: 500;
   245             text-align: center;
   246         }
   247
   248         .vyakhya {
   249             background-color: var(--vyakhya-bg);
   250             padding: 10px;
   251             border-radius: 4px;
   252         }
   253
   254         .vyakhya p {
   255             margin-bottom: 12px;
   256         }
   257
   258         .vyakhya p:last-child {
   259             margin-bottom: 0;
   260         }
   261
   262         blockquote.quote {
   263             border-left: 3px dashed var(--border);
   264             margin: 15px 0;
   265             padding: 10px 20px;
   266             background-color: var(--bg);
   267             font-style: normal;
   268         }
   269
   270         /* Nested Details */
   271         details {
   272             background-color: var(--bg);
   273             border: 1px solid var(--border);
   274             border-radius: 4px;
   275             margin: 10px 0;
   276             padding: 10px;
   277         }
   278
   279         details summary {
   280             font-weight: bold;
   281             color: var(--heading);
   282             cursor: pointer;
   283             outline: none;
   284             user-select: none;
   285         }
   286
   287         /* Footnotes (Asides) */
   288         .footnotes {
   289             margin-top: 40px;
   290             border-top: 2px solid var(--border);
   291             padding-top: 20px;
   292         }
   293
   294         .footnotes h3 {
   295             color: var(--heading);
   296             margin-bottom: 15px;
   297         }
   298
   299         .footnotes ol {
   300             padding-left: 20px;
   301         }
   302
   303         .footnotes li {
   304             margin-bottom: 8px;
   305             font-size: 0.9rem;
   306         }
   307
   308         .footnotes li:target {
   309             background-color: rgba(210, 105, 30, 0.15);
   310             outline: 1px solid var(--border);
   311             padding: 4px;
   312         }
   313
   314         sup a {
   315             color: var(--link);
   316             text-decoration: none;
   317             font-weight: bold;
   318             padding: 0 2px;
   319         }
   320
   321         /* Colophon & Footer */
   322         .colophon {
   323             text-align: center;
   324             margin: 40px 0 20px 0;
   325             padding: 20px;
   326             border-top: 1px dashed var(--border);
   327         }
   328
   329         .colophon h2 {
   330             color: var(--heading);
   331             margin-bottom: 10px;
   332         }
   333
   334         .footer {
   335             text-align: center;
   336             font-size: 0.8rem;
   337             opacity: 0.8;
   338             padding: 15px;
   339             border-top: 1px solid var(--border);
   340         }
   341
   342         /* Responsive Design Rules */
   343         @media (max-width: 768px) {
   344             .toc ol {
   345                 grid-template-columns: 1fr;
   346             }
   347
   348             .toolbar {
   349                 flex-direction: column;
   350                 gap: 10px;
   351                 padding: 10px;
   352             }
   353
   354             .toolbar-controls {
   355                 width: 100%;
   356                 justify-content: space-around;
   357                 flex-wrap: wrap;
   358                 gap: 5px;
   359             }
   360
   361             button, select {
   362                 padding: 8px 12px; /* Touch target enhancement */
   363                 font-size: 0.85rem;
   364             }
   365         }
   366
   367         /* Advanced Print Stylesheet */
   368         @media print {
   369             .toolbar, .search-box, .toggle-btn, .toc {
   370                 display: none !important;
   371             }
   372
   373             .verse-content {
   374                 display: block !important;
   375             }
   376
   377             body {
   378                 background: white !important;
   379                 color: black !important;
   380                 font-size: 12pt;
   381             }
   382
   383             .container {
   384                 max-width: 100%;
   385                 padding: 0;
   386             }
   387
   388             .verse-block {
   389                 border: none;
   390                 border-bottom: 1px solid #ccc;
   391                 page-break-inside: avoid;
   392             }
   393         }
   394     </style>
   395 </head>
   396 <body data-theme="light">
   397
   398     <!-- Header Navigation Panel -->
   399     <header class="toolbar">
   400         <a href="../index.html" class="toolbar-brand">☰ Sanskrit Library</a>
   401         <div class="toolbar-controls">
   402             <button onclick="toggleAllVerses()" id="toggleAllBtn" aria-label="Expand or Collapse All Blocks">[-] Collapse All</button>
   403             <button onclick="adjustFontSize(-1)" aria-label="Decrease Font Size">A−</button>
   404             <button onclick="adjustFontSize(1)" aria-label="Increase Font Size">A+</button>
   405             <button onclick="toggleTheme()" id="themeBtn" aria-label="Toggle Dark and Light Mode">☾</button>
   406             <select onchange="navigateToChapter(this.value)" aria-label="Select Chapter Navigation">
   407                 <option value="">अध्यायसूची (Chapters) ▾</option>
   408                 <option value="ch-1">अध्यायः १ (Chapter 1)</option>
   409                 <option value="ch-2">अध्यायः २ (Chapter 2)</option>
   410             </select>
   411         </div>
   412     </header>
   413
   414     <main class="container">
   415         <!-- Text Identification Metadata -->
   416         <section class="metadata">
   417             <h1>ग्रन्थनाम (Sanskrit Text Title)</h1>
   418             <p><strong>रचयिता (Author):</strong> श्रीमदाचार्यः (Author Name) | <strong>कालः (Date):</strong> ७मः शताब्दी (Circa 7th Century CE)</p>
   419             <p><strong>प्रकारः (Category):</strong> वेदान्तः (Vedānta) | <strong>भाषा (Language):</strong> संस्कृतम् (Sanskrit)</p>
   420             <em>प्रकृतो ग्रन्थः संस्कृतग्रन्थालयप्रकल्पस्य आदर्शभूतः । (This sample text exemplifies the standard digitization architecture of the Sanskrit Library.)</em>
   421         </section>
   422
   423         <!-- Live Content Filter -->
   424         <section class="search-box">
   425             <input type="text" id="searchInput" class="search-input" placeholder="अन्वेषणं क्रियताम्... (Type to search in Devanāgarī or English...)" onkeyup="filterContent()">
   426         </section>
   427         
   428         <div id="noResults" class="no-results">
   429             फलं न लब्धम् (No matching verses found)
   430         </div>
   431
   432         <!-- Table Of Contents -->
   433         <nav class="toc">
   434             <h3>विषयसूची (Table of Contents)</h3>
   435             <ol>
   436                 <li><a href="#ch-1">अध्यायः १ (Chapter 1)</a></li>
   437                 <li><a href="#ch-2">अध्यायः २ (Chapter 2)</a></li>
   438             </ol>
   439         </nav>
   440
   441         <!-- Main Content Area -->
   442         <article class="content">
   443             
   444             <!-- Chapter/Verse Block 1 -->
   445             <section class="verse-block" id="ch-1">
   446                 <h3 class="verse-header" onclick="toggleSingleVerse('ch-1')">
   447                     १. प्रथमः अध्यायः (Chapter 1)
   448                     <span class="toggle-btn" id="btn-ch-1">[-]</span>
   449                 </h3>
   450                 <div class="verse-content" id="content-ch-1">
   451                     <div class="moola">
   452                         सच्चिदानन्दरूपाय विष्णवे सर्वजिष्णवे ।<br>
   453                         नमो वेदान्तवेद्याय गुरवे बुद्धिसाक्षिणे ॥ १ ॥
   454                     </div>
   455                     <div class="vyakhya">
   456                         <p><strong>व्याख्या (Gloss):</strong> सच्चिदानन्दरूपाय सर्वव्यापिने परमेश्वराय नमः। बुद्धिसाक्षिणे आत्मतत्त्वाय नमः।</p>
   457                         <blockquote class="quote">
   458                             उपनिषत्सु पठ्यते — "तमेव भान्तमनुभाति सर्वं तस्य भासा सर्वमिदं विभाति" इति।<sup><a href="#fn1" id="fnref1">1</a></sup>
   459                         </blockquote>
   460                         <details>
   461                             <summary>पूर्वपक्षचर्चा (Skeptical Arguments)</summary>
   462                             <p>ननु ईश्वरस्य रूपरहितत्वात् कथं सच्चिदानन्दरूपाय इति सङ्घटते? इति चेत्, न; व्यावहारिकदृष्ट्या तस्य सगुणारोपात् इति समाहितम्।</p>
   463                         </details>
   464                     </div>
   465                 </div>
   466             </section>
   467
   468             <!-- Chapter/Verse Block 2 -->
   469             <section class="verse-block" id="ch-2">
   470                 <h3 class="verse-header" onclick="toggleSingleVerse('ch-2')">
   471                     २. द्वितीयः अध्यायः (Chapter 2)
   472                     <span class="toggle-btn" id="btn-ch-2">[-]</span>
   473                 </h3>
   474                 <div class="verse-content" id="content-ch-2">
   475                     <div class="moola">
   476                         अथातो ब्रह्मजिज्ञासा ॥ २ ॥
   477                     </div>
   478                     <div class="vyakhya">
   479                         <p><strong>व्याख्या (Gloss):</strong> अतः साधनचतुष्टयसम्पत्त्यनन्तरं ब्रह्मणो जिज्ञासा कर्तव्या इति सूत्रार्थः।</p>
   480                     </div>
   481                 </div>
   482             </section>
   483
   484         </article>
   485
   486         <!-- Footnotes Section -->
   487         <aside class="footnotes">
   488             <h3>टिप्पण्यः (Footnotes)</h3>
   489             <ol>
   490                 <li id="fn1">
   491                     <a href="#fnref1" aria-label="Back to citation 1">↩</a> कठोपनिषद् २.२.१५ (Kaṭhopaniṣad 2.2.15).
   492                 </li>
   493             </ol>
   494         </aside>
   495
   496         <!-- Closing Colophon -->
   497         div class="colophon">
   498             <h2>॥ इति ग्रन्थः संपूर्णः ॥</h2>
   499             <p>ॐ तत्सत् ब्रह्मार्पणमस्तु।</p>
   500         </div>
   501     </main>
   502
   503     <!-- Project Footer -->
   504     <footer class="footer">
   505         <p>© 2026 Sanskrit Library Project. Shared under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) License.</p>
   506     </footer>
   507
   508     <!-- Scripting Engine -->
   509     <script>
   510         // State Keys for Persistence
   511         const THEME_KEY = 'sanskrit_lib_theme';
   512         const FONT_KEY = 'sanskrit_lib_font_size';
   513
   514         // Initialization Logic
   515         document.addEventListener('DOMContentLoaded', () => {
   516             // Load theme configuration
   517             const savedTheme = localStorage.getItem(THEME_KEY) || 'light';
   518             document.body.setAttribute('data-theme', savedTheme);
   519             document.getElementById('themeBtn').textContent = savedTheme === 'dark' ? '☀' : '☾';
   520
   521             // Load font size configuration
   522             const savedFontSize = localStorage.getItem(FONT_KEY) || '18';
   523             document.documentElement.style.setProperty('--base-font', savedFontSize + 'px');
   524         });
   525
   526         // Toggle Theme Engine
   527         function toggleTheme() {
   528             const currentTheme = document.body.getAttribute('data-theme');
   529             const targetTheme = currentTheme === 'dark' ? 'light' : 'dark';
   530             document.body.setAttribute('data-theme', targetTheme);
   531             localStorage.setItem(THEME_KEY, targetTheme);
   532             document.getElementById('themeBtn').textContent = targetTheme === 'dark' ? '☀' : '☾';
   533         }
   534
   535         // Adjust Font Size (A+ / A-)
   536         function adjustFontSize(delta) {
   537             const root = document.documentElement;
   538             let currentSize = parseFloat(getComputedStyle(root).getPropertyValue('--base-font')) || 18;
   539             currentSize += delta;
   540             
   541             // Visual constraints to protect layouts
   542             if (currentSize < 14) currentSize = 14;
   543             if (currentSize > 28) currentSize = 28;
   544             
   545             root.style.setProperty('--base-font', currentSize + 'px');
   546             localStorage.setItem(FONT_KEY, currentSize.toString());
   547         }
   548
   549         // Single Verse Accordion Toggler
   550         function toggleSingleVerse(blockId) {
   551             const content = document.getElementById(`content-${blockId}`);
   552             const btn = document.getElementById(`btn-${blockId}`);
   553             if (content.style.display === 'none') {
   554                 content.style.display = 'block';
   555                 btn.textContent = '[-]';
   556             } else {
   557                 content.style.display = 'none';
   558                 btn.textContent = '[+]';
   559             }
   560         }
   561
   562         // Master Collapser Button (Expand / Collapse All)
   563         function toggleAllVerses() {
   564             const contents = document.querySelectorAll('.verse-content');
   565             const masterBtn = document.getElementById('toggleAllBtn');
   566             const isCurrentlyCollapsed = contents[0] && contents[0].style.display === 'none';
   567
   568             contents.forEach(content => {
   569                 content.style.display = isCurrentlyCollapsed ? 'block' : 'none';
   570             });
   571
   572             document.querySelectorAll('.toggle-btn').forEach(btn => {
   573                 btn.textContent = isCurrentlyCollapsed ? '[-]' : '[+]';
   574             });
   575
   576             masterBtn.textContent = isCurrentlyCollapsed ? '[-] Collapse All' : '[+] Expand All';
   577         }
   578
   579         // Dropdown Selection Smooth Navigation
   580         function navigateToChapter(targetId) {
   581             if (targetId) {
   582                 const element = document.getElementById(targetId);
   583                 if (element) {
   584                     element.scrollIntoView({
   585                         behavior: 'smooth',
   586                         block: 'start'
   587                     });
   588                     
   589                     // Automatically expand target block if collapsed
   590                     const content = document.getElementById(`content-${targetId}`);
   591                     const btn = document.getElementById(`btn-${targetId}`);
   592                     if (content && content.style.display === 'none') {
   593                         content.style.display = 'block';
   594                         if (btn) btn.textContent = '[-]';
   595                     }
   596                 }
   597             }
   598         }
   599
   600         // Real-time Text Filter Engine (Supports Latin and Devanāgarī search)
   601         function filterContent() {
   602             const query = document.getElementById('searchInput').value.toLowerCase().trim();
   603             const blocks = document.querySelectorAll('.verse-block');
   604             const noResultsEl = document.getElementById('noResults');
   605             let matchedCount = 0;
   606
   607             blocks.forEach(block => {
   608                 const textContent = block.textContent.toLowerCase();
   609                 if (textContent.includes(query)) {
   610                     block.style.display = 'block';
   611                     matchedCount++;
   612                     
   613                     // Auto-expand matches for user visibility during searches
   614                     const content = block.querySelector('.verse-content');
   615                     const btn = block.querySelector('.toggle-btn');
   616                     if (query.length > 0 && content) {
   617                         content.style.display = 'block';
   618                         if (btn) btn.textContent = '[-]';
   619                     }
   620                 } else {
   621                     block.style.display = 'none';
   622                 }
   623             });
   624
   625             // Handle Empty Search Results State
   626             if (matchedCount === 0 && query.length > 0) {
   627                 noResultsEl.style.display = 'block';
   628             } else {
   629                 noResultsEl.style.display = 'none';
   630             }
   631         }
   632     </script>
   633 </body>
   634 </html>

  ---

  5. Critical Technical Enhancements Explained

  5.1 LocalStorage State Persistence (New Feature)
  Unlike static documents that reset their configurations on page reload, this template uses the browser's native window-scoped storage system:
   * The Problem: Users reading long-form text are highly sensitive to screen luminosity and text size. Forcing them to repeatedly click "☾" or "A+" on page navigation degrades the experience.
   * The Solution: On page load, immediate script execution reads key values from local storage. The data-theme and font variables are injected prior to full document rendering, preventing flashes of light theme or layout shifting during
     critical render pipelines.

  5.2 Responsive Layout Logic (Media Queries)
  Mobile screens possess a restrictive visual boundary. The layout handles transitions across device scales without generating breaking points or horizontal scroll glitches:
   * Desktop Viewports (> 768px): Structural cards utilize generous 20px margins. The Table of Contents is structured inside an active CSS Grid with parallel columns to limit visual page height.
   * Mobile Viewports (≤ 768px): The sticky header stacks vertically to ensure brand lines do not collide with navigation buttons. Touch targets are scaled outward (padding: 8px 12px minimum) to comfortably fit finger tap boundaries, and
     table lists wrap naturally into single columns.

  5.3 Advanced Printer Adaptation CSS
  Academic texts are often printed for review or physical filing. The custom print rules guarantee perfect black-and-white output:
   * Hides interactive elements completely (.toolbar, .search-box, .toggle-btn) using display: none !important.
   * Forces background overrides to absolute white and body text to true black for maximum ink savings.
   * Enforces structural break limits via page-break-inside: avoid on the .verse-block container, ensuring chapters do not cleanly bifurcate across sheet edges.

  ---

  6. Content Integration Pattern Guide

  6.1 Moola (Root) + Vyākhyā (Commentary) Tier
  For traditional critical editions containing original verse strings alongside multi-tiered textual annotations, structure content exactly as shown below:

    1 <section class="verse-block" id="verse-1.1">
    2     <h3 class="verse-header" onclick="toggleSingleVerse('verse-1.1')">
    3         मङ्गलश्लोकः (Verse 1.1)
    4         <span class="toggle-btn" id="btn-verse-1.1">[-]</span>
    5     </h3>
    6     <div class="verse-content" id="content-verse-1.1">
    7         <!-- The Original Devanāgarī root text -->
    8         <div class="moola">
    9             नारायणं नमस्कृत्य नरं चैव नरोत्तमम् ।<br>
   10             देवीं सरस्वतीं व्यासं ततो जयमुदीरयेत् ॥ १.१ ॥
   11         </div>
   12         <!-- Comprehensive textual commentary division -->
   13         <div class="vyakhya">
   14             <p><strong>भाष्यम् (Primary Gloss):</strong> नारायणं जगत्प्रभवं देवं नमस्कृत्य...</p>
   15             <blockquote class="quote">
   16                 <strong>प्रमाणम् (Supporting Citation):</strong> "नारायणः परोऽव्यक्तात्" इति श्रुतिसिद्धान्तः।
   17             </blockquote>
   18             <p><strong>टीका (Sub-Commentary glosses):</strong> अस्मिन् श्लोके 'जय' शब्देन महाभारताभिधानो ग्रन्थ उच्यते।</p>
   19         </div>
   20     </div>
   21 </section>

  6.2 Footnote Bidirectional Navigation
  Footnotes require immediate return structures to allow scholars to traverse back and forth without losing their visual anchors.

   * Anchor Reference In Content:

   1   उपनिषत्सु पठ्यते<sup><a href="#fn1" id="fnref1">1</a></sup>
   * Footnote Definition block:

   1   <li id="fn1">
   2       <a href="#fnref1" aria-label="Back to citation 1">↩</a> कठोपनिषद् २.२.१५
   3   </li>
   * Visual Aid: When a user navigates to a footnote, the CSS selector target rule activates. It provides an elegant focus highlight to draw the eye directly to the note:

   1   .footnotes li:target {
   2       background-color: rgba(210, 105, 30, 0.15);
   3       outline: 1px solid var(--border);
   4   }

  ---

  7. Developer Lifecycle & Quality Assurance Checklist

  Prior to publishing a text file generated from this template, run this rigorous validation checklist:

   - [ ] Document Language Tag: Verify that <html lang="sa"> is set correctly for screen reader parsing.
   - [ ] Title Tags: Ensure the <title> matches the correct localized text name.
   - [ ] Unique Block Identifiers: Check that every <section class="verse-block"> possesses a unique, lowercase, alphanumeric ID (e.g., id="ch-1", id="ch-2").
   - [ ] Dual Dropdown Select Matching: Confirm that the select options in <header class="toolbar"> match the block IDs exactly:

   1   <option value="ch-1">Chapter 1</option> --> <section class="verse-block" id="ch-1">
   - [ ] Interactive ID Alignment: Ensure the toggleSingleVerse('id') function matches the IDs of both the target content block and its toggle button:
     * Section ID: id="ch-1"
     * Content Block ID: id="content-ch-1"
     * Toggle Button ID: id="btn-ch-1"
   - [ ] Theme Selector Contrast Validation: Verify that color schemes pass a minimum WCAG 2.1 AA contrast check (minimum 4.5:1 ratio between text colors and card backgrounds) in both light and dark states.
   - [ ] Offline File Portability Test: Double-click the saved .html file locally while disconnected from all networks to verify that formatting, icons, rendering, and search systems function perfectly.
