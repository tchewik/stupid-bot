# -*- coding: utf8 -*-
import codecs, re
import os.path, sys
BASE = os.path.dirname(os.path.abspath(__file__))
import random
#from . import base_of_shit


# use it only for file splitting, if you have one
# add your .txt file in the folder and do
# python3 tchebot.py 'Елена Чистова' 'conversation'
# so my replics will be added into 'bot_replics.txt'
# from your conversation
def Guy(name, filename):
    try:
        with codecs.open(os.path.join(BASE, filename), 'r', encoding='UTF-8') as file:
            stuff = file.read()
            with codecs.open(os.path.join(BASE, 'bot_replics.txt'), 'a') as out:
                for str in re.findall(name + ' \(.*\):\n(.*)\n\n', stuff):
                    if not avoid(str):
                        out.write('\n'+str)
    except IOError as annoyingshit:
        print(u'Can\'t open the {0} file'.format(annoyingshit.filename))
        sys.exit(0)


def avoid(str):
    shit = base_of_shit.shit

    for regularochka in shit:
        if re.match(regularochka, str, re.IGNORECASE):
            return True
    return False


QUESTIONS = {
    r'^почему.*':[
        r'потому как',
    ],
    r'^зачем.*':[
        'потому что',
    ],
    r'^когда.*':[
        'когда .*ет',
    ],
    r'^кого.*':[
        'тебя.?$',
        'его.?$',
        '\b.*ну',
    ],
    r'^кому.*':[
        r'ему.?$',
        r'ей.?$',
        r'мне.?$'
    ],
    r'.*ила':[
        r'.*зачем .*ила.*',
    ],
    r'пиздец':[
        r'^[А-Яа-я]*ец',
    ],
    r'блять':[
        r'спокой',
    ],
    r'.*ть\b':[
        r'мило',
    ],
    r'.*хочу .*ся':[
        r'палец',
    ],
    r'нравится':[
        r'как .*к\b',
    ],
    r'кот.*':[
        r'сорок\b',
    ],
    r'кош.*':[
        r'\bнезависим.*',
    ],
    r'.*аха.*':[
        r'смеш.*',
    ],
    r'кек':[
        r'.*ао',
    ],
    r'.*ы кт.*':[
        r'.*не.*жопа.*',
    ],
    r'.*да.*':[
        r'^нет[\.,!?].*',
    ],
    r'.*нет.*':[
        r'^да[\.,!?].*',
    ],
    r'(.*здравствуй.*)|(.*прив.*)':[
        r'^добрый .*',
        r'^доброе .*',
        r'^здравствуйте.*',
        r'^привет.*',
    ],
    r'(.*как дел.*)|(.*как ты.*)|(.*как жизн.*)':[
        r'^как у .*',
        r'^пизд.*',
        r'хорошо.*',
        r'.*норм.*',
        r'отлич.*',
    ],
    r'(как.*зовут.*)|(.*звать.*)':[
        r'лена.*',
    ],
    r'(ч.*делаешь.*)|(ч.*маешься)|(ч.*кодишь)':[
        r'.*аю.*',
        r'.*сплю.*',
    ],
    r'(.*где.*)':[
        r'^в .*',
    ]
}


def checkQuestion(keyword):
    for key in QUESTIONS.keys():
        if re.match(key, keyword, re.IGNORECASE):
            return QUESTIONS[key][random.randint(0, len(QUESTIONS[key]) - 1)]
    return keyword


def answer(message, ignore=[]):
    try:
        with codecs.open(os.path.join(BASE, 'bot_replics.txt'), 'r') as tchewik:
            allbullshit = tchewik.readlines()
            yourWords = message

            keyword = checkQuestion(yourWords.lower())
            for bullshit in allbullshit:
                if re.match(keyword, bullshit, re.IGNORECASE):
                    return (u'{}'.format(bullshit))
            return allbullshit[random.randint(0, len(allbullshit))]
    except IOError:
        print(">>> TROUBLES WITH OPEN bot_replics.txt, SIR. TRY TO START tchebot.py FROM COMMAND LINE")
        return 'Чего-то пошло не так. Попробуй вживую.'


if __name__ == "__main__":
    if (sys.argv[-1] == '--help'):
        print( "\
            \n#\tHELP\
            \n#\
            \n#\toption: grab\
            \n#\tuse it only for file splitting, if you have one\
            \n#\tadd your .txt file in the folder and do smth like\
            \n#\
            \n#\tpython3 tchebot.py grab 'Елена Чистова' 'conversation'\
            \n#\tso my replics will be added into 'bot_replics.txt'\
            \n#\tfrom your conversation\n\
            \n#\
            \n#\toption: talk\
            \n#\tuse it to talk with bot in command line like\
            \n#\
            \n#\tpython3 tchebot.py talk\
            \n#")
        sys.exit(0)
    else:
        print("\nuse --help for information\n")
    if len(sys.argv) == 4 and str(sys.argv[1]) == 'grab':
        Guy(str(sys.argv[2]), str(sys.argv[3]))
        print("\nfile {} was successfully grabbed!".format(sys.argv[3]))
    elif str(sys.argv[1] == 'talk'):
        while(True):
            print(answer(input()))