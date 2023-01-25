def page1(request):
    """Calls on the html file named page1.html and renders it"""
    return render(request, "page1.html")

def page2(request):
    """Calls on the html file named page2.html and renders it"""
    return render(request, "page2.html")

def page3(request):
    """Calls on the html file named page3.html and renders it"""
    return render(request, "page3.html")