from django.shortcuts import render, HttpResponse, redirect
from .models import Show
# Create your views here.
def index(request):
    print('displaying the add a new show page')
    return render(request, 'tv_show_app/index.html')

def add_show(request):
    print('the add show method is running')
    print(request.POST["title"])
    if request.method == "POST":
        val_from_title_field = request.POST["title"]
        val_from_network_field = request.POST["network"]
        val_from_release_date_field = request.POST["release_date"]
        val_from_description_field = request.POST["desc"]
    Show.objects.create(title=val_from_title_field, network=val_from_network_field, release_date=val_from_release_date_field, description=val_from_description_field)
    last_show = Show.objects.last()
    return redirect('/shows/'+ str(last_show.id))

def show_page(request, id):
    print('the show page method is running')
    this_show = Show.objects.get(id=id)
    context = {
        'title': this_show.title,
        'network': this_show.network,
        'release_date': this_show.release_date,
        'description': this_show.description,
        'last_updated': this_show.updated_at,
        'show_id': this_show.id
    }
    return render(request, 'tv_show_app/display_show.html', context)

def show_edit_page(request, id):
    print('the edit page is running')
    this_show = Show.objects.get(id=id)
    context = {
        'this_show': this_show
    }
    return render(request, 'tv_show_app/edit_show.html', context)

def edit_show(request, id):
    print('the edit show method is working')
    if request.method == "POST":
        edit_this_show = Show.objects.get(id=id)
        edit_this_show.title = request.POST['title']
        edit_this_show.network = request.POST['network']
        edit_this_show.release_date = request.POST['release_date']
        edit_this_show.description = request.POST['desc']
        edit_this_show.save()
    return redirect('/shows/' + str(edit_this_show.id))

def delete_show(request, id):
    print('the delete show method is working')
    delete_this_show = Show.objects.get(id=id)
    delete_this_show.delete()
    return redirect('/shows')

def all_shows(request):
    print('all the shows are being displayed')
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'tv_show_app/all_shows.html', context)