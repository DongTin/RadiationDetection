from pydantic import BaseSettings


class Settings(BaseSettings):
    CapitalURL: str = 'https://data.rmtc.org.cn/gis/listtype0M.html'
    NuclearPlantURL: str = 'https://data.rmtc.org.cn/gis/listtype1M.html'

    class Config:
        env_prefix = 'CRAWLER_'
        env_file = ".env"


settings = Settings()
