from distutils.command.upload import upload
from django.db import models
from django.forms import ImageField
from applications.department.models import Department
from ckeditor.fields import RichTextField

# Create your models here.
class Skills(models.Model):
    ability = models.CharField('ability', max_length=50)

    class Meta:
        verbose_name = 'Ability'
        verbose_name_plural = 'Employee Skills'
    
    def __str__(self):
        return str(self.id) + '-' + self.ability
        





class Employee(models.Model):
    JOB_CHOICES = {
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    }
    #model to table employee
    #types(tipos)
    first_name = models.CharField("Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    full_name = models.CharField(
        'Full name ',
        max_length=120,
        blank=True
    )
    job = models.CharField("job", max_length=1, choices=JOB_CHOICES)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='employee', blank=True, null=True)
    skills = models.ManyToManyField(Skills) 
    curriculum_vitae = RichTextField()
    class Meta:
        verbose_name= 'my employee' #change of name
        ordering = ['-first_name', 'last_name', '-job'] #decending order
        unique_together = ('first_name', 'last_name') #only non-repeating value  (does not apply)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
