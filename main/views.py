from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'shop',
        'price' : 25,
        'description' : 'e-shop'
    }

    return render(request, "main.html", context)