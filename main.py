import os

from time import sleep

import discord
from re import search
from gtts import gTTS


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}".format(self.user))

    async def on_message(self, message):

        if search(message.content, "/play_01"):
            channel = message.author.voice.channel
            try:
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio("./sounds/adkjladjfkhasjkfh.mp3"))
                while vc.is_playing():
                    sleep(.1)
                await vc.disconnect()
            except:
                pass

        if "->" in message.content:
            string = message.content.replace("->", '')
            tts = gTTS(string, lang="es")
            tts.save('./sounds/speech.mp3')
            channel = message.author.voice.channel
            try:
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio("./sounds/speech.mp3"))
                while vc.is_playing():
                    sleep(.1)
                await vc.disconnect()
            except:
                pass


client = MyClient()
client.run(os.environ.get('DISCORD_TOKEN'))
