from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=20)
    def __str__(self):
        return self.department_name

class StaffInfo(models.Model):
    staff_name = models.CharField(max_length=20)
    staff_age = models.IntegerField()
    staff_sex = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)