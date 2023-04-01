from rosetta.utils import parse_response, mount_payload


def test_parse_response():
    mock_response1 = {"data": {"translatedText": "Bonjour"}}
    mock_response2 = {"message": "API error"}

    assert parse_response(mock_response1) == "Bonjour"
    assert parse_response(mock_response2) == "API error"


def test_mount_payload():
    current_language = "en"
    target_language = "fr"
    text = "Hello World"

    expected_payload = "source_language=en&target_language=fr&text=Hello%20World"
    assert mount_payload(current_language, target_language, text) == expected_payload
