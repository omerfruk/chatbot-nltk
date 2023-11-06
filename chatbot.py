from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request, jsonify

pairs = [
    ["my name is (.*)", ["Hello %1, How are you today ?",]],
    ["(hi|hello|hey|holla|hola)", ["Hello", "Hey there",]],
    ["(.*) in (.*) is fun", ["%1 in %2 is indeed fun",]],
    ["(.*)(location|city) ?", 'Tokyo, Japan',],
    ["(.*) created you ?", ["I was created by a team of engineers at DSC NIT Rourkela",]],
    ["how is the weather in (.*)?", ["The weather in %1 is amazing like always",]],
    ["(.*)help(.*)", ["I can help you ",]],
    ["(.*) your name ?", ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]],
    ["(.*) thank (.*)", ["You're welcome",]],
    ["(.*) your age ?", ["I'm a very young chatbot",]],
    ["(.*) (sports|game) ?", ["I'm a very big fan of Football",]],
    ["who (.*) (moviestar|actor)?", ["Zendaya"]],
    ["quit", ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]],
    ["(.*)", ["That is nice to hear"]],
]

app = Flask(__name__, template_folder='template')
chatNltk = Chat(pairs, reflections)


@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    print(user_message)

    resp = chatNltk.respond(user_message)
    print(resp)
    return jsonify({'bot_response': resp})

if __name__ == '__main__':
    app.run(debug=True)



# def chatbot():
#     print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#     chat = Chat(pairs, reflections)
#     resp = chat.respond("My name is omer")
#     print(resp)
#     chat.converse(quit="quit")
#
# if __name__ == "__main__":
#     chatbot()