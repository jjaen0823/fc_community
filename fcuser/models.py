from django.db import models

# Create your models here.
class Fcuser(models.Model):  # models.Model inherit
    username = models.CharField(max_length=64, verbose_name='User Name')
    useremail = models.EmailField(max_length=128, verbose_name='User Email')
    password = models.CharField(max_length=64, verbose_name='Password')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Published DateTime')

    def __str__(self):  # class를 문자열로 변환할 때 호출되는 함수
        return self.username
    
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = 'FC User'
        # verbose_name_plural = 'FC Users'