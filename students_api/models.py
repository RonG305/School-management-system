from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=200)
    department_code = models.CharField(max_length=20,unique=True)
    head_of_departmemt = models.CharField(max_length=200)
    
    def __str__(self):
        return self.department_name
        
    

    
class Teacher(models.Model):
    MARITUAL_STATUS = [
        ('Married', 'Married'),
        ('Single', 'Single')
    ]
    
    GENDER = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
       
    ]
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    teacher_id = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    combinations = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=MARITUAL_STATUS)
    gender = models.CharField(max_length=50, choices=GENDER)
    
    
    
    def __str__(self):
        if self.gender == 'MALE':
            return f'Mr.{self.last_name}'
        elif self.gender == 'FEMALE' and self.status == 'Married':
            return f'Mrs.{self.last_name}'
        elif self.gender == 'FEMALE' and self.status == 'Single':
            return f'Ms {self.last_name}'
        else:
            return f'Teacher {self.last_name}'
        
STREAM = [
    ('P', 'P'),
    ('R', 'R'),
    ('S', 'S'),
    ('T', 'T')
] 

CLASS = [
    ('FORM 1', 'Form 1'),
    ('FORM 2', 'Form 2'),
    ('FORM 3', 'Form 3'),
    ('FORM 4', 'Form 4'),
        
    ]       
        
class ClassTeacher(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_mastering = models.CharField(max_length=50, choices=CLASS)
    stream = models.CharField(max_length=50, choices=STREAM)
    
    def __str__(self):
        return self.last_name
   
             
            
            
        


class Student(models.Model):
    GENDER = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER')
    ]
    
    RELIGION = [
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Other', 'Other')
    ]
    
 
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    classroom = models.CharField(max_length=20, choices=CLASS, null=True)
    stream = models.CharField(max_length=50, choices=STREAM, null=True)
    surname = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    reg_number = models.CharField(null=True, max_length = 100, blank=True)
    religion = models.CharField(choices=RELIGION ,max_length=50, null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    happening_date = models.DateField()
    
    def __str__(self):
        return self.title
            
            
class SchoolPerformance(models.Model):
    year = models.PositiveIntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=3)
    
    def __str__(self):
        return f'{self.year} - {self.score}'            