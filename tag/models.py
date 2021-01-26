from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='Tag')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Pub date')

    def __str__(self):  # class를 문자열로 변환할 때 호출되는 함수
        return self.name
    
    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = 'Tag'
        # verbose_name_plural = 'Tags'