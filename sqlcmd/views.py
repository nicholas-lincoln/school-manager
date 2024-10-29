from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserModels


# Create your views here.
def user_list(request):
    context = {'user_list': UserModels.objects.all()}
    return render(request, 'user_register/user_list.html', context)


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            user = UserModels.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'user_register/user_form.html', {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = UserModels.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/sqlcmd/list')


def user_delete(request, id):
    user = UserModels.objects.get(pk=id)
    user.delete()
    return redirect('/sqlcmd/list')
