[translate-api]: https://rapidapi.com/dickyagustin/api/text-translator2

# Rosetta Stone

Rosetta Stone is a command-line interface (CLI) application that translates text from one language to another using the [Text Translator API][translate-api].

## Installation

To install Rosetta Stone, simply clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/rosetta-stone.git
cd rosetta-stone
poetry shell
poetry install
```
## Usage
In some cases, you may need to specify the Python path of your project. To do this, you can use the export command in your terminal:
```bash
export PYTHONPATH=.
```
This command sets the current directory as the Python path for your project. Make sure to run this command before executing any scripts or commands related to your project.

The Rosetta Stone CLI provides three command-line arguments that you can use to customize your translations:

- `-i` or `--input-language`: Specifies the language of the text you want to translate. For example, if you want to translate text from Spanish to English, you would set the input language to "en".

- `-t` or `--text`: Specifies the text you want to translate.

- `-o` or `--output-language`: Specifies the language you want to translate the text to. For example, if you want to translate text from English to Spanish, you would set the output language to "es".
 
To use Rosetta Stone, run the rosetta command followed by the current language, the text to translate, and the target language.

```bash
rosetta -i en -t "Hello, how are you?" -o es
```
This will translate the text "Hello, how are you?" from English to Spanish.


## Contributing

If you'd like to contribute to Rosetta Stone, please submit a pull request! We welcome contributions of all kinds, from bug reports to feature requests to code changes.