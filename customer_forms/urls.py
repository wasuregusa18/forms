from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="forms/login_form.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="forms/loggedout.html"),name="logout"),
    path("", include("forms.urls")),
]
