"""
Run this script to:
  1. Generate the notebook from create_notebook.py
  2. Execute every cell (producing all outputs)
  3. Save the executed notebook with outputs visible

Usage:
    python run_and_save.py
"""

import subprocess
import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))
NOTEBOOK = os.path.join(DIR, "AB_Testing_Experiment_Analysis.ipynb")

# Step 1: Generate the notebook
print("[1/2] Generating notebook...")
result = subprocess.run(
    [sys.executable, os.path.join(DIR, "create_notebook.py")],
    cwd=DIR, capture_output=True, text=True
)
if result.returncode != 0:
    print(f"ERROR generating notebook:\n{result.stderr}")
    sys.exit(1)
print(result.stdout.strip())

# Step 2: Execute the notebook in-place (saves with outputs)
print("\n[2/2] Executing notebook (this may take 1-2 minutes)...")
result = subprocess.run(
    [sys.executable, "-m", "jupyter", "nbconvert",
     "--to", "notebook",
     "--execute",
     "--inplace",
     "--ExecutePreprocessor.timeout=300",
     NOTEBOOK],
    cwd=DIR, capture_output=True, text=True
)
if result.returncode != 0:
    print(f"ERROR executing notebook:\n{result.stderr}")
    print("\nTip: Make sure jupyter is installed: pip install jupyter nbconvert")
    sys.exit(1)

print(f"\nDone! Notebook saved with all outputs at:\n  {NOTEBOOK}")
