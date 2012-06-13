import os.path
import sys

from django.conf import settings

settings.configure(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(__file__), 'testdb.sqlite'),
            }
        },
    INSTALLED_APPS = ('chunks',)
)

from django.test.utils import get_runner

test_runner = get_runner(settings)()
failures = test_runner.run_tests(['chunks'])

sys.exit(failures)
