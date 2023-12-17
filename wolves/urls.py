from django.urls import path

from . import views
urlpatterns = [
    
    path('',views.liverpool,name="liverpool"),
    path('add',views.add,name="add"),
    path('sub',views.sub,name="sub"),
    path('create_user/', views.create_user, name='create_user')
]
