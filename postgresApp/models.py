from django.db import models

class student(models.Model):
    stu_name  = models.CharField(max_length=50)
    stu_mail  = models.EmailField()
    stu_pwd  = models.CharField(max_length=100)
    class Meta:
        db_table="student"
   


    