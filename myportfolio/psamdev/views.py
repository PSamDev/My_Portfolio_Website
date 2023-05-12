from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        form = MessageForm (request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Message Submitted")
           
    else:
        form = MessageForm 
    return render(request, "home.html", context={"form":form})
   