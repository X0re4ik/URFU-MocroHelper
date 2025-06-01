from .service import GetServerInfoService



class GetServerInfoServiceFactory:
    
    @staticmethod
    def create():
        return GetServerInfoService()