from pydantic import BaseSettings

from networth_projection.version import __version__


class Config(BaseSettings):
    title: str = "Networth Projection"
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
