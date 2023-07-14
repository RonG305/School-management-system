from rest_framework import serializers
from .models import Student, Department, Teacher, Event, ClassTeacher, SchoolPerformance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'        

        
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'       
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  
        
        
class ClassTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTeacher
        fields = '__all__'
                       
                       
class SchoolPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolPerformance
        fields = '__all__'
        
                               
               