# -*- coding: utf8 -*-
import codecs, re


def Guy(name, filename):
    try:
        with codecs.open(filename, 'r', encoding='UTF-8') as file:
            stuff = file.read()
            return set(re.findall(name + ' \(.*\):\n(.*)\n\n', stuff))
    except IOError as annoyingshit:
        print(u'Can\'t open the {0} file'.format(annoyingshit.filename))

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

def answer(message):
    filename = 'yell.txt'
    name = 'Елена Чистова'
    bot = Guy(name, filename)
    print('Имеете честь разговаривать с персонажем {}'.format(name))
    used = []
    enough = False
    for word in re.split(r'[., :;]', message):
        keyword = checkQuestion(word.decode('utf8').lower())
        for bullshit in bot:
            if not enough and keyword in u'{}'.format(bullshit.lower()) and not bullshit.lower() in used:
                print(u'{0} <<< {1}'.format(name, bullshit))
                used.append(bullshit.lower())
                enough = True
                break
        if not enough:
            print(u'{0} <<< '.format(name) + u'Да ну тебя')
            break
        else:
            break