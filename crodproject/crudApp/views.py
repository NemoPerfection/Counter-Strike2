from django.shortcuts import render
def homePage(request):
    title = "Home Page"
    return render(request, "index.html", {
        'title': title
    })
# Create your views here.
