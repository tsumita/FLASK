from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('P0eCTrGuCAvmYCdGFTGKa9LfM+MR6z0jOxfqG7pGPV3Ymny8CyOWUykRQLoy4GlxjRTOJFPwS+BjhGz8Z8+rrsxUH5V/jUMpuCMMu9KdIRmKqLSUS/epHpCOSy7PVF/FOTiaB+FD/NA2/DHu8lZnuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('86ec35a0a93202548bff5d343ea33a02')

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()