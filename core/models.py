from django.db import models

class Production(models.Model):

    TYPE_MIRROR = 'MIRROR'
    TYPE_ANOTHER = 'ANOTHER'
    TYPE_CHOICES = (
        (TYPE_MIRROR, 'MIRROR'),
        (TYPE_ANOTHER, 'ANOTHER'),
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

class Another(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img = models.ImageField(null=True)
    parameter1 = models.ForeignKey('Production', on_delete=models.CASCADE, null=True)
    parameter2 = models.TextField(blank=True)
    parameter3 = models.SmallIntegerField(default=0)
    parameter4 = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Mirror(models.Model):

    TYPE_1 = 'Разборное'
    TYPE_2 = 'Цельное'
    TYPE_CHOICES = (
        (TYPE_1, 'Разборное'),
        (TYPE_2, 'Цельное'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img = models.ImageField(null=True)
    product = models.ForeignKey('Production', on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    manufacture = models.ForeignKey('Manufacture', on_delete=models.CASCADE, null=True)
    color = models.ForeignKey('Color', on_delete=models.CASCADE, null=True)
    height = models.SmallIntegerField(default=0, help_text='mm')
    width = models.SmallIntegerField(default=0, help_text='mm')
    thickness = models.SmallIntegerField(default=0, help_text='mm')

    def __str__(self):
        return self.title

class Color(models.Model):
    col_title = models.CharField(max_length=100)
    def __str__(self):
        return self.col_title

class Manufacture(models.Model):
    man_title = models.CharField(max_length=100)
    def __str__(self):
        return self.man_title
