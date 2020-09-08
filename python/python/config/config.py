from pydantic import BaseSettings

class Settings(BaseSettings):
    client_id: str = "Awesome API"
    client_secret: str = "Awesome secret"
    user_agent: str

    class Config:
        env_file = ".env"
        
settings = Settings()
