from django.db import models


# Create your models here.

class Device(models.Model):
    d_name = models.CharField(max_length=20)
    d_type = models.CharField(max_length=20)
    d_date = models.DateTimeField()
    d_describe = models.CharField(max_length=500)
    d_price = models.IntegerField()
    # 关联外键
    user_class = models.ForeignKey("Class", on_delete=models.CASCADE)


class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_model = models.CharField(max_length=100)


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_describe = models.CharField(max_length=1000)
