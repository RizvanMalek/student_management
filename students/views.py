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



def edit(request,id):
    data = StudentsModel.objects.get(id=id)
    return render(request,'students/add.html',{"data":data})

def delete_model(request):
    if request.POST:
        id = request.POST['id']
        StudentsModel.objects.filter(id=id).delete()
        return redirect('/students/listing')
    else:
        return HttpResponse("Something Went Wrong")


def tmp(request):
    if request.GET:
        data = StudentsModel.objects.filter(name__icontains=request.GET['data'])
        tbl = "<tr align='center'><th>ID</td><th>NAME</td><th>EMAIL</td><th>STATUS</td><th>ACTION</td></tr>"
        spn = ""
        for val in data:
            tbl+= "<tr align='center'>"
            tbl+= "<td>"+str(val.id)+"</td>"
            tbl+= "<td>"+val.name+"</td>"
            tbl+= "<td>"+val.email+"</td>"
            if str(val.is_active) == "1":
                spn = "<span class='status--process'>Active</span>"
            else:
                spn = "<span class='status--denied'>Not Active</span>"            
            tbl+= "<td>"+spn+"</td>"
            tbl+="<td><a href='/students/edit/"+str(val.id)+"' class='btn btn-primary'><i class='fa fa-edit'></i></a> "
            tbl+="<button type='button' class='btn btn-danger' data-toggle='modal' data-target='#staticModal' data-id="+str(val.id)+" id='p'><i class='fa fa-trash-alt'></i></button></td>"                                                                                                        
            tbl+= "</tr>"
        return HttpResponse(tbl)