
from . import views
from django.urls import path

urlpatterns = [
    path('firstpage',views.firstpage,name='firstpage'),
    path('',views.load_add_page,name='load_add_page'),
    path('add_num',views.add_num,name='add_num'),
]
