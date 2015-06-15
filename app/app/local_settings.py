from .settings import *

# change to the place where you put your static files (e.g. where "/srv/www/django-skeleton/" is web root)
STATIC_ROOT = "/srv/www/django-skeleton/static"

# an upload folder where you upload files to (can use symbolic link to set under app folder)
MEDIA_ROOT = os.path.join(BASE_DIR, "upload")
