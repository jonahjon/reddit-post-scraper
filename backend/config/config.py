from pydantic import BaseSettings
import praw

class Settings(BaseSettings):
    client_id: str = "Awesome API"
    client_secret: str = "Awesome secret"
    user_agent: str = "Awesome agent"

    class Config:
        env_file = ".env"


settings = Settings()


reddit = praw.Reddit(client_id=settings.client_id,
                     client_secret=settings.client_secret,
                     user_agent=settings.user_agent)

