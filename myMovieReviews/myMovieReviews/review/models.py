from tabnanny import verbose
from django.db import models
app_name='posts'
# Create your models here.
class Post(models.Model):
    title=models.CharField(verbose_name="제목",max_length=100)
    director=models.CharField(verbose_name="감독",max_length=50)
    main=models.CharField(verbose_name="주연",max_length=100)
    romance='로맨스'
    horror='공포'
    comedy='코미디'
    fantasy='판타지'
    SF="SF"
    history="사극"
    choice_genre=(
        (romance,'로맨스'),(horror,'공포'),(comedy,'코미디'),(fantasy,'판타지'),(SF,'SF'),(history,'사극')
    )
    genre=models.CharField(choices=choice_genre,verbose_name="장르",max_length=100)
    photo = models.ImageField(upload_to="",blank=True, null=True)
    star= models.IntegerField(verbose_name="별점")
    time=models.CharField(verbose_name="러닝타임",max_length=50)
    review=models.TextField(verbose_name="내용")
    year=models.CharField(verbose_name="개봉년도",max_length=50)

    def __str__(self):
        return self.title



        
