from django.db import models
import datetime
from imagekit.models import ImageSpecField # 썸네일 만들 수 있게 해줌
from imagekit.processors import ResizeToFill # 썸네일 크기 조정
class Blog(models.Model):
    title = models.CharField(max_length = 20, default='제목없음') 
    image = models.FileField(upload_to='images/')
    description = models.CharField(max_length = 500)
    date = models.DateTimeField('date published')
    user = models.CharField(max_length = 20, default = '글쓴이 없음')
   
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(80, 80)])
    def __str__(self):
        return self.title