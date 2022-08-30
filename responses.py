import mao_quotes
import weather

def handle_response(command,sender) -> str:
    if command == 'hi' or command == 'hello':
        name_only = sender[:sender.find("#")]
        return f'Magandang araw sa iyo kasamang {name_only}!'
    elif command == 'quotes' or command == 'quote':
        return mao_quotes.get_quote()
    elif command == 'tulong' or command == 'help':
        return '''Use `$mao` as prefix for the commands\n`$mao hi` / `$mao hello` - greetings\n`$mao quotes` / `$mao quote` - random quote from comrade Mao\n`$mao tulong` / `$mao help` - details about commands\n`$mao calendar` - get the link of notion calendar'''
    elif command == 'calendar' or command == 'petsa' or command == 'notion':
        return "https://www.notion.so/Calendar-c01b1b77cf2b4eee8333307be7f5b5f1"
    elif command == 'weather':
        loc = ""
        if sender == "KomradeKat#9491":
            loc = "Malabon, PH"
        else:
            loc = "Calamba, PH"
        return weather.get_weather(loc)

    #  return 'Yeah, I don\'t know. Try typing "!help".'

def get_list_display(items):
    output = ''''''
    n = len(items)
    for i in range(n):
        output += items[i]
        if i < n - 1:
            output += "\n"
    return output