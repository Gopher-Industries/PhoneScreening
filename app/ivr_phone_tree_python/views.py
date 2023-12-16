from flask import (
    render_template,
    request,
    url_for,
)
from twilio.twiml.voice_response import VoiceResponse

from ivr_phone_tree_python import app
from ivr_phone_tree_python.view_helpers import twiml


@app.route('/')
@app.route('/ivr')
def home():
    return render_template('index.html')


@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
        num_digits=1, action=url_for('menu'), method="POST"
    ) as g:
        g.say(message="Thanks for calling, if you are above the age of 60, please stay on the line and someone will be with you shortly. If you are a healthcare professional, please press 1 to leave us a message. For any other inquiries, please press 2 to leave a message, we will get back to you as soon as possible.", loop=2)
    return twiml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': _give_instructions}

    if selected_option in option_actions:
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()


def _redirect_welcome():
    response = VoiceResponse()
    response.say("Returning to the main menu",
                 voice="Polly.Amy", language="en-GB")
    response.redirect(url_for('welcome'))

    return twiml(response)
