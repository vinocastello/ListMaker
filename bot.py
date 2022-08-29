import discord
import responses
import random
import glob

cat_commands = {"cat","cats","catto","cattos","mao","meow","pusa"}
pics = glob.glob('pics')
print(f"pics = {pics}")

# Send messages
async def send_message(message, user_message, is_private):
    pic_commands = {}
    try:
        prefix,command = user_message.split(" ")
        if prefix == '$mao':
            if command in cat_commands:
                with open(random.choice(pics), 'rb') as f:
                    picture = discord.File(f)
                    await message.author.send(file=picture) if is_private else await message.channel.send(file=picture)
            else:
                response = responses.handle_response(user_message,str(message.author))
                await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTAxMzMzMDQ2MTAxMzA0OTQxNA.GA3SH-.GX_QwoCTJN2F6IFzMoJRmD6jn-cYMZuF_ZzvBI'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)