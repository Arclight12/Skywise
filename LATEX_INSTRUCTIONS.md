# LaTeX Compilation Instructions

## Files Created:
1. **Technical_Report.tex** - Main LaTeX document
2. **system_architecture.png** - System architecture diagram (in outputs/)
3. **prioritization_comparison.png** - Algorithm comparison visualization (in outputs/)

## How to Compile to PDF:

### Option 1: Online (Easiest - No Installation Required)
1. Go to https://www.overleaf.com/
2. Create a free account
3. Click "New Project" → "Upload Project"
4. Upload `Technical_Report.tex`
5. Create a folder called `satellite_prioritization_code/outputs/`
6. Upload both PNG images to that folder
7. Click "Recompile" - PDF will be generated automatically!

### Option 2: Local Installation (Windows)
1. Install MiKTeX: https://miktex.org/download
2. Install TeXstudio: https://www.texstudio.org/
3. Open `Technical_Report.tex` in TeXstudio
4. Press F5 or click "Build & View"
5. PDF will be generated in the same folder

### Option 3: Command Line (if you have LaTeX installed)
```bash
cd "c:\Users\KALIDASAN\OneDrive\Documents\FAI Project"
pdflatex Technical_Report.tex
pdflatex Technical_Report.tex  # Run twice for table of contents
```

## What You Get:
✅ Professional PDF matching the ASC template format
✅ Automatic table of contents
✅ Proper section numbering
✅ Formatted algorithms with pseudocode
✅ Tables and figures with captions
✅ References section
✅ ~15-18 pages of formatted content

## Before Compiling:
1. **Add your team details** in the `\author{}` section (lines 18-22)
2. **Verify image paths** - make sure the PNG files are in the correct location
3. **Optional**: Add Amrita logo if you have it

## Troubleshooting:
- **Missing packages**: MiKTeX will auto-install them when compiling
- **Image not found**: Check that images are in `satellite_prioritization_code/outputs/`
- **Compilation errors**: Run pdflatex twice (first run generates references)

## Customization:
- Change margins: Edit line 3 `\usepackage[margin=1in]{geometry}`
- Change font size: Edit line 1 `\documentclass[12pt,a4paper]{article}`
- Add more sections: Use `\section{}` and `\subsection{}`
