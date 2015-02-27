"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

    def __str__(self):
        return self.name

class Element(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    css_string = models.CharField(verbose_name='Styles', max_length=5000)
    search_words = models.CharField(verbose_name='Search Words', max_length=1000)
    category = models.ForeignKey(Category, verbose_name='Categories', blank=True,
                                 null=True, default='', on_delete=models.SET_NULL,)

    def __str__(self):
        string = self.name
        if(self.category):
            string += ' Category: ' + self.category.__str__()

        return string

#ID, css string, search words