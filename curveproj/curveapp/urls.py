from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('define', views.index, name='index'),
    path('library', views.library, name='library'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("error", views.error_page, name="error"),
    # path("register", views.register, name="register")
]