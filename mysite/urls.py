from django.conf.urls import url

from . import view,testdb,search

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search_form$',search.search_form),
    url(r'^search$', search.search)
]