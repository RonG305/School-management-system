from django.shortcuts import render
from .serializer import StudentSerializer, DepartmentSerializer, TeacherSerializer, EventSerializer, ClassTeacherSerializer, SchoolPerformanceSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Student, Department, Teacher, Event, ClassTeacher, SchoolPerformance

# Create your views here.
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StudentDetail(APIView):
    def get_object(self, pk):
        try: 
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        Response(status=status.HTTP_204_NO_CONTENT)     
        
        
class TeacherList(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    
class TeacherDetail(APIView):
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)   
        except Teacher.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
    
class ClassTeacherList(APIView):
    def get(self, request):
        class_teachers = ClassTeacher.objects.all()
        serializer = ClassTeacherSerializer(class_teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClassTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassTeacherDetail(APIView):
    def get_object(self, pk):
        try:
            return ClassTeacher.objects.get(pk=pk)
        except ClassTeacher.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        class_teacher = self.get_object(pk)
        serializer = ClassTeacherSerializer(class_teacher)
        return Response(serializer.data)
    
    def put(self, request, pk):
        class_teacher = self.get_object(pk)
        serializer = ClassTeacherSerializer(class_teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        class_teacher = self.get_object(pk)
        class_teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                  
        


class DepartmentList(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DepartmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    
class CourseList(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventDetail(APIView):
    def get_object(self, pk):
        try: 
            return Event.objects.get(pk=pk)    
        except Event.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
        
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    
class SchoolPerformanceList(APIView):
    def get(self, request):
        performances = SchoolPerformance.objects.all()
        serializers = SchoolPerformanceSerializer(performances, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializers = SchoolPerformanceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SchoolPerformanceDetail(APIView):
    def get_object(self, pk):
        try:
            return SchoolPerformance.objects.get(pk=pk)
        except SchoolPerformance.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        performance = self.get_object(pk)
        serializer = SchoolPerformanceSerializer(performance)
        return Response(serializer.data)
    
   
    def put(self, request, pk):
        performance = self.get_object(pk)
        serializer = SchoolPerformanceSerializer(performance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        performance = self.get_object(pk)
        performance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
                       
          
    
                      
          
              
               