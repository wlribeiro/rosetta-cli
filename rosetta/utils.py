from urllib.parse import quote


def parse_response(response: dict) -> str:
    text: None | str = None
    data = response.get("data")
    if data:
        text = data.get("translatedText")
    message = response.get("message")
    return text or message


def mount_payload(current_languages: str, target_leaguage: str, text: str) -> str:
    """This method return an stringified url with this format: source_language=en&target_language=pt&text=What%20is%20your%20name%3F"""
    return f"source_language={current_languages}&target_language={target_leaguage}&text={quote(text)}"
