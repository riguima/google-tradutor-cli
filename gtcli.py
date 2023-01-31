from argparse import ArgumentParser
from googletrans import Translator


def get_terminal_arguments():
    argument_parser = ArgumentParser(description='Translate texts.')
    argument_parser.add_argument('text', help='text that will be translated')
    argument_parser.add_argument(
        '-d', default='pt', help='to which language will it be translated'
    )
    return argument_parser.parse_args()


def translate(text, dest):
    return Translator().translate(text, dest=dest).text


if __name__ == '__main__':
    args = get_terminal_arguments()
    translated_text = translate(args.text, args.d)
    print(translated_text)
