import sys
import json
import os


BASE = os.path.dirname(os.path.abspath(__file__))
FILE_ANSWERS = 'res/answers.json'
FILE_HELP = 'res/rgxhelp.dat'


def help():
  
    with codecs.open(os.path.join(BASE, FILE_HELP), 'r', encoding='UTF-8') as file_help:
        print(file_help.read())

    sys.exit(0)


if __name__ == "__main__":

    if 'show' in sys.argv:
        with open(os.path.join(BASE, FILE_ANSWERS), 'r') as file:
            questions = json.load(file)
            print(json.dumps(questions, ensure_ascii=False, sort_keys=True, indent=4))

        sys.exit(0)

    if 'remove' in sys.argv:
        with open(os.path.join(BASE, FILE_ANSWERS), 'r') as file:
            questions = json.load(file)
        questions.pop(sys.argv[2], None)

        with open(os.path.join(BASE, FILE_ANSWERS), 'w+') as file:
            json.dump(questions, file)
        print('\nDONE: remove {}'.format(sys.argv[-1]))

        sys.exit(0)

    if len(sys.argv) > 1 and not '--help' in sys.argv:

        with open(os.path.join(BASE, FILE_ANSWERS), 'r') as file:
            questions = json.load(file)
        questions[sys.argv[1]] = []

        for item in sys.argv[2:]:
            questions[sys.argv[1]].append(item)

        with open(os.path.join(BASE, FILE_ANSWERS), 'w+') as file:
            json.dump(questions, file)

        print('\nDONE: add answers for key {}'.format(sys.argv[1]))

    else:
        help()