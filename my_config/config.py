from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix=False,
    # envvar_prefix="",  # export envvars with `export DYNACONF_FOO=bar`.
    settings_files=['my_config\somewhere\config.yaml'],  # Load files in the given order.
)
