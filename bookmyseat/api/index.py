import os
import sys
from pathlib import Path

# Ensure the repo root, project root (<repo>/bookmyseat), and package dir are on sys.path
# so that 'bookmyseat.settings' can be imported reliably in the Vercel runtime.
REPO_ROOT = Path(__file__).resolve().parents[2]             # <repo>
PROJECT_ROOT = REPO_ROOT / 'bookmyseat'                     # <repo>/bookmyseat
PACKAGE_DIR = PROJECT_ROOT / 'bookmyseat'                   # <repo>/bookmyseat/bookmyseat
for path in (PACKAGE_DIR, PROJECT_ROOT, REPO_ROOT):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmyseat.settings')

from django.core.wsgi import get_wsgi_application

# Vercel expects `app` as the entrypoint for Python functions
app = get_wsgi_application()
