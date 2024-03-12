from django.db import models
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
      return self.name
class person(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics1')
    descp=models.TextField()
    def __str__(self):
        return self.name
