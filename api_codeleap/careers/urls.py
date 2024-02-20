from careers.views import user_list,user_change_and_delete

from django.urls import path

urlpatterns = [path('',user_list),path('<int:pk>/',user_change_and_delete)]