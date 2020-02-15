from django.urls import path
from . import views
urlpatterns=[
    path('HelloApi/',views.HelloApiView.as_view())
]