from django.db import models

# Create your models here.

class Bb(models.Model):
    title=models.CharField(max_length=50
                           ,verbose_name='Заголовок')
    content=models.TextField(null=True,blank=True,verbose_name='Текст объявления')
    price=models.FloatField(null=True,blank=True,verbose_name='Цена')
    published=models.DateTimeField(auto_now_add=True,db_index=True)
    rubric=models.ForeignKey('rubric',on_delete=models.PROTECT,
                             verbose_name='Рубрика',null=True)

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name='Объявление'


class Rubric(models.Model):
    name=models.CharField(max_length=20,db_index=True,
                          verbose_name='Название')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Рубрики'
        verbose_name='Рубрика'
        ordering=['name']

