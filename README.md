# GDS Library — ANFF-Q

A collection of GDS-II file generators for nanofabrication mask design, developed at the **Australian National Fabrication Facility Queensland (ANFF-Q), University of Queensland**.

---

## Overview

This library provides tools for generating GDS-II layout files used in electron-beam and photolithography mask writing. The focus is on parametric array patterns — define your geometry once, export a ready-to-use `.gds` file.

Currently includes:

| Tool | Description |
|---|---|
| `gds_hexdots.py` | Command-line generator for hexagonally-packed circular dot arrays |
| `gds_hexdots_GUI.py` | Desktop GUI version (Windows executable via Py2exe) |
| `gds_hexdots_web.html` | Browser-based GUI with live preview and direct `.gds` export — no installation required |

---

## Web Interface (Recommended)

The web tool runs entirely in your browser — no Python or dependencies needed. Open `gds_hexdots_web.html` directly, or host it via GitHub Pages.

**Features:**
- **Array lattice** — Hexagonal (true 6-neighbour close-packing) or Square
- **Element shapes** — Circle, Hexagon, Square, Triangle, Diamond, Octagon, Cross, Ring
- **Live canvas preview** with pan and zoom
- **Fill ratio and element count** calculated in real time
- **Canvas background themes** — Dark, Light, White/Print, Blueprint
- **One-click `.gds` export** — binary GDS-II written directly in the browser

---

## Python Scripts

### `gds_hexdots.py`

Command-line script. Run it and enter parameters when prompted.

**Requirements:**
```
pip install gdsCAD numpy
```

**Usage:**
```bash
python gds_hexdots.py
```

You will be prompted for:
- Dot radius (μm)
- Centre-to-centre pitch (μm)
- Write area width (μm)

The output `.gds` file is saved to the current directory with an auto-generated filename, e.g.:
```
Area1mm_circ_Dia4um_Lcc10um.gds
```

### `gds_hexdots_GUI.py`

Desktop GUI version of the same tool. Can be compiled to a standalone Windows `.exe` using [Py2exe](https://www.py2exe.org/).

**Requirements:**
```
pip install gdsCAD numpy tkinter
```

---

## GDS-II File Format Notes

- **Database units:** 1 nm (1 μm = 1000 db units)
- **User units:** μm
- Circular dots are approximated as **32-sided polygons** — standard practice in GDS-II, which has no native arc primitive
- **Layer 0** — dot/element geometry
- **Layer 99** — bounding box of the write area

---

## Output Filename Convention

Files are named to encode the key parameters at a glance:

```
hex_circ_Dia4um_Lcc10um_Area500um.gds
 │    │     │      │       └─ write area width
 │    │     │      └───────── centre-to-centre pitch
 │    │     └──────────────── dot diameter
 │    └────────────────────── element shape (circ, hexa, squa, …)
 └─────────────────────────── lattice type (hex / sq)
```

---

## Author

**Elliot Cheng**
ANFF-Q, The University of Queensland
h.cheng6@uq.edu.au

---

## License

This project is intended for use within ANFF-Q and collaborating research groups. Please contact the author for reuse or distribution queries.
