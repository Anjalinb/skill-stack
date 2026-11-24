from django.urls import path
from programs.views import CourseListCreateView,CourseRetrieveUpdateDeleteView


urlpatterns=[
    path('courses/',CourseListCreateView.as_view()),
    path('courses/<int:pk>/',CourseRetrieveUpdateDeleteView.as_view()),
]