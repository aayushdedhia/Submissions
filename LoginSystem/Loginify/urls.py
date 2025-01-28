
from django.urls import path
from . import views


urlpatterns = [
    path('print-hello/', views.hello_world),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success'),

    path('users/', views.get_all_users, name='get_all_users'),
    path('user/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('update-user/<str:email>/<str:new_password>/', views.update_user_password, name='update_user_password'),
    path('delete-user/<str:email>/', views.delete_user, name='delete_user'),
]
