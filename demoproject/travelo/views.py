from django.shortcuts import render
from.models import place,team


# Create your views here.
def trvl(request):
    obj=place.objects.all()
    teamm = team.objects.all()
    return render(request,'index.html',{'result':obj,'teamm':teamm})
