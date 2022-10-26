from django.urls import path
from .views import CourseList, CourseDetail

urlpatterns = [
    path('', CourseList.as_view(), name='get-courses'),
    path('<int:pk>', CourseDetail.as_view(), name='course-detail'),
]