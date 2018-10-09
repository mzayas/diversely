from django.urls import path
from django.contrib import admin
admin.autodiscover()

import home.views, accounts.views, jobs.views


# Examples:
# url(r'^$', 'diversely.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', home.views.index, name='index'),
    path('faq', home.views.faq, name='faq'),
    path('about', home.views.about, name='about'),
    path('services', home.views.services, name='services'),
    path('blog', home.views.blog, name='blog'),
    path('consultation', home.views.consultation, name='consultation'),
    path('register', accounts.views.register, name='register'),
    path('login', accounts.views.login, name='login'),
    path('admin/', admin.site.urls),
]
