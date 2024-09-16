from django.shortcuts import render, redirect
from main.forms import NotesEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    notes_entries = Product.objects.all()
    
    context = {
        'name' : 'Min Kim',
        'class': 'KKI',
        'notes_entries' : notes_entries
    }

    return render(request, "main.html", context)

def create_note_entry(request):
    form = NotesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_note_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
