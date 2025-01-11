

from django.urls import path

from girman_app.views import home , UserDataAPI , UserDataAPI_byname


urlpatterns = [
    path('home/', home),
    path('userdata/', UserDataAPI.as_view()),
    path('userdata_byname/<str:name>', UserDataAPI_byname.as_view(), name='Data By Name'),
]