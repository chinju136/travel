from django.shortcuts import render

from travelapp.models import Place, Demo


# Create your views here.
def demo(request):
    obj =Place.objects.all()
    obj1=Demo.objects.all()

    return render(request,"index.html",{'result':obj,'output':obj1})