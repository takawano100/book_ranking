from django.db import models


class Publishers(models.Model):
    name = models.CharField(max_length=1000)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    date_of_publication = models.DateField()
    publisher = models.ForeignKey(
        Publishers, on_delete=models.CASCADE
    )
    url = models.URLField()
    total_point = models.IntegerField()
    yearly_point = models.IntegerField()
    monthly_point = models.IntegerField()

    class Meta:
        db_table = 'book'
    
    def __str__(self):
        return self.title

class Pictures(models.Model):
    picture = models.FileField(upload_to='picture/')
    book = models.ForeignKey(
        Books, on_delete=models.CASCADE
    )
    order = models.IntegerField()

    class Meta:
        db_table = 'picture'
        ordering = ['order']

    def __str__(self):
        return self.book.title + ': ' + str(self.order)
