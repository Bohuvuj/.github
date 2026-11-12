---
title: Org profile animated SVG asset generator tools/build.py
author: Redwan002117
date: 2026-11-12
branch: main
id: l-b70c7c21
scope: repo
status: active
src: agent
touches:
  - tools/build.py
  - profile/README.md
---

## Decided
tools/build.py renders profile/assets/*-{dark,light}.svg with dark/light THEMES palettes, hex grid pattern, blurred glow blobs, inline Lucide SVG icons from tools/src/icons/*.svg, and prefers-reduced-motion media query.

## Tried and ruled out
Using external JS or web fonts in GitHub README SVGs because GitHub camo image proxy strips scripts and external font requests.

## Watch out
Re-run python tools/build.py after editing copy or card metadata; never commit secrets or customer metrics to public profile assets.
