from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def save_model(self):
        m = MyModel(self.name, self.age)
        m.save()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(MyModel, self).__init__()

    def __str__(self):
        return self.name