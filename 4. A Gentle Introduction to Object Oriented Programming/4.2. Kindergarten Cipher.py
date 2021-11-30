def decipher(message,pasword):
    for changer in pasword:
        message=message.replace(changer[0],changer[1])
    return message
