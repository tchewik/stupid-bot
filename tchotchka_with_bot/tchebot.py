# -*- coding: utf8 -*-
import codecs, re
import os.path, sys
BASE = os.path.dirname(os.path.abspath(__file__))
import random
import pickle, json
#import base_of_shit


class Tchebot:
    data = []
    file_data = 'data'

    def __init__(self):
        try:
            with open(os.path.join(BASE, self.file_data), 'rb+') as file_data:
                self.data = pickle.load(file_data)
            with open(os.path.join(BASE, 'answers.json'), 'r+') as file_dict:
                self._questions = json.load(file_dict)
        except IOError:
            print("can't find data, please, use 'grab' option or type '--help'")


    def grab(self, name, filename):
        # use it only for file splitting, if you have one
        # add your .txt file in the folder and do
        # python3 tchebot.py 'Елена Чистова' 'conversation'
        # so my replics will be added into 'bot_replics.txt'
        # from your conversation
        try:
            with codecs.open(os.path.join(BASE, filename), 'r', encoding='UTF-8') as file:
                console_counter = 0
                for sentence in re.findall(name + ' \(.*\):\n([^(http)/]+)\n\n', file.read()):
                    if len(sentence) > 5:
                        sentence = re.split(r'[^a-zа-яё\-]', sentence.lower())  # tokenize a sentence
                        for trash in ['']:
                            while trash in sentence:
                                sentence.remove(trash)
                        self.data.append(sentence)
                        console_counter += 1
                        if console_counter % 500 == 0:
                            print(">>> successfully added string {0} in dataset".format(console_counter))

                with open(os.path.join(BASE, self.file_data), 'wb+') as file:  # write in a binary file
                    pickle.dump(self.data, file)

        except IOError as annoyingshit:
            print(u'Can\'t open the {0} file'.format(annoyingshit.filename))
            sys.exit(0)

    def _checkQuestion(self, keyword):
        for key in self._questions.keys():
            if re.match(key, keyword, re.IGNORECASE):
                return self._questions[key][random.randint(0, len(self._questions[key]) - 1)]
        return keyword

    def reply(self, message, used=[]):
        try:
            #allbullshit = tchewik.readlines()
            random.shuffle(self.data)
            yourWords = re.split(r'[^a-zа-яё\-]', message.lower())
            while '' in yourWords:
                yourWords.remove('')

            for word in yourWords:
                keyword = self._checkQuestion(word.lower())
                for bullshit in self.data:
                    bullshit = ' '.join(bullshit)  # костыль, временный.
                    if not bullshit in used and re.match(keyword, bullshit, re.IGNORECASE):
                        return bullshit
            return ' '.join(self.data[random.randint(0, len(self.data))])
        except IOError:
            print(">>> TROUBLES WITH OPEN bot_replics.txt, SIR. TRY TO START tchebot.py FROM COMMAND LINE")
            return 'Чего-то пошло не так. Попробуй вживую.'

def help():
    with codecs.open(os.path.join(BASE, 'help'), 'r', encoding='UTF-8') as help_file:
        print(help_file.read())
    sys.exit(0)

if __name__ == "__main__":

    if len(sys.argv) > 1 and '--help' in sys.argv:
        help()
    else:
        print("\nuse --help for information\n")
        tchebot = Tchebot()

        if len(sys.argv) == 4 and str(sys.argv[1]) == 'grab':
            tchebot.grab(str(sys.argv[2]), str(sys.argv[3]))
            print("\nfile {} was successfully grabbed!\n".format(sys.argv[3]))

        elif len(sys.argv) > 1 and 'talk' in sys.argv:
            while(True):
                print(u"<<<", tchebot.reply(input('>>> ')))