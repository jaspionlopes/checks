DEBUG = False
ALLOWED_HOSTS = ["https://checks-ii29.onrender.com", "localhost"]

import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
