from django.db import models

class Arka(models.Model):
    title = models.CharField('Name', max_length=60)
    trailer = models.CharField('Intro', max_length=365)
    full_text = models.TextField('Article')
    when = models.DateField('Date of post')

    def __str__(self):
        return f'Novelty: {self.title}'
