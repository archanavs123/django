from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about-us/',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
]
