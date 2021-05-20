import students
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import StudentsModel
from .forms import StudentsForm
# Create your views here.

def listing(request):
    if request.user.is_authenticated:
        data = StudentsModel.objects.all()
        return render(request,'students/listing.html',{"data":data})
    else:
        return redirect('/login')

    

def add(request):
    if request.user.is_authenticated:
        return render(request,'students/add.html')
    else:
        return redirect('/login')

def add_model(request):
    if request.POST:
        if "btnEdit" in request.POST:
            id = request.POST['hdid']
            tmp_id = StudentsModel.objects.get(id=id)
            form = StudentsForm(request.POST,instance=tmp_id)
            if form.is_valid():
                form.save()
                return redirect('/students/listing')
            else:
                return redirect('/students/edit')
        else:
            form = StudentsForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('/students/listing')
            else:
                return redirect('/students/add')

def delete_model(request,id):
    StudentsModel.objects.filter(id=id).delete()
    return redirect('/students/listing')


def edit(request,id):
    data = StudentsModel.objects.get(id=id)
    return render(request,'students/add.html',{"data":data})