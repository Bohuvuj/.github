---
title: Open Graph badge generator tools/og.py and og outputs
author: Redwan002117
date: 2026-11-12
branch: main
id: l-1caed848
scope: repo
status: active
src: agent
touches:
  - tools/og.py
  - og/bohuvuj.svg
---

## Decided
tools/og.py builds product Open Graph SVG and PNG cards under og/ for autletto, beeezee, bohupay, bohuvuj, collectra, messmanager, perfumevault, and subash using tools/src/bohuvuj-logo.b64.

## Tried and ruled out
Maintaining hand-edited PNGs without matching SVG sources.

## Watch out
Keep PNG and SVG pairs in og/ regenerated together via tools/og.py so product OG previews stay consistent across repos.
