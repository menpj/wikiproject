from django.urls import path

from . import views

app_name= "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    #path("content",views.content,name="content"),
    path("wiki",views.wiki,name="wiki"),
    path("wiki/<str:name>",views.wiki,name="wiki"),
    path("wikiSearch",views.wikiSearch,name="wikiSearch"),
    path("newPage",views.newPage,name="newPage"),
    path("newPageError",views.newPageError,name="newPageError"),
    path("editPage/<str:name>",views.editPage,name="editPage"),
    path("editPage",views.editPage,name="editPage"),
    path("randomPage",views.randomPage,name="randomPage")
    
]
