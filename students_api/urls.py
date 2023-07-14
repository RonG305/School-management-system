from django.urls import path
from .views import StudentList, StudentDetail, DepartmentList, DepartmentDetail, TeacherList, TeacherDetail, EventList, EventDetail, ClassTeacherList, ClassTeacherDetail, SchoolPerformanceList, SchoolPerformanceDetail

urlpatterns = [
    path('students/', StudentList.as_view() ),
    path('students/<int:pk>/', StudentDetail.as_view()),
    path('departments/', DepartmentList.as_view() ),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>/', StudentDetail.as_view()),
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('classteachers/', ClassTeacherList.as_view()),
    path('classteachers/<int:pk>/', ClassTeacherDetail.as_view()),
    path('performances/', SchoolPerformanceList.as_view()),
    path('performances/<int:pk>/', SchoolPerformanceDetail.as_view())   
]