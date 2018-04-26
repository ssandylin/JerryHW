from django.shortcuts import render_to_response
from .models import person

def index(request):
	Person=person.objects.all()
	return render_to_response('cms/menu.html',locals())

# Create your views here.
