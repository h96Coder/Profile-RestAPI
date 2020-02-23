from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router =DefaultRouter()
router.register('HelloViewSet',views.HelloViewSet,base_name='HelloViewSet')
router.register('Profiles',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns=[
    path('HelloApi/',views.HelloApiView.as_view()),
    path('Login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]