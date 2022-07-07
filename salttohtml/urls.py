from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("converter", views.convert_page, name='converter'),
    path("guides", views.guides_page, name='guides'),
    path("preview1", views.preview_page1, name='preview1'),
    path("preview2", views.preview_page2, name='preview2'),
]