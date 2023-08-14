from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().values()
  firstnames = Member.objects.all().values_list('firstname', flat=True)
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
    'members_firstnames': firstnames,
    'members': mymembers,
    'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'],
  }
  return HttpResponse(template.render(context, request))

def testing_again(request):
  mydata = Member.objects.all().values()
  mydata1 = Member.objects.all().values_list('firstname')
  mydata2 = Member.objects.filter(firstname='Emil').values()
  mydata3 = Member.objects.filter(lastname='Refsnes', id=2).values()
  template = loader.get_template('tests.html')
  context = {
    'mydata': mydata,
    'mydata1': mydata1,
    'mydata2': mydata2,
    'mydata3': mydata3,
  }
  return HttpResponse(template.render(context, request))
