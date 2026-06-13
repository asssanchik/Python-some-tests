import pytest

from src.baseclasses.response import Response


def test_getting_api_v1_channels(get_api_v1_channels):
    Response(get_api_v1_channels).assert_status_code(200)

