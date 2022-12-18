from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("", include("django.contrib.auth.urls")),  # new
    # get and post req. for Login
    path('', views.loginPanel, name='login'),
    # get and post req. for Logout
    path('logou/', views.logoutUser, name='logou'),
    # get and post req. for registration
    path('register', views.registerPanel, name='register'),
    # get and post req. for insert operation
    path('insert', views.employee_form, name='employee_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    # get req. to retrieve and display all records
    path('list/', views.employee_list, name='employee_list'),

]
