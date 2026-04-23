import dataclasses

import pytest

from nekosbest import Dimensions, Result


def _base_payload(**extra):
    data = {
        "url": "https://nekos.best/api/v2/neko/x.png",
        "artist_href": "",
        "artist_name": "",
        "source_url": "",
    }
    data.update(extra)
    return data


def test_result_without_dimensions_has_no_dimensions():
    result = Result(_base_payload())
    assert result.dimensions is None


def test_result_with_dimensions_object_has_dimensions():
    result = Result(_base_payload(dimensions={"width": 1280, "height": 720}))
    assert result.dimensions == Dimensions(width=1280, height=720)


def test_result_matches_real_api_response_shape():
    payload = {
        "artist_name": "ちゃべす",
        "artist_href": "https://twitter.com/tyabesu3",
        "source_url": "https://twitter.com/tyabesu3/status/1746827870016864302",
        "url": "https://nekos.best/api/v2/neko/bc36813f-5b1c-4632-b088-09bd0fde534e.png",
        "dimensions": {"width": 1122, "height": 2048},
    }
    result = Result(payload)
    assert result.dimensions == Dimensions(width=1122, height=2048)


def test_result_with_only_width_in_dimensions_has_no_dimensions():
    result = Result(_base_payload(dimensions={"width": 1280}))
    assert result.dimensions is None


def test_result_with_only_height_in_dimensions_has_no_dimensions():
    result = Result(_base_payload(dimensions={"height": 720}))
    assert result.dimensions is None


def test_result_with_non_mapping_dimensions_has_no_dimensions():
    result = Result(_base_payload(dimensions=None))
    assert result.dimensions is None


def test_dimensions_is_frozen():
    dim = Dimensions(width=1, height=1)
    with pytest.raises(dataclasses.FrozenInstanceError):
        dim.width = 5  # type: ignore[misc]


def test_dimensions_equality_by_value():
    assert Dimensions(1, 2) == Dimensions(1, 2)
    assert Dimensions(1, 2) != Dimensions(2, 1)


def test_dimensions_is_hashable():
    assert hash(Dimensions(1, 2)) == hash(Dimensions(1, 2))
