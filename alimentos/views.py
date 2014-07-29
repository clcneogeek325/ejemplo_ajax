from django.shortcuts import render_to_response
from django.template import RequestContext
from alimentos.forms import tipoForm
from django.core import serializers
from alimentos.models import frutas,verduras
from django.http import HttpResponse
import json


def view_index(request):
	if request.is_ajax():
		print "Fue una peticion ajax"
	form  = tipoForm()
	ctx = {'form':form}
	return render_to_response("index.html",ctx,context_instance=RequestContext(request))

def view_ws_alimento(request,tipo):
	if request.method == "GET":
		if tipo == "ver":
			print "verduras"
			data = serializers.serialize("json",verduras.objects.filter(status=True))
			return HttpResponse(data,mimetype='application/json')
		else:
			print "frutas"
			data = serializers.serialize("json",frutas.objects.filter(status=True))
			return HttpResponse(data,mimetype='application/json')
	else:
		return HttpResponse("No hay ningun problema")
