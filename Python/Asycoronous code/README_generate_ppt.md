Generate Module_System_in_Python.pptx

This small script builds a PowerPoint containing all content from `Module System in Python.txt`.

Setup

1. Create a virtual environment (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements:

```powershell
pip install -r requirements.txt
```

Run

```powershell
python generate_ppt.py
```

Output

- `Module_System_in_Python.pptx` will be created in the same folder.

Notes

- The script places the source text into slides in chunks and adds full text to speaker notes so no content is removed.
- If you want richer diagrams (shapes, arrows), I can extend the script to draw those programmatically or accept images to embed.