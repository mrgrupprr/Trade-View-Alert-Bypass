from flask import Flask, request, redirect, url_for, render_template
import requests



yourkey = 'test' #here you put your PASSWORD BE SURE IT IS SECURE!!!!!
urlofthepostlink = 'https://3commas.io/trade_signal/trading_view' # this is the link you would normally enter on the tradingview website as the webhook


app = Flask(__name__)

@app.route("/")
def start():
    return 'WELCOME'

@app.route("/tvluxalgo", methods=['GET', 'POST'])
def luxalgo():
    if request.method == 'GET':
        return 'Error 404'
    if request.method == 'POST':
        key = request.args.get('key')
        if key == yourkey:
            requests.post(urlofthepostlink, json={ #ensert here your message that is needed for your trade signal
                "action": "bot",
                "message_type": "bot",
                "bot_id": "8318377",
                "email_token": "CEA9E9E9-E9E9-E9E9-E9E9-E9E9E9E9E9E9", 
                "delay_seconds": 0,
                "pair": "USD_BTC-PERP"
            })
            return 'ok'
            
        else:
            return 'Error 404'

if __name__ == "__main__":
    app.run()