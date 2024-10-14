from django.urls import path
from accounts.views import homepage,about_us


app_name = 'first_app'
urlpatterns = [
    #path('', about_us, name="about_us"),
    path('home',homepage,name="home"),
    path("about",about_us,name = 'about'),

]