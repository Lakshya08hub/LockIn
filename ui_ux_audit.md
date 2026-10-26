# UI/UX Audit — LockIn Prototype

> Audit of the original bare Streamlit prototype (`app.py`), conducted before the startup-style redesign (`web/`). Kept as a record of what was wrong and why, for the project write-up/demo narrative ("here's what we started with, here's what we fixed and why").

## 50 Issues

| # | Issue | Location | Severity | Suggested Fix | Status |
|---|---|---|---|---|---|
| 1 | No product name, logo, or wordmark anywhere | Whole app | High | Brand it — add name + logo in header | Fixed — "VidyaPulse" brand + logo across `web/` |
| 2 | Title is a generic emoji + description, reads as a tool not a product | Top of page | High | Replace with a real hero/header section | Fixed — `index.html` hero |
| 3 | Default Streamlit light theme, no custom color palette | Whole app | High | Define a brand palette, apply via theme/CSS | Fixed — `shared.css` tokens |
| 4 | No landing/marketing page — app opens straight into the tool | Entry point | High | Add a landing page before the app | Fixed — `index.html` |
| 5 | No navigation bar / way to get back to "home" | Whole app | High | Add persistent top nav | Fixed — `components.js` nav |
| 6 | No login/signup — anyone can use it, no concept of "account" | Whole app | High | Add auth screens (even if mocked) | Fixed — `signup.html` |
| 7 | No pricing or monetization surface | Whole app | High | Add a Pricing page | Fixed — `pricing.html` |
| 8 | "Model comparison" table is the first thing shown — exposes internals before value | Top of page | Medium | Move technical details behind a collapsed/advanced section | Fixed — kept as collapsed expander in `app.py`; hidden entirely from `web/` UX |
| 9 | Raw metric names like `f1`, `roc_auc` shown to end users | Model comparison expander | Medium | Translate to plain-language labels | Open — still raw in `app.py`; not surfaced in `web/` |
| 10 | Radio button for "input mode" looks like a form control, not a product choice | Below title | Medium | Redesign as two clear tabs/cards | Open (Streamlit-side); superseded in `web/` by roster table |
| 11 | "Pick an existing student by ID" exposes raw database browsing | Input mode | High | Replace with a searchable student list/table | Fixed — `dashboard.html` roster + search box |
| 12 | Numeric ID input has no context (no name, no class/cohort) | Student picker | Medium | Show student name, photo placeholder, cohort | Fixed — `report.html` header |
| 13 | 20+ sliders dumped in 3 plain columns for manual entry | Manual entry form | High | Break into multi-step wizard or grouped accordion | Open — `app.py` unchanged; out of scope for `web/` showcase |
| 14 | No labels explaining units clearly | Manual entry sliders | Medium | Add helper text/tooltips per field | Open |
| 15 | Checkboxes for binary fields have no grouping/visual hierarchy | Manual entry | Low | Group into a "Student background" card | Open |
| 16 | No validation feedback (e.g., units_passed > units_enrolled) | Manual entry | Medium | Add inline validation | Open |
| 17 | "Actual recorded outcome" shown as a spoiler before prediction | Student picker | Medium | Hide ground truth until after prediction | Open (Streamlit app); not present in `web/` mockup |
| 18 | Model selector dropdown is a raw technical choice exposed to end users | Below inputs | Medium | Hide behind "Advanced settings"; auto-pick best model | Open |
| 19 | Risk shown only as a percentage + red/green text — no visual gauge/chart | Results | High | Add a risk gauge/meter visualization | Fixed — `report.html` SVG gauge |
| 20 | Binary "HIGH RISK"/"LOW RISK" label with no middle tier | Results | Medium | Add Low/Medium/High bands | Fixed — `dashboard.html`/`report.html` 3-tier badges |
| 21 | No explanation of *why* risk is high | Results | High | Add a short "key drivers" explanation | Fixed — `report.html` "Why this student is flagged" |
| 22 | Weak-area list shows raw z-score numbers to end users | Weak area section | High | Hide raw scores; show plain-language severity | Fixed — `report.html` progress bars instead of numbers |
| 23 | No icons/visual distinction between the four weak-area domains | Weak area section | Medium | Add an icon per domain | Fixed — emoji icons per domain |
| 24 | Recommendations rendered as plain bullet markdown | Recommendations | Medium | Style as actionable cards with icons/CTAs | Fixed — `report.html` recommendation cards |
| 25 | No "mark as done" / tracking for recommendations | Recommendations | Low | Add checkboxes/progress tracking | Fixed (UI only) — "Mark as assigned" buttons |
| 26 | No empty/loading states designed | Whole app | Low | Add branded loading and empty states | Open |
| 27 | No error handling UI for invalid inputs | Student picker | Medium | Add a friendly error message/illustration | Open |
| 28 | No mobile responsiveness considered | Whole app | High | Design mobile-first layouts for new pages | Fixed — `web/` uses responsive Tailwind grid/breakpoints |
| 29 | No dark mode support | Whole app | Low | Add theme toggle | Partial — toggle UI present in `settings.html`, not wired |
| 30 | No accessibility labels (aria-labels, contrast) verified | Whole app | Medium | Run an accessibility pass | Open |
| 31 | Font is default Streamlit sans — no distinct typographic identity | Whole app | Low | Pick a brand typeface | Fixed — Inter via Google Fonts |
| 32 | No whitespace rhythm — sections butt up against each other | Whole app | Medium | Add consistent vertical spacing | Fixed — `web/` section padding |
| 33 | No testimonials, social proof, or credibility markers | Whole app | High | Add testimonials/logos section | Fixed — `index.html` logos + testimonial |
| 34 | No call-to-action anywhere | Whole app | High | Add clear CTAs throughout | Fixed — CTAs on every `web/` page |
| 35 | No footer (contact, terms, privacy, social links) | Whole app | Medium | Add a standard footer | Fixed — `components.js` footer |
| 36 | "Domain definitions" expander uses raw column names | Bottom expander | Medium | Translate to human-readable descriptions | Open (Streamlit app) |
| 37 | No way to export/share a student's report | Results | Medium | Add "Export report" / "Share" action | Fixed (UI only) — `report.html` buttons |
| 38 | No multi-student/batch view | Whole app | Medium | Add a cohort/class-level dashboard view | Fixed — `dashboard.html` |
| 39 | No trend-over-time view | Results | Medium | Add a simple trend chart | Fixed — `dashboard.html` GPA trend column |
| 40 | No onboarding/empty state explaining what the tool does | Entry point | High | Add a short onboarding walkthrough | Fixed — `index.html` how-it-works section |
| 41 | No visual distinction between "input" and "output" sections | Whole page | Medium | Use clear section containers/cards | Fixed — card-based layout throughout `web/` |
| 42 | No settings/profile page | Whole app | Low | Add a Settings screen | Fixed — `settings.html` |
| 43 | No favicon/browser tab branding | Browser tab | Low | Add custom favicon + page title | Fixed — inline SVG favicon on every `web/` page |
| 44 | No currency/market localization anywhere | N/A | High | Add INR pricing throughout commercial pages | Fixed — ₹ pricing on `pricing.html`/`checkout.html` |
| 45 | No visual risk history for a student | Results | Medium | Add a mini sparkline of risk over semesters | Open — flagged for future iteration |
| 46 | Long form in manual-entry mode has no progress indicator | Manual entry | Medium | Add a stepper/progress bar | Open |
| 47 | No distinction between "Admin/Institution view" and "Student/Parent view" | Whole app | Medium | Add role-based views | Fixed (UI only) — role selector in `signup.html` |
| 48 | Recommendations don't link to any actual resource | Recommendations | Medium | Add clickable resource links/buttons | Open — placeholder buttons only |
| 49 | No confirmation/success state after any action | Whole app | Low | Add toast/success states | Fixed — `checkout.html` payment success state |
| 50 | Overall visual tone reads as an internal analytics tool, not a product | Whole app | High | Full visual redesign | Fixed — `web/` full redesign |

## Summary
- **Fixed in `web/` redesign:** 32 of 50 issues (mostly High severity — branding, navigation, monetization, visual hierarchy, trust signals).
- **Still open (Streamlit `app.py` internals):** 16 issues — largely form-UX refinements (multi-step wizard, validation, tooltips) that matter once the raw ML tool is the primary interface rather than the Streamlit instance being wrapped by the `web/` front-end.
- **Partial:** 2 issues (dark mode toggle present but not wired; most recommendation CTAs are UI-only placeholders).

See `web/` for the implemented redesign and `README.md` for the full project structure.
