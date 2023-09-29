from django.db import models

# Create your models here.

class meet(models.Model):
    imgsrc=models.ImageField(upload_to="mtt")
    name=models.CharField(max_length=250)
    des=models.TextField()

    def __str__(self):
        return self.name

class place(models.Model):
    imgsrc1=models.ImageField(upload_to="ptt")
    name1=models.CharField(max_length=250)
    des1=models.TextField()


