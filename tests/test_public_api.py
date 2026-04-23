import nekosbest


def test_all_contains_expected_names():
    expected = {
        "__version__",
        "__author__",
        "__copyright__",
        "Client",
        "Dimensions",
        "Result",
        "NekosBestBaseError",
        "NotFound",
        "APIError",
        "ClientError",
    }
    assert set(nekosbest.__all__) == expected


def test_all_is_tuple():
    assert isinstance(nekosbest.__all__, tuple)


def test_every_name_in_all_is_resolvable():
    for name in nekosbest.__all__:
        assert hasattr(nekosbest, name), f"nekosbest.{name} missing"


def test_client_error_is_reexported():
    from nekosbest import ClientError
    from nekosbest.errors import ClientError as _original

    assert ClientError is _original


def test_star_import_exposes_exactly_all():
    ns: dict = {}
    exec("from nekosbest import *", ns)
    public = {k for k in ns if not k.startswith("_")}
    dunders = {k for k in ns if k.startswith("__") and k.endswith("__") and k != "__builtins__"}
    assert public | dunders == set(nekosbest.__all__)
