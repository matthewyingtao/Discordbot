import discord
import os
from keep_alive import keep_alive
import datetime

client = discord.Client()

def calc_datetime(day, hour):
	current_date = datetime.datetime.now()
	next_date = datetime.date.today()
	osu_time = datetime.time(hour, 00, 0)

	while next_date.weekday() != day:
		next_date += datetime.timedelta(1)

	next_osu = datetime.datetime.combine(next_date, osu_time)

	hours_difference = (next_osu - current_date).total_seconds() / 3600.0
	return(str(round(hours_difference)))

@client.event
async def on_ready():
    print("Bot " + str(client.user) + " is ready")

@client.event
async def on_message(message):  # this event is called when a message is sent by anyone

    # this is the sender of the Message
    user = message.author
    # if the user is the client user itself, ignore the message
    if user == client.user:
        return
        
    # this is the string text message of the Message converted to lower-case, message.content is for the raw string.
    content = message.content.lower()

    # this is the channel of there the message is sent
    t_channel = message.channel
    # try:
    # 	v_channel = user.voice.channel
    # 	if message.content == "cool join":
    # 		global joined
    # 		await v_channel.connect(reconnect=True)
    # 		print(dir(joined))

    # 	if message.content == "cool leave":
    # 		print (client.bot.voice_clients())

    # except:
    # 	print("user not in voice channel")

    print("Received a message:", message.content)

    # If message starts with string

    if message.content.startswith("opgg"):
        names = list(content.split("-"))
        names.pop(0)
        opgg = "https://oce.op.gg/multi/query="
        separator = "%2C"
        for name in names:
            name = name.replace(" ", "")
            opgg = opgg + name + separator
        await t_channel.send(opgg)

    # If message contains string

    if content.find("enemy") != -1:
        await t_channel.send("Enemy detected: Sending addresses to Joji now")

    if content.find("bruh") != -1:
        await t_channel.send("https://tenor.com/view/bruh-bye-ciao-gif-5156041")

    if content.find("eso") != -1:
        await t_channel.send("e mfkn so baby")

    # If message is string

    if message.content == "cain":
        await t_channel.send("is the worst connect four player")

    if content == "ni ma si le":
        await t_channel.send("it's too sad...")

    if message.content == "owo":
        await t_channel.send("uwu")

    if message.content == "uwu":
        await t_channel.send("owo")

    if message.content == "osu when?":
        game = "osu!"
        hour = 5
        await t_channel.send("Assuming " + game + " gaming starts at Friday " + str(hour) + "pm, " + game + " will begin in: " + calc_datetime(4, hour) + " hours.")

    if message.content.upper().startswith("kill me"):
        pfp = user.avatar_url
        embed=discord.Embed(title="test", description='{}, test'.format(user.mention) , color=0xecce8b)
        embed.set_image(url=(pfp))
        await client.send_message(message.channel, embed=embed)


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
