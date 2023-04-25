from django.shortcuts import render
from sessionAPIapp.forms import ItemForm

# Create your views here.

def home(request):
    count = request.session.get("count", 0)
    count +=1
    request.session["count"] = count
    return render(request, "index.html")

def add(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            quantity = form.cleaned_data["quantity"]
            request.session[item] = quantity   # Note it is request not response. In cookies we set on response to send to coming view
    return render(request, "add.html", {"form":form})

def display(request):
    return render(request, "display.html")