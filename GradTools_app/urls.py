from django.urls import path
from . import views

app_name = "GradTools_app"

urlpatterns = [
    path('greet', views.Greet, name="greeting_page"),
    path('', views.home, name='home_page'),
    path('register/', views.register, name="register_page"),
    path('login/', views.login, name="login_page"),
    path('logout/', views.logout, name="logout_page"),
    path('new-page/', views.new_page, name="a new_page for form_page"),
    path('form/', views.form, name="form_page"),

]
