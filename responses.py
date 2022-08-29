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
        elif p_message == 'tulong' or p_message == 'help':
            return '''`Use '$mao' as a prefix for commands\nExample: '$mao hi' or '$mao hello' will give you a greeting`'''
        elif p_message == 'calendar' or p_message == 'petsa' or p_message == 'notion':
            return "https://www.notion.so/Calendar-c01b1b77cf2b4eee8333307be7f5b5f1"

    #  return 'Yeah, I don\'t know. Try typing "!help".'