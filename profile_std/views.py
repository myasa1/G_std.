from django.shortcuts import render ,redirect ,get_object_or_404
from .models import  Profile

from .forms import ProfileForm

def Profile(request):
   Profile = Profile.objects.all()

    if request.method == 'POST' :
        form =ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:Profile')
    else:
        form = ProfileForm()

        

    if request.method == 'POST' :
        Profile_id = request.POST['Profile_id']
        Profile = get_object_or_404(Profile , id = Profile_id)

        if Profile.checked:
            Profile.checked = False
            Profile.save()
        else:
            Profile.checked = True
            Profileo.save()

    return render(request , 'Profile' , {
        Profile' : Profile ,
        'form' : form,
    })

def update_Profile(request , pk):

    Profile_id = Profile.objects.get(pk=pk)
    update_form = ProfileForm(instance=Profile_id)
    if request.method == 'POST' :
        update_form = ProfileForm(request.POST , instance=Profile_id)
    if update_form.is_valid():
        update_form.save()
        return redirect('home:Profile')
    else:
        update_form = ProfileForm(instance=todoProfile_id)

    return render(request , 'update_Profile.html' , {
        'update_form' :update_form,
    })

def Profile_delete(request , pk):
    Profile_delete = Todo.objects.get(pk=pk)
    Profile_delete.delete()
    return redirect('home:Profile')