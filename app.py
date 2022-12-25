import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message, send_image_message,send_text_message_AI



load_dotenv()


machine = TocMachine(
    states=["user", "menu", "movie", "eat", "work_out", "meal", "drink", "dessert", "show_fsm", "random_meal", "random_dessert", "random_drink", "fifteen", "twenty"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {  # movie <->selection
            "trigger": "advance",
            "source": "menu",
            "dest": "movie",
            "conditions": "is_going_to_movie",
        },
        { 
            "trigger": "advance",
            "source": "movie",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # show_fsm <-> selection
            "trigger": "advance",
            "source": "menu",
            "dest": "show_fsm",
            "conditions": "is_going_to_show_fsm",
        },
        { 
            "trigger": "advance",
            "source": "show_fsm",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        
        { # eat <-> selection
            "trigger": "advance",
            "source": "menu",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "eat",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # work_out <-> selection
            "trigger": "advance",
            "source": "menu",
            "dest": "work_out",
            "conditions": "is_going_to_work_out",
        },
        { 
            "trigger": "advance",
            "source": "work_out",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # eat <-> meal
            "trigger": "advance",
            "source": "eat",
            "dest": "meal",
            "conditions": "is_going_to_meal",
        },
        { 
            "trigger": "advance",
            "source": "meal",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "eat",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {   "trigger": "advance",
            "source": "meal",
            "dest": "random_meal",
            "conditions": "is_going_random_meal",   
        },
        { 
            "trigger": "advance",
            "source": "random_meal",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # eat <-> drink
            "trigger": "advance",
            "source": "eat",
            "dest": "drink",
            "conditions": "is_going_to_drink",
        },
        { 
            "trigger": "advance",
            "source": "drink",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        {   "trigger": "advance",
            "source": "drink",
            "dest": "random_drink",
            "conditions": "is_going_to_random_drink",   
        },
        { 
            "trigger": "advance",
            "source": "random_drink",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "random_drink",
            "dest": "drink",
            "conditions": "is_going_to_drink",
        },
        { # eat <-> dessert
            "trigger": "advance",
            "source": "eat",
            "dest": "dessert",
            "conditions": "is_going_to_dessert",
        },
        { 
            "trigger": "advance",
            "source": "dessert",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "random_dessert",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        {   "trigger": "advance",
            "source": "dessert",
            "dest": "random_dessert",
            "conditions": "is_going_to_random_dessert",   
        },
        {   "trigger": "advance",
            "source": "random_dessert",
            "dest": "dessert",
            "conditions": "is_going_to_dessert",   
        },
        { 
            "trigger": "advance",
            "source": "work_out",
            "dest": "fifteen",
            "conditions": "is_going_to_fifteen",
        },
        { 
            "trigger": "advance",
            "source": "fifteen",
            "dest": "work_out",
            "conditions": "is_going_to_work_out",
        },
         { 
            "trigger": "advance",
            "source": "work_out",
            "dest": "twenty",
            "conditions": "is_going_to_twenty",
        },
        { 
            "trigger": "advance",
            "source": "twenty",
            "dest": "work_out",
            "conditions": "is_going_to_work_out",
        },
        { ######
            "trigger": "advance", 
            "source": ["menu", "work_out" "movie", "show_fsm", "meal", "drink", "dessert", "random_meal", "random_dessert", "random_drink"], 
            "dest": "menu",
            "conditions": "is_go_back"
            
        },
        { ######
            "trigger": "advance", 
            "source": ["menu", "work_out" "movie", "show_fsm", "meal", "drink", "dessert", "random_meal", "random_dessert", "random_drink", "fifteen", "twenty"], 
            "dest": "menu",
            "conditions": "is_going_to_menu"
            
        },
       
       
    ],
    initial="user",
    auto_transitions=False,
    #show_conditions=True,
)

app = Flask(__name__, static_url_path="")



# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)


line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

#mode = 0 # mode 0




@app.route("/callback", methods=["POST"])
def callback():
    #global mode
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        '''
        if not isinstance(event.message.text, str):
            continue
        print(f'\nFSM STATE: {machine.state}')
        print(f'REQUEST BODY: \n{body}')
        '''
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    #global mode

    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")
        print(f"\nafter FSM STATE: {machine.state}")
        

        
    return "OK"


'''
@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")
'''

'''
@app.add(MessageEvent, message = TextMessage)
def handle_message(event):
    message = text = event.message.text
'''





if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
