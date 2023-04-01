import argparse
from unittest.mock import patch

from rosetta import cli


@patch('argparse.ArgumentParser.parse_args',
       return_value=argparse.Namespace(i='en', t='Hello world!', o='pt'))
def test_cli(mock_args):
    result = cli.cli()

    assert result.i == 'en'
    assert result.t == 'Hello world!'
    assert result.o == 'pt'
