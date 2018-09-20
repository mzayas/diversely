from django.urls import path
from django.contrib import admin
admin.autodiscover()

import home.views, diagnostics.views, tools.views, accounts.views


# Examples:
# url(r'^$', 'diversely.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', home.views.index, name='index'),
    path('tools', tools.views.tools, name='tools'),
    path('diagnostics', diagnostics.views.diagnostics, name='diagnostics'),
    path('register', accounts.views.RegisterView, name='register'),
    path('login', accounts.views.login, name='login'),
    path('admin/', admin.site.urls),
]
