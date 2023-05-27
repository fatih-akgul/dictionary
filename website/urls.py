from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path('', views.index, name='index'),
    path('meaning-of/<str:word>', views.word_details, name='word_details', ),
    path('lookup-redirect', views.lookup_redirect, name='lookup_redirect', ),
]
