from .models import Account, Doctor, Visit
from .forms import CreateUserForm, VisitForm, UpdateAccountForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# View for Register Account
def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


# View for Home Page (list of doctors)
def home_view(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'home.html', context)


# View for Visit
@login_required
def visit_view(request, id):
    form = VisitForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    form = VisitForm(initial={'doctor': id, 'patient': request.user})

    context = {'form': form}
    return render(request, 'visit.html', context)


# View for profile of user
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UpdateAccountForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)