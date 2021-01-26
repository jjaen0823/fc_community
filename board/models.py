from django.db import models

# Create your models here.
class Board(models.Model):  # models.Model inherit
    title = models.CharField(max_length=128, verbose_name='Title')
    contents = models.TextField(verbose_name='Contents')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='Writer')  # ForeignKey 는 1:N 관계
    tags = models.ManyToManyField('tag.Tag', verbose_name='Tag')
    # on_delete=models.CASCADE: 가리키고 있는 사용자 탈퇴시, 같이 삭제한다.(해당 사용자가 쓴 글을 모두 삭제)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Published DateTime')

    def __str__(self):  # class를 문자열로 변환할 때 호출되는 함수
        return self.title
    
    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = 'Board'
        # verbose_name_plural = 'Boards'