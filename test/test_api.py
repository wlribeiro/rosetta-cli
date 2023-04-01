from unittest.mock import Mock, patch
import requests
from rosetta import api, config


def test_post_translate():
    mock_response = Mock()
    mock_response.json.return_value = {"data": {"translatedText": "Olá Mundo!"}}

    with patch.object(requests, "post", return_value=mock_response) as mock_post:
        result = api.post_translate(
            "source_language=en&target_language=pt&text=Hello%20World!"
        )

        mock_post.assert_called_once_with(
            config.URL,
            data="source_language=en&target_language=pt&text=Hello%20World!",
            headers=config.HEADERS,
        )

        assert result == {"data": {"translatedText": "Olá Mundo!"}}
