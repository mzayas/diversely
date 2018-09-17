from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views, ideas.views
from ideas.views import BrainstormView

# Examples:
# url(r'^$', 'diversely.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', hello.views.index, name='index'),
    path('db', hello.views.db, name='db'),
    path('brainstorm', BrainstormView.as_view(), name='brainstorm'),
    path('admin/', admin.site.urls),
]
