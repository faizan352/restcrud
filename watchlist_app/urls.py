from django.urls import path
# from.views import Movie_list
from .views import  WatchDetailAV,WatchListAV,StreamPlatformAV,StreamDetailAV

urlpatterns = [

    path('stream/', StreamPlatformAV.as_view()),
    path('stream/<int:pk>/', StreamDetailAV.as_view()),
    path('watchlist/', WatchListAV.as_view()),
    path('watchlist/<int:pk>/', WatchDetailAV.as_view()),


]