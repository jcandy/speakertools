# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Speakertools is the documentation repository for [Speakerbench](https://speakerbench.com), a loudspeaker simulation and analysis platform. It contains:
- Sphinx documentation sources in `src/` (reStructuredText)
- Built HTML documentation synced to `doc/`

Development tools (Python utilities, circuit diagram sources) live in the separate private repo `~/GITLAB/speakerdev`.

## Commands

```bash
make          # Build HTML docs into src/_build/html
make sync     # Copy built HTML to doc/ (for publishing)
make clean    # Remove src/_build contents
make distclean  # clean + remove doc/
```

### Setup
```bash
pip install -r requirements.txt
```

## Architecture

### Sphinx Documentation (`src/`)
- `conf.py` — Sphinx config; loads math macros from `mathmacros.tex` and injects them into MathJax
- `mathmacros.tex` — shared LaTeX `\newcommand` definitions used in both Sphinx/MathJax and any LaTeX output
- `refs.bib` — BibTeX bibliography (used via `sphinxcontrib.bibtex`)
- `_static/css/custom.css` — custom CSS overrides for the RTD theme
- Content is in `.rst` files covering loudspeaker theory: alignment, box design, delta-mass, time/frequency response, and fitting

### Math Macros
Math macros defined in `src/mathmacros.tex` are parsed by `conf.py` and registered with MathJax so the same `\command` syntax works in both the HTML output and any LaTeX documents.
