from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Restaurate, Menu
from django.core.urlresolvers import reverse_lazy, reverse


class RegistrarRestaurante(generic.CreateView):
	template_name = 'restaurantes/registrar.html'
	fields="__all__"
	model = Restaurate
	success_url = reverse_lazy('restaurantes:reportar_restaurante')

class RestauranteView(generic.RedirectView):
	def get_redirect_url(self,*args, **kwargs):
		restaurante_obj = Restaurate.objects.get(id=kwargs.get('pk'))
		restaurante_obj.status = Restaurate.STATUS_DELETED
		restaurante_obj.save()
		return reverse('restaurantes:registrar_restaurante')

class ReportarRestaurante(generic.ListView):
	template_name = 'restaurantes/reportar.html'
	model = Restaurate
	def get_queryset(self):
		return Restaurate.objects.filter(status = Restaurate.STATUS_ACTIVE)

class ActualizarRestaurante(generic.UpdateView):
	template_name = 'restaurantes/actualizar.html'
	fields="__all__"
	model = Restaurate
	success_url = reverse_lazy('restaurantes:reportar_restaurante')
	template_name_suffix = '_update_form'
	
	

class EliminarRestaurante(generic.DeleteView):
	template_name = 'restaurantes/reportar.html'
	model = Restaurate
	success_url = reverse_lazy('restaurantes:reportar_restaurante')
