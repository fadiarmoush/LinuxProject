from django.urls import path
from django.conf.urls import url
from .views import ListSongsView
from .views import ListSongsView2
from .views import ListSongsView3
from . import views
from .views import currentsView



urlpatterns = [
    path('cpu/', ListSongsView.as_view()),
    path('mem/', ListSongsView2.as_view()),
    path('disk/', ListSongsView3.as_view()),
    url(r'currents', currentsView.as_view()),
       
]
