from django.urls import URLPattern
from . import views
from django.urls import path
from .views import *

urlpatterns =[
    path('index',index),
    path('logEvaluate',logEvaluate)
]
