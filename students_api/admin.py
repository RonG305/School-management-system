from django.contrib import admin
from .models import Student, Department, Teacher, Event, ClassTeacher, SchoolPerformance
admin.site.site_header = 'STUDENT MANAGEMENT SYSTEM API'
admin.site.site_title = 'SMS API'
admin.site.index_title = 'Student Management app'

# Register your models here.

@admin.register(Student)
class StudentAdminModel(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'classroom', 'stream', 'surname', 'gender', 'date_of_birth', 'reg_number', 'religion']
@admin.register(Teacher)    
class TeacherAdminModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'teacher_id', 'department', 'date_joined', 'combinations', 'status', 'gender']   
    
@admin.register(Department)    
class DepartmentAdminModel(admin.ModelAdmin):
    list_display = ['department_name', 'department_code', 'head_of_departmemt']
    
@admin.register(Event)
class EventAdminModel(admin.ModelAdmin):
    list_display = ['title', 'date_uploaded', 'happening_date']  
    
@admin.register(ClassTeacher)
class ClassTeacherAdminModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'teacher_id', 'class_mastering', 'stream']
@admin.register(SchoolPerformance)    
class SchoolPerformanceAdminModel(admin.ModelAdmin):
    list_display = ['year', 'score']     
    
      
    
    