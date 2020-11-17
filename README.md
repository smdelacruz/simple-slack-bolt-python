# Simple Slack App - using Bolt

This project followed the tutorial from [Bolt with Python](https://slack.dev/bolt-python/concepts#basic)

A simple app that uses bolt for Python.

## Pre-requisite

1. Create a [slack app](https://api.slack.com/apps?new_app=1). There should be a 'SigninSecret' and 'BotToken'.
2. Install [ngrok](https://api.slack.com/tutorials/tunneling-with-ngrok) to test app on your local machine.
    - After installation, add to PATH
    - Execute the command `ngrok http 3001`. Session status should be online. Copy the forwarding URL, for example is 
    http://4e4652ccb589.ngrok.io
        

## Configure Slack app
Go to your **Slack App Settings**.

On the left side find, **Event Subscriptions**
1. Toggle to On
2. Add the ngrok forwarding Url and add _'/slack/events/'_ at the end of the URL
3. Subscribe to bot events, add the following then Save Changes.
 - message.channels
 - message.groups
 - message.im
 - message.mpim

On the left side find, **Interactivity & Shortcuts**
1. Toggle to On
2. Add the ngrok forwarding Url and add _'/slack/events/'_ at the end of the URL
3. Save Changes.

## Test
```bash
python app.py
```
Should show  `Bolt app is running! (development server)`
Test on Slack.

## Usage
Uncomment each Exercise 1,2,3 and see the different behavior
```python
# Exercise 1
# Listens to incoming messages that contain "hello
@app.message("hello") # input hello
 def message_hello(message, say):
     # say() sends a message to the channel where the event was triggered
     say(f"Hey there <@{message['user']}>!") #example: Hey there @<user>!>

```