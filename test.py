# from slacker import Slacker

# slack = Slacker('xoxb-1998689688754-1983918473255-Kn9HFKKecCuj9g9rX2F7nMTK')

# # Send a message to #general channel
# slack.chat.post_message('#stock', 'Hello fellow slackers!')

import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization" : "Bearer " + token},
        data={"channel" : channel, "text" : text}
    )
    print(response)

myToken = "xoxb-1998689688754-1983918473255-Kn9HFKKecCuj9g9rX2F7nMTK"

post_message(myToken, "#stock", "suhan")