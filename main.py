from config import settings
from pprint import pprint

def _print(key):
    value = settings.get(key, None)
    if isinstance(value, list):
        print(f"{key}: {list(value)} | {type(value)}")
    elif isinstance(value, dict):
        print(f"{key}: {dict(value)} | {type(value)}")
    else:
        print(f"{key}: {value} | {type(value)}")


def main():
    # pprint(settings.__dict__)
    _print("test_str")
    _print("TEST_NUM")

    # auto mapped to env TEST_LIST
    # need to use @json syntax
    # eg.:
    # - TEST_LIST="@json [true, false]"
    # - TEST_LIST="@json ['a']"
    # - TEST_LIST="@json [9, 8, 7, 6]"
    # _print(list(settings.test_list))
    _print("test_list")

    # auto mapped to env TEST_OBJ__NAME and TEST_OBJ__QUANTITY
    # _print(dict(settings.test_obj))
    _print("test_obj")

    _print("MY_SECRET")

if __name__ == "__main__":
    main()
