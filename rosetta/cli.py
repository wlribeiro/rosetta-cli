import argparse


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Translate text using Rosetta")
    parser.add_argument(
        "-i", "--input-language", type=str, help="Current language of the text"
    )
    parser.add_argument("-t", "--text", type=str, help="Text to translate")
    parser.add_argument(
        "-o", "--output-language", type=str, help="Output language of text"
    )
    return parser.parse_args()
