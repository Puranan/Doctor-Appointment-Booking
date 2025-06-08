from django.urls import path
from . import views
urlpatterns = [
    path("",views.hi, name="homepage"),
    path("about.html/",views.about, name="about"),
    path("contactus.html/",views.contactus,name="contactus"),
    path('add/',views.Insertdata,name="add"),
    path("services.html/",views.services),
    path("regforn.html/",views.reg),
    path('texas/',views.data,name='texas'),
    path('city/',views.andrew,name="city"),
    path("send/",views.Senthil,name="send"),
    path("afsal/",views.afsalas,name="afsal"),
    path("vikram/",views.vikramas,name="vikram")

 ]
