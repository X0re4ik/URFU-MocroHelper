from src.shared.api.yandex.map import YandexMapClient, YandexMapResult


class GetPotentialTargets:

    def __init__(self, client: YandexMapClient):
        self._client = client

    async def get_potential_targets(
        self,
        latitude: float,
        longitude: float,
        message: str = "Производственные предпрития",
    ) -> list[YandexMapResult]:
        results = (
            await self._client.set_ll(latitude, longitude).set_attrs().send(message)
        )
        return results
