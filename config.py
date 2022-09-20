from typing import Optional, Literal
from appium.options.android import UiAutomator2Options
import pydantic

from utils import path

EnvContext = Literal['personal', 'test', 'stage', 'prod']


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'personal'

    # --- Appium Capabilities ---
    platform_name: str = 'android'
    platform_version: str = '9.0'
    device_name: str = 'Google Pixel 3'
    app: Optional[str] = None
    app_name: Optional[str] = None

    # --- > BrowserStack Capabilities ---
    project_name: Optional[str] = None
    build_name: Optional[str] = None
    session_name: Optional[str] = None
    # --- > > BrowserStack credentials---
    user_name: Optional[str] = None
    access_key: Optional[str] = None

    # --- Remote Driver ---
    remote_url: str = 'http://127.0.0.1:4723/wd/hub'  # it's a default appium server url

    # --- Selene ---
    timeout: float = 6.0

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        options.device_name = self.device_name
        options.platform_name = self.platform_name
        options.app = self.app
        if 'hub.browserstack.com' in self.remote_url:
            options.load_capabilities(
                {
                    'platformVersion': self.platform_version,
                    'bstack:options': {
                        'projectName': self.project_name,
                        'buildName': self.build_name,
                        'sessionName': self.session_name,
                        'userName': self.user_name,
                        'accessKey': self.access_key,
                    },
                }
            )

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        """
        factory method to init Settings with values from corresponding .env file
        """
        asked_or_current = env or cls().context
        return cls(
            _env_file=path.abs_path_from_project(
                f'config.{asked_or_current}.env'
            )
        )


settings = Settings.in_context()


