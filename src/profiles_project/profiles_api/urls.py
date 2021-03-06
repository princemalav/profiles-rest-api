from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-view', views.HelloViewset, base_name='hello-view')
router.register('profile',views.UserProfileViewset)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeedViewSet)
#url for class based views

urlpatterns = [
    url(r'^hello-world/',views.HelloWorldApi.as_view()),
    url(r'',include(router.urls)),

]
