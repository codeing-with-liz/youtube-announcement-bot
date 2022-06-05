import os
import discord
from pyngrok import ngrok
from dotenv import load_dotenv

load_dotenv()

# Start reverse proxy for webhook using ngrok
http_tunnel = ngrok.connect(addr='8080')

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

# Config values
bot.config = {
	'target_channel': 'https://www.youtube.com/channel/UCA-ZGJRoU4gVNEhuIYWKFBg',
	'callback_url': http_tunnel.public_url,
	'announcement_channel': 980170911704491202
}

@bot.event
async def on_ready():
    print(f'Bot Active')

# Video event
@bot.event
async def on_new_video(video_data):
	# Grab the channel from bot
	channel = bot.get_channel(bot.config['announcement_channel'])

	# Build embed message
	embed = discord.Embed(
        title=video_data['title'],
        color=discord.Colour.blurple()
    )
	embed.set_author(name=video_data['channel_name'])
	# https://img.youtube.com/vi/<Video ID here>/1.jpg
	embed.set_image(url=f'https://img.youtube.com/vi/{video_data["video_id"]}/1.jpg')
	embed.add_field(name='URL', value=video_data['video_url'])
	embed.set_thumbnail(url='https://i.imgur.com/zwHqAkd.png')

	# Send message
	await channel.send(f"{video_data['channel_name']} uploaded a new video.", embed=embed)

# Load the webserver
bot.load_extension('webserver')


bot.run(os.getenv('TOKEN'))