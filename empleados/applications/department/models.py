from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField('Name', max_length=50)
    short_name = models.CharField('short name ', max_length=20, blank=True)
    Anulate = models.BooleanField('Anulate', default=False)

    class Meta:
        verbose_name= 'my department' #change of name
        ordering = ['-name'] #orden descendente
        unique_together = ('name', 'short_name') #unico valor to don´t repit

    def __str__(self):
        return str(self.id) + '_' + self.name + '_' + self.short_name # TODO
        