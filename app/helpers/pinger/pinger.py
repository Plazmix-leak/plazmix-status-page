from app.helpers.cache import Cache


class Pinger:
    def __init__(self, service_name: str):
        self._cache = Cache(f"pinger_{service_name}")