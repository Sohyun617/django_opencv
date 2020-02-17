from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # ses.jpg-> image/2020/02/17/ses.jpg
    document= models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add =True)
    
