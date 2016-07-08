# -*- coding: utf8 -*-
import codecs, re
import os.path, sys
BASE = os.path.dirname(os.path.abspath(__file__))


# use it only for file splitting, if you have one
# add your .txt file in the folder and do
# python3 tchebot.py 'Елена Чистова' 'conversation'
# so my replics will be added into 'bot_replics.txt'
# from your conversation
def Guy(name, filename):
    try:
        with codecs.open(os.path.join(BASE, filename), 'r', encoding='UTF-8') as file:
            stuff = file.read()
            with codecs.open(os.path.join(BASE, 'bot_replics.dat'), 'a') as out:
                for str in re.findall(name + ' \(.*\):\n(.*)\n\n', stuff):
                    out.write('\n'+str)
            return set(re.findall(name + ' \(.*\):\n(.*)\n\n', stuff))
    except IOError as annoyingshit:
        print(u'Can\'t open the {0} file'.format(annoyingshit.filename))
        sys.exit(0)

QUESTIONS = {
    u'почему':u'потому что',
    u'зачем':u'затем',
    u'когда':u'тогда, '
}

def checkQuestion(keyword):
    try:
        return QUESTIONS[keyword]
    except KeyError:
        return keyword


CRITICAL_COUNTER = 0
def answer(message):
    name = 'Елена Чистова'
    filename = 'yell.txt'
    print('Имеете честь разговаривать с персонажем {}'.format(name))
    used = []
    enough = False
    try:
        with codecs.open(os.path.join(BASE, 'bot_replics.txt'), 'r') as bot:
            print("TYPE OF message: ", type(message))
            yourWords = re.split(r'[., :;]', str(message))
            for word in yourWords:
                keyword = checkQuestion(word.lower())
                for bullshit in bot:
                    if not enough and keyword in u'{}'.format(bullshit.lower()) and not bullshit.lower() in used:
                        used.append(bullshit.lower())
                        return (u'{}'.format(bullshit))
                if not enough:
                    print(u'{0} <<< '.format(name) + u'Да ну тебя')
                    break
                else:
                    break
        return u'Извините, я у бабушки'
    except IOError as notbotreplics:
        print(">>>TROUBLES WITH OPEN bot_replics.txt, SIR. TRY AGAIN")

if __name__ == "__main__":
    if (sys.argv[-1] == '--help'):
        print( "\
            \n#\tuse it only for file splitting, if you have one\
            \n#\tadd your .txt file in the folder and do smth like\
            \n#\
            \n#\tpython3 tchebot.py 'Елена Чистова' 'conversation'\
            \n#\
            \n#\tso my replics will be added into 'bot_replics.txt'\
            \n#\tfrom your conversation\n")
    else:
        print("\nuse --help for information\n")
    if len(sys.argv) == 3:
        Guy(str(sys.argv[1]), str(sys.argv[2]))