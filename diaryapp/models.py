from django.db import models
import datetime
class Blog(models.Model):
    title = models.CharField(max_length = 20, default='제목없음') 
    image = models.FileField(upload_to='images/')
    description = models.CharField(max_length = 500)
    date = models.DateTimeField('date published')
    user = models.CharField(max_length = 20, default = '글쓴이 없음')
    def __str__(self):
        return self.title
