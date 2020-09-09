from . import pusher_client


def Chat(chat_to, message):
    pusher_client.trigger('chat'+str(chat_to), str(chat_to),
                          {'message': message})


def Received(chat_session, sender):
    pusher_client.trigger('Received'+str(sender), str(sender),
                          {'chat_session': chat_session})
