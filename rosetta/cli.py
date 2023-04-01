import argparse


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Translate text using Rosetta")
    parser.add_argument("-i", type=str, help="Current leanguage of the tetx")
    parser.add_argument("-t", type=str, help="Text to translate")
    parser.add_argument("-o", type=str, help="Output leanguage of text")
    return parser.parse_args()
