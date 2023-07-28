from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginCustomer, name="loginCustomer"),
# user/password = testing/temporary123
    path('logout/',views.logoutCustomer,name="logoutCustomer"),
]
