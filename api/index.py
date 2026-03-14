import os
import sys
from pathlib import Path

# Ensure the package dir, project root (<repo>/bookmyseat), and the repo root are on sys.path
# so that 'bookmyseat.settings' can be imported reliably in the Vercel runtime.
PACKAGE_DIR = Path(__file__).resolve().parent.parent / 'bookmyseat' / 'bookmyseat'
PROJECT_ROOT = PACKAGE_DIR.parent          # outer bookmyseat
REPO_ROOT = PROJECT_ROOT.parent            # repo root
for path in (PACKAGE_DIR, PROJECT_ROOT, REPO_ROOT):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmyseat.settings')

from vercel_django import handler
