from django.conf import settings
from md5 import md5 

def get_cache_suffix():
    try:
        project_hash = md5(settings.SECRET_KEY).hexdigest()
        return "_%s" % project_hash
    except AttributeError:
        return "_%s" % md5().hexdigest()