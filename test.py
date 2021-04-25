from slacker import Slacker

slack = Slacker('xoxb-1998689688754-1983918473255-JdW0XKHCvRyqL05Cbaf58002')

# Send a message to #general channel
slack.chat.post_message('#stock', 'Hello fellow slackers!')