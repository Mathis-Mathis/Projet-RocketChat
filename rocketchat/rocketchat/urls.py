from django.contrib import admin
from django.urls import path

import accounts.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
]
