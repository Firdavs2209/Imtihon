from django.db import models
from django.shortcuts import render, get_object_or_404, redirect


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True,verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='static/image/',verbose_name="Image")
    Area= models.CharField(max_length=255, verbose_name="Area")
    def __str__(self):
        return self.name


class Meta:
    verbose_name = "Uzbekistan"
    verbose_name_plural = "Viloyatlar"
    ordering = ['id']
    db_table = 'Uzbekistan'

def create_theme(request):
    if request.method == 'POST':
        name = request.POST['name']
        new_theme = Region(name=name)
        new_theme.save()
        return redirect('theme_show', pk=new_theme.pk)

    else:
        return render(request, 'region/create_theme.html')


def edit_theme(request, pk, name):
    this_theme = get_object_or_404(Region, id=pk)
    if request.method == 'POST':
        this_theme.name = request.POST['name']
        this_theme.save()
        return redirect('themes_show')
    else:
        return render(request, 'region/edit_theme.html', context={'theme_name': name})


def delete_theme(request, pk, name):
    this_theme = get_object_or_404(Region, id=pk)
    if request.method == 'POST':
        this_theme.delete()
        return redirect('themes_show')
    else:
        return render(request, 'region/delete_theme.html', context={'theme_name': name})
