import os
import logging
import slack
import ssl as ssl_lib
import certifi
from message_class import Message

message_sent = {}

def start(web_client: slack.WebClient, user_id: str, channel: str):
    message_inst = Message(channel)

    message = message_inst.get_messsage_payload()

    response = web_client.chat_postMessage(**message)

    message_inst.timestamp = response["ts"]

    if channel not in message_sent:
        message_sent[channel] = {}
    message_sent[channel][user_id] = message_inst
