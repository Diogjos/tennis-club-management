from django.http import HttpResponse
from django.template import loader
from .models import Membros

def members(request):
  membro = Membros.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'membro': membro,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  membro = Membros.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'membro': membro,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  membro = Membros.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'fruits': 'banana',
  }
  return HttpResponse(template.render(context, request))