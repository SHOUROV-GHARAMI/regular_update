# CSS Methods Used in `css-methods-demo.html`

This document explains the CSS methods demonstrated in `css-methods-demo.html` and where they appear.

Files created/updated
- `css-methods-demo.html` — demo page (uses Inline, Internal, and External CSS).
- `mystyle.css` — external stylesheet (updated with many examples).

## Methods demonstrated

1) Inline CSS
- What: CSS applied directly on an element using the `style` attribute.
- Example in page: `<p style="color:teal;font-weight:600;">` and the inline-styled button.
- Use-case: quick one-off overrides or generated styles; low specificity (but higher than user-agent default).

2) Internal CSS
- What: CSS placed inside a `<style>` block in the page `<head>`.
- Example in page: `.internal-note` and `.internal-badge` defined in the head.
- Use-case: page-specific styles without a separate file.

3) External CSS
- What: CSS in a separate file (here `mystyle.css`) linked with `<link rel="stylesheet" href="mystyle.css">`.
- Example in page: the majority of styles (IDs, classes, pseudo-classes, positioning, etc.).
- Use-case: reusable styles shared across pages; cached by browser.

4) Selectors
- Tag selector: `p { ... }` — affects all paragraphs. (see `mystyle.css`)
- Class selector: `.box`, `.badge`, `.demo-btn`, etc. — used widely in the demo.
- ID selector: `#hero` — styled in `mystyle.css` and used on the hero section.
- Attribute selector: `a[target="_blank"] { ... }` — styles links that open in a new tab.
- Descendant selector: `.card p { ... }` — targets `p` inside `.card`.
- Child selector: `.parent > .child { ... }` — targets direct children only.
- Pseudo-classes: `:hover` for `button.demo-btn:hover` (hover effect).
- Pseudo-elements: `.badge::after { content: " ★"; }` adds decorative content.
- Structural pseudo-class: `ul.demo-list li:nth-child(odd)` and `nth-child(even)`.

5) Properties (examples used)
- Colors: `color`, `background`, `background-image`.
- Fonts: `font-family`, `font-size`, `font-weight`, `font-style`.
- Text styling: `text-transform`, `text-decoration`, `letter-spacing`.
- Box model: `width`, `padding`, `border`, `margin` (see `.box-model`).
- Background images: `.hero-bg` uses a background image and `background-size: cover`.

6) Positioning
- `position: relative` — `.pos-relative` shows offset from normal flow.
- `position: absolute` — `.pos-absolute` positioned relative to its positioned ancestor.
- `position: fixed` — `.pos-fixed` attached to the viewport (see bottom-right fixed box).
- `position: sticky` — `.pos-sticky` sticks to the top when scrolling.

7) Display & Visibility
- `display: none` (class `.hidden`) hides an element entirely.
- `display: block` and other display modes controlled via classes and tag defaults.

8) Media Query (responsive)
- `@media (max-width:600px)` demonstrates a responsive tweak for small screens.

9) CSS Custom Properties (Variables)
- `:root { --brand: #1e90ff; --accent: ... }` used across the stylesheet.

## How to view the demo
1. Open `css-methods-demo.html` in a browser (double-click or open from editor).
2. Inspect elements using DevTools to see which rule comes from Inline, Internal, or External CSS.

## Notes on specificity & cascade
- Inline styles have the highest specificity of the three methods shown (except `!important`).
- Internal and external styles follow normal cascade and specificity rules; the last declared rule wins when specificity is equal.

## Suggested next steps
- Expand the demo with interactive toggles to show/hide styles (JS) so learners can toggle inline vs external rules.
- Add comments in `mystyle.css` pointing to which demo element each block targets for quicker learning.

---

_File generated alongside the demo — feel free to request any clarifications or additions._

---

## Code examples (copyable)

Below are minimal, copyable examples that map to the demo so you can try them individually.

### Tag selector
```html
<p>This paragraph is styled by a tag selector.</p>
```
```css
p { color: #222; }
```

### Class selector
```html
<div class="box">Box using a class selector</div>
```
```css
.box { padding: 12px; border: 1px solid #ddd; }
```

### ID selector
```html
<section id="hero">Hero area</section>
```
```css
#hero { background: var(--brand); color: white; }
```

### Attribute selector
```html
<a href="https://example.com" target="_blank">Open in new tab</a>
```
```css
a[target="_blank"] { text-decoration: underline; }
```

### Child vs Descendant selector
```html
<div class="parent">
	<div class="child">Direct child</div>
	<div>
		<div class="child">Descendant (not a direct child of .parent)</div>
	</div>
</div>
```
```css
.parent > .child { background: brown; }
.parent .child { border: 1px solid #ccc; }
```

### Pseudo-class (hover) and pseudo-element (::after)
```html
<button class="demo-btn">Hover me</button>
<p class="badge">Badge</p>
```
```css
button.demo-btn:hover { background: darkblue; }
.badge::after { content: ' ★'; color: gold; }
```

### nth-child example
```html
<ul class="demo-list">
	<li>One</li>
	<li>Two</li>
	<li>Three</li>
</ul>
```
```css
ul.demo-list li:nth-child(odd) { background: #f6f8fa; }
ul.demo-list li:nth-child(even) { background: #eef2ff; }
```

## Printable cheat-sheet (short)

- Named colors: `red`, `tomato`, `dodgerblue`
- Hex: `#f00`, `#ff0000`, `#123456`
- RGB(A): `rgb(255,0,0)`, `rgba(255,0,0,0.5)`
- HSL(A): `hsl(120,100%,50%)`, `hsl(120 100% 50% / 0.5)`
- Variables: `:root { --brand: #1e90ff }` then `color: var(--brand)`
- Display / Visibility: `display: none`, `visibility: hidden`
- Positioning: `static`, `relative`, `absolute`, `fixed`, `sticky`

## Where to look in the project
- `index.html` — the integrated demo (entry page)
- `mystyle.css` — external stylesheet with comments linking blocks to demo elements
- `css-methods-demo.html` — an alternate demo page (kept for reference)

If you'd like, I can also generate a printable PDF of this cheat-sheet or add interactive toggles so each rule can be enabled/disabled live on the page.
