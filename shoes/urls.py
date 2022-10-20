
from django.urls import path 
from . import views
app_name='shoes'
urlpatterns = [
    path('',views.index,name='men'),
    
    path('women',views.home,name='women')
]