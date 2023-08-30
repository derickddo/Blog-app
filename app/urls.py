from django.urls import path 
from . import views

urlpatterns = [
    path("",views.redirect_to_home, name="redirect__to_home"),
    path('sign_up',views.sign_up, name='sign_up'),
    path('update_user',views.update_user, name='update_user'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('page/<str:page>',views.home, name='home'),
    path('create_post/',views.create_post, name='create_post'),
    path('get_post/<str:pk>/',views.get_post, name='get_post'),
    path('update_post/<str:pk>/',views.update_post, name='update_post'),
    path('update_comment/<str:pk>/',views.update_comment, name='update_comment'),
    path('delete_post/<str:pk>/',views.delete_post, name='delete_post'),
    path('delete_comment/<str:pk>/',views.delete_comment, name='delete_comment'),
    path("add_category", views.add_category, name="add_category")
]