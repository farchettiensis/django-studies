from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user)
    print(args, kwargs)
    # return HttpResponse("<h1>foo</h1>")
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        'title': 'nothing much to this',
        'my_text': 'This is about us',
        'abc': 'This is not about us',
        'my_number': 123,
        'my_list': [1313, 4231, 312, "Abc"],
        'my_html': '<h1>Jordgubbe</h1>',
    }
    return render(request, 'about.html', my_context)

def documentation_view(request, *args, **kwargs):
    return render(request, 'documentation.html', {})