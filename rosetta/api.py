import requests


from rosetta import config


def post_translate(payload: str) -> dict:
    try:
        response = requests.post(config.URL, data=payload, headers=config.HEADERS)
        return response.json()
    except ValueError as e:
        return e


def get_leanguages() -> list[dict]:
    pass
