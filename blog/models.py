from django.db import models
from django.utils import timezone#importamos librerias
# Create your models here.
class Post(models.Model):#esta línea define nuestro modelo
#//CLASS definicion de un objeto//post nombre de el objeto ///models.Model  el post es un modelo de Django asi se guarda en la BD
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#este es una relación (link) con otro modelo.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
