import json
from flask import Flask
from flask import render_template
import telebot

bot = telebot.TeleBot("5987185300:AAFnRyCQt2-wCJzoDnG138I1M4rcpCyjS8s")
user_id = "254382041"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/processInfo/<string:info>', methods=['POST'])
def process(info):
    info = json.loads(info)
    info = info.split(" ")
    data = {"Processor": info[0], "OS": info[1]}
    bot.send_message(user_id, str(data))
    return 'Done'


if __name__ == '__main__':
    app.run(debug=True)
