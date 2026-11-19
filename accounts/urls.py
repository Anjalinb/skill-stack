from django.urls import path
from accounts.views import UserSignUpView,AdminSignUpView,TrainerProfileUpdateView,TrainerProfileDetailView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path('user/signup/',UserSignUpView.as_view()),
    path('admin/signup/',AdminSignUpView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('trainerprofile/update/',TrainerProfileUpdateView.as_view()),
    path('trainerprofile/detail/',TrainerProfileDetailView.as_view()),
]