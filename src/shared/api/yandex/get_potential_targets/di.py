from .service import GetPotentialTargets

from src.shared.api.yandex.map import yandexMapClient

class GetPotentialTargetsFactory:
    
    @staticmethod
    def create():
        return GetPotentialTargets(
            yandexMapClient,
        )