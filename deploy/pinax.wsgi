# pinax.wsgi is configured to live in projects/cldj/deploy.

import os
import sys
import site

env_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../envs/cldj'))
site.addsitedir(os.path.join(env_dir, 'lib/python2.5/site-packages'))
sys.path.append(env_dir)

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "cldj.settings"

sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
