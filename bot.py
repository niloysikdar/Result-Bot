from dotenv import load_dotenv
import os
import discord
from check_result import check_result


load_dotenv()
token = os.getenv("TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if (message.content.startswith("!result")):
            data = message.content.split(" ")[1]
            result, url = check_result(str(data))
            if (result):
                await message.channel.send(f"Hey {message.author.mention}, you can view the result at {url} \nGood luck.")

            else:
                await message.channel.send(f"Sorry {message.author.mention}, your requested result isn't available right now.")


client = MyClient()
client.run(token)
