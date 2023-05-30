from networth_projection.api import Api
from networth_projection.core.config import Config
from networth_projection.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
