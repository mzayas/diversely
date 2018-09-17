from django.urls import path
from django.contrib import admin
admin.autodiscover()

import home.views, diagnostics.views, tools.views

# Examples:
# url(r'^$', 'diversely.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', home.views.index, name='index'),
    path('db', home.views.db, name='db'),
    path('tools', tools.views.tools, name='tools'),
    path('diagnostics', diagnostics.views.diagnostics, name='diagnostics'),
    path('admin/', admin.site.urls),
]
