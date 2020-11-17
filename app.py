import os
from slack_bolt import App

SLACK_BOT_TOKEN = '[slack-bot-token-here]'
SLACK_SIGNING_SECRET = '[slack-signing-secret-here]'

# Initializes your app with your bot token and signing secret
app = App(
    # token=os.environ.get("SLACK_BOT_TOKEN"),
    # signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

# Exercise 1
# # Listens to incoming messages that contain "hello
# @app.message("hello") # input hello
# def message_hello(message, say):
#     # say() sends a message to the channel where the event was triggered
#     say(f"Hey there <@{message['user']}>!") #example: Hey there @smdelacruz28!

#Exercise2
# Listens to incoming messages that contain "hello"
# @app.message("hello")
# def message_hello(message, say):
#     # say() sends a message to the channel where the event was triggered
#     say(
#         blocks=[
#             {
#                 "type": "section",
#                 "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
#                 "accessory": {
#                     "type": "button",
#                     "text": {"type": "plain_text", "text": "Click Me"},
#                     "action_id": "button_click"
#                 }
#             }
#         ],
#         text=f"Hey there <@{message['user']}>!"
#     )

#Exercise3
# Listens to incoming messages that contain "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3001)))
