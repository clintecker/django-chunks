# ---- django-chunks ----

urlpatterns += patterns('',
    (r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)
