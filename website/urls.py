from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('meaning-of/<str:word>', views.WordView.as_view(), name='word_details', ),
    path('lookup-redirect', views.LookupRedirectView.as_view(), name='lookup_redirect', ),
]
