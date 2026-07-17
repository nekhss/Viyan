from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "VIYAN"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str
    NASA_API_KEY: str = ""
    CELESTRAK_URL: str = ""
    MCP_SERVER_URL: str = ""

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
    }


settings = Settings()
