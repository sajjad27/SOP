# SOP Guide Studio

**SOP Guide Studio** is an interactive web-based solution for creating, editing, and navigating **Standard Operating Procedures (SOPs)**.  
It’s designed as a lightweight **HTML/JS application** that works entirely offline – perfect for teams that need a self-contained, portable SOP builder and viewer.

---

## ✨ Features

- **Landing Page**
  - Title & description with toggle between **Preview** and **Edit**.
  - Dirty-state detection with confirmation modal (never lose unsaved changes).
  - List of SOP “starters” as clickable cards.

- **Starter View**
  - Preview mode → clean stepper view of all SOP steps.
  - Edit mode → full studio with metadata, steps, and interactive **map/graph**.
  - One global toggle for switching between **View** and **Edit** modes.

- **Step Management**
  - View steps in a wizard-like flow.
  - Edit steps, reorder, and visualize relationships.
  - Graph/Map rendering for complex SOP flows.

- **State Management**
  - No external frameworks — all handled with `screen="..."` and `data-mode="..."` attributes on `<html>`.
  - Clear separation of concerns:
    - `screen="landing"` → Landing page.
    - `screen="starter"` → Starter viewer/editor.
    - `data-mode="view"` / `data-mode="edit"` → switch between preview and editing.

- **Offline & Portable**
  - Pure HTML, CSS, and vanilla JavaScript.
  - No build step required — just open the file in your browser.

---

## 🖼️ Screens

- **Landing (View)** – clean overview with title, description, and SOP cards.
- **Landing (Edit)** – edit title/description with live inputs and Save/Cancel.
- **Starter (View)** – stepper wizard for walking through the SOP.
- **Starter (Edit)** – studio view with metadata, steps editor, and process map.

---

## 🚀 Usage

1. Clone or download the repo.
2. Open `sop_guide_stodio.html` in your browser.
3. Use the **Edit / View toggle** to switch modes.
4. Click a card:
   - In **View mode** → open the stepper viewer.
   - In **Edit mode** → open the SOP editor with the interactive map.

---

## 📂 Project Structure

- `sop_guide_stodio.html` – main HTML file, includes all logic.
- `README.md` – you’re reading it.
- (Optional) future separation of CSS/JS if you want modularity.

---

## 🛠️ Customization

- Adapt the CSS theme with `--fg`, `--bg`, and `--accent` variables.
- Extend the starter editor with new fields (owner, tags, attachments).
- Integrate with storage backends (localStorage, API, etc.) if needed.

---

> SOP Guide Studio helps you **bridge the gap between documentation and execution** — keeping your processes clear, editable, and always in sync.
