from django.shortcuts import render, redirect
from main.forms import NotesEntryForm
from main.models import Product
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    
    context = {
        'name' : request.user.username,
        'class': 'KKI',
        'last_login' : request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_note_entry(request):
    form = NotesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        note_entry = form.save(commit=False)
        note_entry.user = request.user
        note_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_note_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_entry(request, id):
    note = Product.objects.get(pk = id)

    form = NotesEntryForm(request.POST or None, instance = note)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_entry.html", context)

def delete_entry(request, id):
    note = Product.objects.get(pk = id)
    note.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_note_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    subject = strip_tags(request.POST.get("subject"))
    description = strip_tags(request.POST.get("description"))
    price = strip_tags(request.POST.get("price"))
    user = request.user

    new_note_entry = Product(
        name=name, subject=subject,
        description = description, price=price,
        user=user
    )
    new_note_entry.save()

    return HttpResponse(b"CREATED", status=201)