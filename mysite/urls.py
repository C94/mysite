from django.urls import include,path
from django.contrib import admin

from . import view,testdb,search

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
    # path(r'^testdb$', testdb.testdb),
    # path(r'^hello',view.hello),
    # path(r'^search$', search.search)
]
