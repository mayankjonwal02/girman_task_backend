

from django.urls import path

from girman_app.views import home , UserDataAPI


urlpatterns = [
    path('home/', home),
    path('userdata/', UserDataAPI.as_view()),
]