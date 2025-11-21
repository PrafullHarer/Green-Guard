# QR Generator (React + Vite)

Generate and download QR codes instantly.

## Overview

This is a small Vite + React project focused on providing a fast QR-code
creation experience. It supports instant previews, responsive layout, and
client-side downloads so no data ever leaves the browser.

## Getting Started

1. **Install dependencies**

   ```
   npm install
   ```

2. **Run the dev server**

   ```
   npm run dev
   ```

3. Open the printed local URL (defaults to `http://localhost:5173`) in your
   browser.

## Configuration

- Update `src/components/QRCodeGenerator.jsx` if you want to tweak default size,
  padding, or color values.
- Styles live in `src/styles/qr.css` and `src/App.css`. Adjust them for branding
  or layout changes.
- Asset imports (logos, icons) can be placed inside `src/assets/`.

## Tech Stack

- React 18 with hooks and functional components
- Vite for bundling and fast HMR
- `qrcode.react` for rendering the QR canvas
- Vanilla CSS modules for styling

## Scripts

- `npm run dev`: start the dev server
- `npm run build`: production build
- `npm run preview`: preview the build locally

## Project Structure

```
src/
  components/
    QRCodeGenerator.jsx
  hooks/
    useDebouncedValue.js
  pages/
    Home.jsx
  styles/
    qr.css
  utils/
    download.js
  App.jsx
  main.jsx
  index.css
```

## Features

- Enter any text or URL
- Choose size (64–1024)
- Download PNG
- Debounced input to avoid unnecessary renders
- Keyboard-friendly controls and accessible labels

## Testing & Linting

- `npm run build`: quick way to ensure the project still compiles
- `npm run lint`: run ESLint checks (configured via `eslint.config.js`)

## Dependencies

- `qrcode.react`

## Roadmap Ideas

- Theming support (light/dark or custom palettes)
- Bulk QR generation from CSV uploads
- SVG export option alongside PNG
- Shareable URLs that encode QR settings for easy collaboration
