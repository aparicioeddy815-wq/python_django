import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from saludo.domain.persona import Persona
from saludo.application.services.saludar_service import SaludarService

servicio = SaludarService()


@csrf_exempt
def saludar(request):
    if request.method != "POST":
        return JsonResponse({"error": "Solo se permite POST"}, status=405)

    datos = json.loads(request.body)
    nombre = datos.get("nombre")

    if not nombre:
        return JsonResponse({"error": "El nombre es obligatorio"}, status=400)

    persona = Persona(nombre)
    mensaje = servicio.saludar(persona)

    return JsonResponse({"mensaje": mensaje})