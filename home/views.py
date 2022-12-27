from django.shortcuts import render
from home.models import Saya
from home.forms import FormSaya
# Create your views here.

def home(request):
    saya = Saya.objects.all()

    context = {
        'saya': saya,
    }
    return render(request,'home.html',context)

def tambah(request):
    form = FormSaya()

    context = {
        'form' : form,
    }
    return render(request,'form.html',context)