from django.conf.urls import url
from . import views

#url for class based views

urlpatterns = [
    url(r'^hello-world/',views.HelloWorldApi.as_view()),

]
