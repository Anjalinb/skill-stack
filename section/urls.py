from django.urls import path
from section.views import ModuleCreateView,ModuleRetrieveUpdateDeleteView

urlpatterns=[
    path('course/<int:pk>/module/',ModuleCreateView.as_view()),
    path('module/<int:pk>/',ModuleRetrieveUpdateDeleteView.as_view()),
]