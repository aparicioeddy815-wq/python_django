from saludo.application.ports.saludar_use_case import SaludarUseCase


class SaludarService(SaludarUseCase):

    def saludar(self, persona):
        return "Hola " + persona.nombre