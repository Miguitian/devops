import traceback
import sys
try:
    from __init__ import _project_root
    sys.path.append(_project_root)
except Exception as e:
    traceback.print_exc()