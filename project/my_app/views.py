from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import MOUForm
from .models import MOU
from django.contrib.auth import authenticate, login

def index_view(request):
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('view_mou')  # Redirect to another page after saving
    else:
        form = MOUForm()

    return render(request, 'index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index view after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def update_mou_view(request, id):
    mou_instance = MOU.objects.get(id=id)
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES, instance=mou_instance)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('view_mou')  # Redirect after successful update
    else:
        form = MOUForm(instance=mou_instance)
    return render(request, 'update_mou.html', {'form': form})

def create_mou_view(request):
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('view_mou')  # Redirect after successful upload
        else:
            # If the form is not valid, display the errors
            messages.error(request, "There was an error in the form. Please correct the errors and try again.")
    else:
        form = MOUForm()
    return render(request, 'create_mou.html', {'form': form})

def view_mou_view(request):
    mou_list = MOU.objects.all()  # Fetch all MOU records

    return render(request, 'view_mou.html', {'mou_list': mou_list})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MOUForm
from .models import MOU

def view_mou_view(request):
    mou_list = MOU.objects.all()  # Fetch all MOU records
    return render(request, 'view_mou.html', {'mou_list': mou_list})

def edit_mou_view(request, id):
    mou_instance = get_object_or_404(MOU, id=id)
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES, instance=mou_instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MOUForm(instance=mou_instance)
        return render(request, 'edit_mou_form.html', {'form': form, 'mou': mou_instance})

def delete_mou_view(request, id):
    mou_instance = get_object_or_404(MOU, id=id)
    if request.method == 'POST':
        mou_instance.delete()
        return redirect('view_mou')
    return render(request, 'delete_mou.html', {'mou': mou_instance})


# EDIT
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .forms import MOUForm
from .models import MOU

def view_mou_view(request):
    mou_list = MOU.objects.all()  # Fetch all MOU records
    return render(request, 'view_mou.html', {'mou_list': mou_list})

def edit_mou_view(request, id):
    mou_instance = get_object_or_404(MOU, id=id)
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES, instance=mou_instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MOUForm(instance=mou_instance)
        return render(request, 'edit_mou_form.html', {'form': form, 'mou': mou_instance})