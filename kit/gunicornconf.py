# use command: `gunicorn -c kit/gunicornconf.py`
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

wsgi_app = "kit.wsgi"
bind = ["0.0.0.0:8005"]
worker_class = "sync"
workers = 1
loglevel = "error"
capture_output = False
accesslog = os.path.join(BASE_DIR, "log/access.log")
errorlog = os.path.join(BASE_DIR, "log/error.log")
