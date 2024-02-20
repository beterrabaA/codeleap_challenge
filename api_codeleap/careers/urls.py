from careers.views import user_list

from django.urls import path

urlpatterns = [path('',user_list)]