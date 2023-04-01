[translate-api]: https://rapidapi.com/dickyagustin/api/text-translator2
[rapid-api]: https://rapidapi.com/

# Rosetta Stone

Rosetta Stone is a command-line interface (CLI) application that translates text from one language to another using the [Text Translator API][translate-api].

## Installation

To install Rosetta Stone, simply clone the repository and install the dependencies:

```bash
git clone https://github.com/wlribeiro/rosetta-cli.git
cd rosetta-stone
poetry shell
poetry install
```

## Usage

This command sets the current directory as the Python path for your project. Make sure to run this command before executing any scripts or commands related to your project.

The Rosetta Stone CLI provides three command-line arguments that you can use to customize your translations:

(This will translate the text "Hello, how are you?" from English to Spanish.)
```bash
rosetta -i en -t "Hello, how are you?" -o es
```

- `-i` or `--input-language`: Specifies the language of the text you want to translate. For example, if you want to translate text from Spanish to English, you would set the input language to "en".

- `-t` or `--text`: Specifies the text you want to translate.

- `-o` or `--output-language`: Specifies the language you want to translate the text to. For example, if you want to translate text from English to Spanish, you would set the output language to "es".

## Running

To use Rosetta Stone with the Text Translator API, you need to create an account on [RapidAPI][rapid-api] and generate an access token for the [Text Translator API][translate-api]. Once you have the access token, create a .env file in the root directory of your project and add the following line to it:

```bash
cp .evn.example .env
```

Replace your_api_key_here with the actual access token generated from RapidAPI. This will allow your project to use the Text Translator API to translate the text.

```bash
API_KEY=your-secrete-api-key
```

You can run the rosetta command without building the project by using the following command:

```bash
python rosetta -i en -t "Hello, how are you?" -o es
```

### Building

To build the project and generate a distribution package, run the following command:

```bash
poetry build
```

This will generate a distribution package in the dist/ directory.

To install the package globally, run:

```bash
pip install .
```

Alternatively, you can install the package directly from the distribution package by running:

```bash
pip install dist/rosetta_stone-<version>-py3-none-any.whl
```

or

```bash
poetry add
```

And run the `rosetta` using the following command:

```bash
rosetta -i en -t "Hello, how are you?" -o es
```

## Contributing

If you'd like to contribute to Rosetta Stone, please submit a pull request! We welcome contributions of all kinds, from bug reports to feature requests to code changes.
