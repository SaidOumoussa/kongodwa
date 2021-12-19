from django.urls import path
from . import views as reg_views
urlpatterns = [
    path('index', reg_views.index, name='index'),
    path('profile/', reg_views.register, name='profile'),
]