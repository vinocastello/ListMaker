import mao_quotes

def handle_response(message,sender) -> str:
    temp_message = message.split(" ")
    if temp_message[0].lower() == "$mao":
        p_message = temp_message[1].lower()
        if p_message == 'hi' or p_message == 'hello':
            name_only = sender[:sender.find("#")]
            return f'Magandang araw sa iyo kasamang {name_only}!'
        elif p_message == 'quotes' or p_message == 'quote':
            return mao_quotes.get_quote()
        if p_message == 'tulong':
            return '''`Use '$mao' as a prefix for commands\nExample: '$mao hi' or '$mao hello' will give you a greeting`'''

    #  return 'Yeah, I don\'t know. Try typing "!help".'