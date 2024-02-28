
from django.urls import path,path,include
from.views import see_user_ordr_history,sign_up,log_in,log_out,user_profile,change_password,profileUP
urlpatterns = [
   
    path('sign_up/',sign_up,name='sign_up'),
    path('change_password/',change_password,name='change_password'),
    path('login/',log_in,name='login'),
    path('log_out/',log_out,name='log_out'),
    path('user_profile/',user_profile,name='user_profile'),
    path('profileUP/',profileUP,name='profileUP'),
    path('see_user_ordr_history/',see_user_ordr_history,name='see_user_ordr_history'),

   
]
