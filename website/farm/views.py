from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
# from .forms import ()  from .models import
from django.shortcuts import render

# Create your views here.
def about(request):

    context={

    }
    return render(request,'farm/about.html',context=context)

def blog(request):

    context={

    }
    return render(request,'farm/blog.html',context=context)\

def contact(request):

    context={

    }
    return render(request,'farm/contact.html',context=context)

def products(request):

    context={

    }
    return render(request,'farm/products.html',context=context)

def index(request):

    context={

    }
    return render(request,'farm/index.html',context=context)