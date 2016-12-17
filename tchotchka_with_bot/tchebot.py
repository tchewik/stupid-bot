# -*- coding: utf-8 -*-
import codecs, re
import os.path, sys
import random
import pickle, json
#import base_of_shit


BASE = os.path.dirname(os.path.abspath(__file__))
FILE_TIP = 'res/tip.dat'
FILE_HELP = 'res/help.dat'
FILE_AVOID = 'res/avoid.dat'

class Tchebot:
    data = []
    FILE_DATA = 'res/data.dat'
    FILE_ANSWERS = 'res/answers.json'
    FILE_AVOID = 'res/avoid.dat'

    def __init__(self):
        try:
            with open(os.path.join(BASE, self.FILE_DATA), 'rb+') as file_data:
                self.data = pickle.load(file_data)
            with open(os.path.join(BASE, self.FILE_ANSWERS), 'r+') as file_dict:
                self._questions = json.load(file_dict)
        except IOError:
            print("can't find data, please, use 'grab' option or type '--help'")

    def grab(self, name, filename):
        try:
            with codecs.open(os.path.join(BASE, filename), 'r', encoding='UTF-8') as file:
                console_counter = 0
                for sentence in re.findall(name + ' \(.*\):\n([^(http)/]+)\n\n', file.read()):
                    if len(sentence) > 5:
                        sentence = re.split(r'[^a-zа-яё\-]', sentence.lower())  # tokenize a sentence
                        avoid_data = ['']
                        try:
                            with codecs.open(os.path.join(BASE, FILE_AVOID), 'r', encoding='UTF-8') as file_avoid:
                                avoid_data = re.split(r'[^a-zа-яё\-]', file_avoid.read().lower())
                        except IOError as annoyingshit:
                            print(u'Can\'t open the {0} file'.format(annoyingshit.filename))

                        for trash in avoid_data:
                            while trash in sentence:
                                sentence.remove(trash)
                                
                        self.data.append(sentence)
                        console_counter += 1
                        if console_counter % 500 == 0:
                            print(">>> successfully added string {0} in dataset".format(console_counter))

                with open(os.path.join(BASE, self.FILE_DATA), 'wb+') as file:  # write in a binary file
                    pickle.dump(self.data, file)
                print("\nfile {} was successfully grabbed!\n".format(sys.argv[3]))

        except IOError as annoyingshit:
            print(u'Can\'t open the {0} file'.format(annoyingshit.filename))
            sys.exit(0)

    def _checkQuestion(self, keyword):
        try:
            for key in self._questions.keys():
                    if re.match(key, keyword, re.IGNORECASE):
                        return self._questions[key][random.randint(0, len(self._questions[key]) - 1)]
            return keyword
        except AttributeError:
                sys.exit(0)

    def reply(self, message, used=[]):
        try:
            random.shuffle(self.data)
            yourWords = re.split(r'[^a-zа-яё\-]', message.lower())
            while '' in yourWords:
                yourWords.remove('')

            keyword = self._checkQuestion(' '.join(yourWords))  # костыль, да
            for bullshit in self.data:
                bullshit = ' '.join(bullshit)  # костыль, временный.
                if not bullshit in used and re.match(keyword, bullshit, re.IGNORECASE):
                    return bullshit
            return ' '.join(self.data[random.randint(0, len(self.data))])
        except IOError:
            print(">>> TROUBLES WITH OPEN bot_replics.txt, SIR. TRY TO START tchebot.py FROM COMMAND LINE")
            return 'Чего-то пошло не так. Попробуй вживую.'


def tip():
    with codecs.open(os.path.join(BASE, FILE_TIP), 'r', encoding='UTF-8') as file_tip:
        print(file_tip.read())

def help():
    with codecs.open(os.path.join(BASE, FILE_HELP), 'r', encoding='UTF-8') as file_help:
        print(file_help.read())
    sys.exit(0)

def reply(sentence, escape_list):
    tchebot = Tchebot()
    return tchebot.reply(sentence, escape_list)

if __name__ == "__main__":
    if len(sys.argv) > 1 and '--help' in sys.argv:
        help()
    else:
        tip()
        tchebot = Tchebot()

        if len(sys.argv) == 4 and str(sys.argv[1]) == 'grab':
            tchebot.grab(str(sys.argv[2]), str(sys.argv[3]))

        elif len(sys.argv) > 1 and 'talk' in sys.argv:
            while(True):
                print(u"<<<", tchebot.reply(input('>>> ')))