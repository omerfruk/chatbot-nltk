from nltk.chat.util import Chat, reflections
from tr_pairs import tr_pairs

chatNltk = Chat(tr_pairs, reflections)

def chat(message):
    return chatNltk.respond(message)
