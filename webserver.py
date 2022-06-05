import asyncio
from aiohttp import web, ClientSession
import xmltodict
import discord 
from discord.ext import commands

# Pycord Cog class
class YoutubeHook(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		# Set for storing video ids
		self.memory = set()

	# Function to start the web server async
	async def web_server(self):
		# This is required to use decorators for routes
		routes = web.RouteTableDef()

		# The youtube API sends a get request for the initial authorization
		@routes.get('/')
		async def authenticate(request):
			if 'hub.challenge' not in request.query:
				return web.Response(status=400)
			print("Authenticated")
			challenge_response = request.query.get('hub.challenge')
			return web.Response(text=challenge_response, status=200)

		# The youtube API sends post requests when new videos are posted
		@routes.post('/')
		async def receive(request):
			# Ensure the post is of the proper type
			content_type = request.content_type
			if content_type != 'application/atom+xml':
				return web.Response(status=400)
			
			# Read all the data in the body and convert it to a dict
			body_content = await request.content.read(n=-1)
			data = xmltodict.parse(body_content, 'UTF-8')
			
			# Ensure this is a proper video and its not already been announced before
			if 'entry' in data['feed'] and data['feed']['entry']['yt:videoId'] not in self.memory:
				entry = data['feed']['entry']
				# Add video id to memory to prevent duplicates
				self.memory.add(entry['yt:videoId'])
				# store wanted data in a simple dict
				video_data = {
					'title': entry['title'],
					'video_url': entry['link']['@href'],
					'channel_name': entry['author']['name'],
					'channel_url': entry['author']['uri'],
					'date_published': entry['published'],
					'video_id': entry['yt:videoId']
				}
				# Trigger the new_video event with video data
				self.bot.dispatch('new_video', video_data)
			return web.Response(status=200)

		# Create application and connect the routes
		app = web.Application()
		app.add_routes(routes)

		# Prepare the app runner
		runner = web.AppRunner(app)
		await runner.setup()

		# Prepare the website
		self.site = web.TCPSite(runner, '127.0.0.1', 8080)

		# Wait until the discord bot is fully started
		await self.bot.wait_until_ready()
		# Start the web server
		await self.site.start()
		# Send subscribe request to API
		await self.subscribe()
		
	# Function to subscribe to the website 
	async def subscribe(self):
		# Start web client to send post request
		async with ClientSession() as session:
			# Grab the ID from the channel url
			channel_id = self.bot.config["target_channel"].split('/')[-1]
			# Prepare the form data required to subscribe
			payload = {
				'hub.callback': self.bot.config['callback_url'],
				'hub.mode': 'subscribe',
				'hub.topic': f'https://www.youtube.com/xml/feeds/videos.xml?channel_id={channel_id}',
				'hub.lease_seconds': '', # Might want to define this, max 828000 seconds
				'hub.secret': '',
				'hub.verify': 'async',
				'hub.verify_token': ''
			}
			# Send post request to the API
			async with session.post('https://pubsubhubbub.appspot.com/subscribe', data=payload) as response:
				# if status is 202 it worked
				if response.status == 202:
					print("Subscribe request sent")
				else:
					print("Failed to subscribe")

	# If Cog is unloaded this runs
	def __unload(self):
		# Run site stopper in background without awaiting
		asyncio.ensure_future(self.site.stop())

def setup(bot):
	hook = YoutubeHook(bot) # Create hook
	bot.add_cog(hook) # add hook to bot to get context
	bot.loop.create_task(hook.web_server()) # Create web server and attach it to bot event loop