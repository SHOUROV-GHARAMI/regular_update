# CSS Color Cheat Sheet

A concise Markdown cheat-sheet with common CSS color formats, examples, and short usage snippets.

---

## Quick summary
- Named colors (keywords)
- Hex colors (#RGB, #RRGGBB, #RGBA, #RRGGBBAA)
- rgb() / rgba() and modern space/slash syntax
- hsl() / hsla() and modern space/slash syntax
- CSS custom properties (variables)
- Useful keywords: `transparent`, `currentColor`, `inherit`

---

## Named colors (keywords)
Common keywords supported by all browsers. Use these for readability or quick prototypes.

Examples:
- `black`, `white`, `red`, `blue`, `green`, `yellow`, `orange`, `purple`, `pink`, `brown`, `gray`, `silver`, `maroon`, `navy`, `olive`, `teal`, `lime`, `fuchsia`, `coral`, `gold`, `tomato`, `skyblue`

Usage:

```css
/* CSS */
.color-name { color: tomato; }
.bg-name { background-color: skyblue; }
```

---

## Hex colors
- 3-digit shorthand: `#f00`, `#0f0`, `#00f`, `#000` (equivalent to `#ff0000`, etc.)
- 6-digit: `#ff0000`, `#00ff00`, `#0000ff`, `#abcdef`, `#123456`
- 4-digit (shorthand with alpha): `#f008` (interpreted as `#ff000088`)
- 8-digit (with alpha): `#ff000080` (50% opaque red)

Usage:

```css
.hex { color: #1e90ff; }
.hex-alpha { background-color: #ff000080; }
```

---

## rgb() / rgba() and modern syntax
- Traditional: `rgb(255, 0, 0)`, `rgba(255, 0, 0, 0.5)`
- Modern (space-separated + slash for alpha): `rgb(255 0 0 / 0.5)`
- Percent variants: `rgb(100% 0% 0%)`

Usage:

```css
.rgb { color: rgb(34, 139, 34); }
.rgba { background: rgba(0, 0, 0, 0.6); }
.modern-rgb { background: rgb(255 165 0 / 0.4); }
```

---

## hsl() / hsla() and modern syntax
- `hsl(hue, saturation%, lightness%)` — hue is 0–360
- `hsla(hue, sat%, light%, alpha)` or `hsl(hue sat% light% / alpha)`

Examples:
- `hsl(0, 100%, 50%)` — red
- `hsl(120, 100%, 25%)` — dark green
- `hsl(240 100% 50% / 0.25)` — translucent blue

Usage:

```css
.hsl { color: hsl(200, 80%, 40%); }
.hsla { background: hsl(200 80% 40% / 0.2); }
```

HSL is handy for programmatic color adjustments (lighter/darker by adjusting lightness).

---

## CSS custom properties (variables)
Define colors once and reuse them.

```css
:root {
  --brand: #1e90ff;
  --accent: hsl(340 80% 60%);
  --overlay: rgb(0 0 0 / 0.5);
}
.btn { background: var(--brand); color: white; }
.overlay { background: var(--overlay); }
```

---

## Useful keywords
- `transparent` — fully transparent color
- `currentColor` — uses the element's `color` value (useful for borders/icons)
- `inherit`, `initial`, `unset` — standard cascade/initialization keywords

Examples:

```css
.border { border-color: currentColor; }
.faded { background: transparent; }
```

---

## Small HTML demo snippet (paste into an HTML file to see examples)

```html
<div style="font-family: sans-serif; padding: 12px; max-width:520px;">
  <h2>Color examples</h2>
  <div style="background:#1e90ff;color:#fff;padding:8px;margin:6px 0;">Hex: #1e90ff</div>
  <div style="background:rgb(255,165,0);color:#000;padding:8px;margin:6px 0;">RGB: rgb(255,165,0)</div>
  <div style="background:rgba(0,0,0,0.6);color:#fff;padding:8px;margin:6px 0;">RGBA: rgba(0,0,0,0.6)</div>
  <div style="background:hsl(200 80% 40%);color:#fff;padding:8px;margin:6px 0;">HSL: hsl(200 80% 40%)</div>
  <div style="background:tomato;color:#fff;padding:8px;margin:6px 0;">Named color: tomato</div>
</div>
```

---

## Quick reference table (short)
- Named: `red`, `tomato`, `dodgerblue`, `gold`
- Hex: `#f00`, `#ff0000`, `#00ff00`, `#0000ff`, `#abcdef`
- RGB/RGBA: `rgb(255,0,0)`, `rgba(255,0,0,0.5)`
- HSL/HSLA: `hsl(0,100%,50%)`, `hsl(0 100% 50% / 0.5)`
- Variables: `--name: #123456; color: var(--name);`

---

## Notes & tips
- Prefer HSL when you need to shift hue/lightness/saturation programmatically.
- Use CSS variables for themeability and easier maintenance.
- Use named colors for readability in small projects; prefer hex/HSL/RGB for precise control.
- For semi-transparency, prefer the modern `rgb()/hsl()` with alpha or 8-digit hex if you need exact alpha in hex.

---

_File created: colors-cheatsheet.md — placed next to your `index.html` in the CSS folder._

If you want, I can also:
- Add a rendered HTML demo file (`colors-demo.html`) showing swatches and copy buttons.
- Insert the demo into your `index.html`.
- Expand the cheat-sheet with a full list of all 140+ CSS named colors.
