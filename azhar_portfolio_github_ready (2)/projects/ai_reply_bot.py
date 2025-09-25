print('AI Reply Bot — Run in terminal')
while True:
    msg = input('You: ')
    if msg.lower() in ('quit','exit'):
        print('Bot: Goodbye!')
        break
    elif 'hello' in msg.lower():
        print('Bot: Hello!')
    elif 'bye' in msg.lower():
        print('Bot: Bye!')
    else:
        print('Bot: Sorry, I did not understand.')