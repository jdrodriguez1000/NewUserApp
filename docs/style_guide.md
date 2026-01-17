# Style Guide - NewUserApp

This document outlines the visual identity and design system for the application, inspired by the modern, premium health-dashboard aesthetic provided in the reference.

## Visual Identity Overview

The design follows a **Clean, Card-based, and Information-Dense** approach with a focus on high-readability and vibrant accents against neutral backgrounds.

## Color Palette

### Base Colors
| Role | Color | Hex | Sample |
| :--- | :--- | :--- | :--- |
| **Background (Light)** | Off-White | `#F5F7FA` | |
| **Background (Dark)** | Charcoal | `#1A1C1E` | |
| **Surface/Cards** | White | `#FFFFFF` | |
| **Text (Primary)** | Deep Black | `#000000` | |
| **Text (Secondary)** | Slate Gray | `#71717A` | |

### Accent Colors (Dashboard/Health)
| Category | Color | Hex Range | Usage |
| :--- | :--- | :--- | :--- |
| **Primary/Progress** | Electric Blue | `#4A90E2` to `#357ABD` | Progress bars, Main CTAs |
| **Carbs** | Vibrant Orange | `#F5A623` | Nutrition charts |
| **Fat** | Leaf Green | `#7ED321` | Nutrition charts |
| **Protein** | Royal Blue | `#4A90E2` | Nutrition charts |
| **Calories/Action** | Soft Black | `#2D2D2D` | Buttons, Dark surfaces |

---

## Typography

**Primary Font Family**: `Inter`, `Roboto`, or system-sans-serif.

### Type Scale
- **H1 (Header)**: `24px` / Bold / `#000000`
- **H2 (Sub-header)**: `18px` / Semi-bold / `#2D2D2D`
- **Body**: `14px` / Regular / `#71717A`
- **Caption/Small**: `12px` / Medium / `#A1A1AA`

---

## UI Components & Design Patterns

### 1. Cards (The "Container" Pattern)
- **Border Radius**: `24px`
- **Shadow**: `0 4px 20px rgba(0, 0, 0, 0.05)`
- **Padding**: Large (`24px`) for content separation.

### 2. Buttons
- **Primary Pill**: Rounded corners (`50px`), high contrast (Dark background with White text).
- **Secondary**: Glassmorphism effect or subtle borders.
- **Icon Buttons**: Circle containers with subtle shadows.

### 3. Data Visualization
- **Progress Arcs**: Thick strokes, rounded ends, using the Blue gradient.
- **Bar Charts**: Rounded tops, segmented for stacked data (Nutrition percentages).
- **Micro-interactions**: Subtle hover state lifting (shadow increase) for cards.

### 4. Layout
- **Mobile First**: Single column stack with generous vertical spacing (`24px` to `32px`).
- **Grouping**: Logical sections titled "Today's Activity" or "Nutrition" with clear "See All" triggers.

---

## Interaction Design
- **Transitions**: Smooth HSL-based color shifts on hover.
- **Glassmorphism**: Use `backdrop-filter: blur(10px)` for overlays and popups to maintain context.
