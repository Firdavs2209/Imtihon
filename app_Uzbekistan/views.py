from django.shortcuts import render, get_object_or_404, redirect

from .models import Region


def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region/index.html', {'regions': regions})


def region_detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'region/index2.html', {'region': region})


def create_region(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'region/create_theme.html')


def create_theme(request):
    if request.method == 'POST':
        name = request.POST['name']
        new_theme = Region(name=name)
        new_theme.save()
        return redirect('theme_show', pk=new_theme.pk)

    else:
        return render(request, 'region/create_theme.html')


def edit_region(request, pk):
    this_theme = get_object_or_404(Region, id=pk)
    if request.method == 'POST':
        this_theme.name = request.POST['name']
        this_theme.save()
        return redirect('themes_show')
    else:
        return render(request, 'region/edit_theme.html', context={'region': this_theme})


def delete_region(request, pk):
    this_theme = get_object_or_404(Region, id=pk)
    if request.method == 'POST':
        this_theme.delete()
        return redirect('themes_show')
    else:
        return render(request, 'region/delete_theme.html', context={'theme_name': this_theme})