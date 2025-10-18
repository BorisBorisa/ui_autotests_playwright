from enum import Enum
from typing import Self

from pydantic import BaseModel, FilePath, EmailStr, HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    zip_code: str


class TestData(BaseModel):
    invalid_email: str
    invalid_password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    base_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    @property
    def get_base_url(self):
        return str(self.base_url)

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("./.auth/browser-state.json")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.parent.mkdir(parents=True, exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        )


settings = Settings.initialize()
