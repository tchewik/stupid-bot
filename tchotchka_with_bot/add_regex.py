import sys
import json
import os
BASE = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    if 'show' in sys.argv:
        with open(os.path.join(BASE, 'answers.json'), 'r') as file:
            questions = json.load(file)
            print(json.dumps(questions, ensure_ascii=False, sort_keys=True, indent=4))
        sys.exit(0)
    if 'remove' in sys.argv:
        with open(os.path.join(BASE, 'answers.json'), 'r') as file:
            questions = json.load(file)
        questions.pop(sys.argv[2], None)
        with open(os.path.join(BASE, 'answers.json'), 'w+') as file:
            json.dump(questions, file)
        print('\nDONE: remove {}'.format(sys.argv[-1]))
        sys.exit(0)
    if len(sys.argv) > 1:
        with open(os.path.join(BASE, 'answers.json'), 'r') as file:
            questions = json.load(file)
        questions[sys.argv[1]] = sys.argv[2]
        with open(os.path.join(BASE, 'answers.json'), 'w+') as file:
            json.dump(questions, file)
    else:
        print("\ntype key and all the items in a string to add it\
              \nexample:\
              \n$ python3 add_regex.py 'Привет.*' 'Прощай.*' '.*потому что.*'\
              \n\
              \nor type key to remove it\
              \nexample:\
              \n$ python3 add_regex.py remove 'Привет.*'")