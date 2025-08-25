from my_config.config import settings
from pprint import pprint

def _print(value):
    print(f"{value} | {type(value)}")


def main():
    # pprint(settings.__dict__)
    _print(settings.name)
    _print(settings.PORT)

    # auto mapped to env TEST_LIST
    # need to use @json syntax
    # eg.:
    # - TEST_LIST="@json [true, false]"
    # - TEST_LIST="@json ['a']"
    # - TEST_LIST="@json [9, 8, 7, 6]"
    _print(list(settings.test_list))

    # auto mapped to env TEST_OBJ__NAME and TEST_OBJ__QUANTITY
    _print(dict(settings.test_obj))

if __name__ == "__main__":
    main()
