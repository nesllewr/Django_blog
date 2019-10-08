from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):#post가 데이터베이스에 저장되어야 한다
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # foreignKey 다른 모델에 대한 링크 
    title = models.CharField(max_length=200)#글자 수 제한(제목)
    text = models.TextField() #글자수 제한 없는 긴 텍스트(블로그 콘텐츠)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title