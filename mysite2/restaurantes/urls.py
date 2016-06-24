from django.conf.urls import url


from . import views


app_name = 'restaurantes'
urlpatterns = [

	url(r'^$', views.RegistrarRestaurante.as_view(), name='registrar_restaurante'),
	url(r'^reportar/$', views.ReportarRestaurante.as_view(), name='reportar_restaurante'),
	url(r'^actualizar/(?P<pk>\d+)/$', views.ActualizarRestaurante.as_view(), name='actualizar_restaurante'),
	url(r'^reportar/(?P<pk>\d+)/$', views.EliminarRestaurante.as_view(), name='eliminar_restaurante'),
		
]