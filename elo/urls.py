from django.conf.urls import url
from elo import views
from django.urls import path

urlpatterns = [
        path('testget/top/',views.Top.as_view()),
        path('testget/',views.eloView.as_view()),
        path('testget/validateUser/',views.processing.as_view()),
        ]
