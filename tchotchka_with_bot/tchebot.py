# -*- coding: utf8 -*-
import codecs, re
import os.path, sys
BASE = os.path.dirname(os.path.abspath(__file__))


def Guy(name, filename):
    try:
        with codecs.open(os.path.join(BASE, filename), 'r', encoding='UTF-8') as file:
            stuff = file.read()
            with codecs.open(os.path.join(BASE, 'bot_replics.txt'), 'a') as out:
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
        global CRITICAL_COUNTER
        if CRITICAL_COUNTER <= 4:
            CRITICAL_COUNTER += 1
            botreplics = Guy(name, filename)
            answer(message)
        else:
            sys.exit(0)

if __name__ == "__main__":
    answer('Hi')