from django.urls import path
from inicio.views import inicio, crear_curso

urlpatterns = [
    path('', inicio),
    path('curso/crear/<titulo>/<numero>', crear_curso)
]
