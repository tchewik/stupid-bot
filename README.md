# stupid-bot

Чатбот на регулярных выражениях, моделирующий поведение одного из участников переписки (или переписок).
Опробовать можно здесь: https://tchewik.pythonanywhere.com/ (возможна ненормативная лексика).

Для каждого скрипта в папке tchotchka_with_bot применима команда --help:

python3 tchebot.py --help

HELP

#   option: grab
#   use it only for file splitting, if you have one
#   add your .txt file in the folder and do smth
#   for example
#       $ python3 tchebot.py grab "Елена Чистова" "conversation.txt"
#   so my replics will be added into 'data' file
#   from your conversation
#
#   if you grabbed all your data but bot says he sees nothing,
#   try "question_pack_script.py"
#
#   option: talk
#   use it to talk with bot in command line
#   for example
#       $ python3 tchebot.py talk