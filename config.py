from dynaconf import Dynaconf
import os


SECRETS_PATH = os.getenv("SECRETS_PATH", default="")

settings = Dynaconf(
    envvar_prefix=False,
    # envvar_prefix="",  # export envvars with `export DYNACONF_FOO=bar`.
    settings_files=[
        "settings.yaml",
        f"{SECRETS_PATH}.secrets.toml"
    ],  # Load files in the given order.
)
