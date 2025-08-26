# test_dynaconf

### DISCLAIMER: Knowledge/implementation in this document may not be 100% correct. Do read with cautious. Thank you.

---

My simple attempt to use dynaconf to:

- read environment variables to overwrite config data.
- read `settings.yaml` for config data.
- read `.secrets.toml` for secret data.

### Objective

- To test that data in `settings.yaml` can be overwrite by environment variables.

- To conform to what I think Kubernetes Secret way of doing is,
  - secret data will be store in `.secrets.toml` (or any other file type).
  - secret data must not appear in any other files other than `.secrets.toml`.
  - `.secrets.toml` will not be baked into the image.
  - `.secrets.toml` will only be mounted onto the container at runtime.
  - `SECRETS_PATH` is the environment variable I used to tell the app where the secret volume is.

### Example `.secrets.toml`

```toml
# .secrets.toml
MY_SECRET = "my so called top secret...."
```

### Compose

In `compose.yaml`, the `.secrets.toml` is mounted to `/etc/secret-volume/.secrets.toml`.

Then `/etc/secret-volume/` is injected into the environment variable `SECRETS_PATH`.

Then in `config.py`, dynaconf is configured to read from `/etc/secret-volume/.secrets.toml`.

By doing so, secret data is made available to container only at runtime, hopefully.

### Build Command

```
docker build -t test_dynaconf:latest .
```

### Compose Run Command

```
docker compose run --rm app
```

### Output

#### No Environment Injected and No Secret Volume Mounted

Note that:

- values are all from yaml file.
- value of `MY_SECRET` is None.

```
test_str: some test str at yaml file. | <class 'str'>
TEST_NUM: 1000 | <class 'int'>
test_list: ['yaml_a', 'yaml_b'] | <class 'dynaconf.vendor.box.box_list.BoxList'>
test_obj: {'name': 'yaml name', 'quantity': 1000} | <class 'dynaconf.utils.boxing.DynaBox'>
MY_SECRET: None | <class 'NoneType'>
```

#### Environment Injected and Secret Volume Mounted

Note that:

- value of `test_str` has changed, read from env.
- value of `TEST_NUM` has changed to 2000, read from env.
- value of `test_list` has changed, read from env.
- value of `test_obj` has changed, read from env.
- value of `MY_SECRET` has changed, read from `/etc/secret-volume/.secrets.toml`.

```
test_str: str from env | <class 'str'>
TEST_NUM: 2000 | <class 'int'>
test_list: ['env_a', 'env_b'] | <class 'dynaconf.vendor.box.box_list.BoxList'>
test_obj: {'quantity': 2000, 'name': 'env new name'} | <class 'dynaconf.utils.boxing.DynaBox'>
MY_SECRET: my so called top secret.... | <class 'str'>
```
