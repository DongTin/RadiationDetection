from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST: str = 'localhost'
    PORT: int = 3306
    DATABASE: str = 'RadiationDetectionSystem'
    USER: str = 'pyUser2'
    PASSWORD: str = '123456'

    class Config:
        env_prefix = 'DB_'
        env_file = ".env"


settings = Settings()
