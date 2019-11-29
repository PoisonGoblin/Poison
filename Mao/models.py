from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    isDelete = models.BooleanField(default=False)
    # 关联外键
    user_class = models.ForeignKey("Class", on_delete=models.CASCADE)


class Class(models.Model):
    class_name = models.CharField(max_length=20)
