from django.db import models
from pymongo import MongoClient


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, null=True)
    url = models.URLField(null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.name


# test = Student(name="pan", url="www.baidu.com", image="http://www.semantic-ui.cn/images/avatar2/large/matthew.png")
# test.save()
# c = MongoClient("localhost", 27017)
# school = c["school"]
# student_profile = school["student_profile"]
# for i in student_profile.find():
#     # print(i["name"], i["url"], i["image"])
#     m = Student(name=i["name"], url=i["url"], image=i["image"])
#     m.save()
