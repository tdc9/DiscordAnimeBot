import discord
import datetime
from discord.ext import commands,tasks
from discord import app_commands, Interaction, Embed, Intents



from commands.searchAnime import animeSearch
from commands.reverseSearch import reverseSearch
from commands.searchManga import mangaSearch
from commands.searchStudio import studioSearch
from commands.searchStaff import staffSearch
from commands.searchCharacter import charSearch
from commands.searchUser import userSearch, userError, generateUserInfo, Profile

from misc.help import helpMessage
from config import token
class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        activity = discord.Game(name="With Darling ", type=1)
        await self.change_presence(status=discord.Status.do_not_disturb, activity=activity)
        print('All commands synced!', self.user)




intents=discord.Intents.all()
intents.message_content = True
client = Client()
tree = app_commands.CommandTree(client)

@tree.command(name='ping',description='Pong')
async def ping(interaction: Interaction):
    await interaction.response.send_message('Pong')

@tree.command(name='send_msg',description="Sends an Announcement To Jharna's Server ")
@app_commands.default_permissions(administrator=True)
async def ping(interaction: Interaction , msg:str=".", ):
    await interaction.response.send_message("Sent")
    await interaction.channel.purge(limit=1)
    channel=client.get_channel(1199397315019014376)
    await channel.send(f'{msg}')


@tree.command(name='loop',description='Loops A Message')
@app_commands.default_permissions(administrator=True)
async def ping(interaction: Interaction, channelid:str  ,msg:str ,num:int):
    channel=client.get_channel(channelid)
    await interaction.response.send_message("Starting")
    await interaction.channel.purge(limit=1)
    for i in range (0,num+1):
        if channelid == " ":
            await interaction.response.send_message(" Enter A Channel Id Where Bot Can Message")
        else:
            await channel.send(f'{msg}')

@tree.command(name='missing',description="If Num = 1 Jay Miss Dharna ,Num = 2 Dharna Miss Jay")

@app_commands.default_permissions(administrator=True)

async def ping(interaction: Interaction, num:int  = 1 , name1:str="<@1031545370712477748>", name2:str="<@1092777864983744512>"):
    channel=client.get_channel(1276878285644496991)
    await interaction.response.send_message("Starting")
    await interaction.channel.purge(limit=1)
    for i in range (0,1000):
        if num==1:
            await channel.send(f'{name1} Always Misses {name2}')
        elif num == 2:
            await channel.send(f'{name2} Always Misses {name1}')
        else:
            await interaction.response.send_message("Enter A Valid Choice")


@tree.command(name='help', description='Brings up the list of commands and things you can do with the bot.')
async def help(interaction: Interaction):
    await interaction.response.send_message(embed=helpMessage())


@tree.command(name='anime', description="Search for an anime based on its title or Anilist ID.")
@app_commands.describe(anime='Search by title or Anilist ID')
async def anime(interaction: Interaction, anime: str):
    await interaction.response.send_message(embed=animeSearch(anime))


@tree.command(name='manga', description="Search for an manga based on its title or Anilist ID.")
@app_commands.describe(manga='Search by title or Anilist ID')
async def manga(interaction: Interaction, manga: str):
    await interaction.response.send_message(embed=mangaSearch(manga))


@tree.command(name='reverse', description="Reverse search an anime based on an image")
@app_commands.describe(link='Search image of an anime (PNG/JPG)')
async def manga(interaction: Interaction, link: str):
    if link.endswith(".jpg") or link.endswith(".png") or link.endswith(".jpeg"):
        await interaction.response.send_message(embed=animeSearch(title=str(reverseSearch(link))))
    else:
        await interaction.response.send_message(embed=Embed(description="Link is not a .jpg or a .png file."))


@tree.command(name='user', description="Search for a user by name")
@app_commands.describe(username='Search for a user on AniList.')
async def user(interaction: Interaction, username: str):
    result = generateUserInfo(username)
    if result:
        await interaction.response.send_message(embed=userSearch(result), view=Profile(result))
    else:
        await interaction.response.send_message(embed=userError(username))


@tree.command(name='studio', description="Search for an anime studio by name")
@app_commands.describe(studio='Search for an animation studio by name.')
async def studio(interaction: Interaction, studio: str):
    await interaction.response.send_message(embed=studioSearch(studio))


@tree.command(name='staff', description="Searches for an anime staff by name")
@app_commands.describe(staff='Search for a staff member by name.')
async def staff(interaction: Interaction, staff: str):
    await interaction.response.send_message(embed=staffSearch(staff))


@tree.command(name='character', description="Searches for a character by name")
@app_commands.describe(character='Search for a character by name.')
async def char(interaction: Interaction, character: str):
    await interaction.response.send_message(embed=charSearch(character))

@tree.command(name='avatar',description=("Pulls The Avatar Of A User "))
async def avatar(interaction: discord.Interaction , member: discord.Member):
    await interaction.response.send_message(member.avatar)
    channel = client.get_channel(1199397328092659724)
    await channel.send(f"avatar was used by <@{interaction.user.id}> on {member} {member.avatar}")

@tree.command(name="ban", description="Bans Selected Member")
@app_commands.default_permissions(ban_members=True)
@app_commands.default_permissions(administrator=True)
async def banUser(interaction: discord.Interaction, user: discord.Member,*,
                   reason:str ='Reason Not Specified'):
        await user.ban(reason=reason)
        await interaction.response.send_message(f'{user} is Banned')
        channel = client.get_channel(1199397328092659724)
        await channel.send(f"{user} was Kicked by  <@{interaction.user.id}>", reason)


@tree.command(name='kick', description='Kicks A Selected Member')
@app_commands.default_permissions(kick_members = True)
@app_commands.default_permissions(administrator=True)
async def kickUser(interaction: discord.Interaction, user: discord.Member,*,
                   reason:str ='Reason Not Specified'):
        await user.kick(reason=reason)
        await interaction.response.send_message(f'{user} is Kicked')
        channel = client.get_channel(1199397328092659724)
        await channel.send(f"{user} was Kicked by  <@{interaction.user.id}>", reason)

@tree.command(name='mute', description='timeouts a user for a specific time')
@app_commands.checks.has_permissions(moderate_members=True)
async def mute(interaction:discord.Interaction, user: discord.Member, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, reason: str = None):
    duration = datetime.timedelta(seconds=seconds, minutes=minutes, hours= hours, days=days)
    day = datetime.timedelta(days=1)

    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
    if user.is_timed_out():
            await interaction.response.send_message(f'{user} is already Timed Out')
    elif not duration:
        await user.timeout(day, reason=reason)
        await interaction.response.send_message(f'{user} was timeouted for 1 Day', ephemeral=True)
        channel = client.get_channel(1199397328092659724)
        await channel.send(f"{user} was muted by  <@{interaction.user.id}>", reason)

    else:
        try:
            user.timeout(duration, reason=reason)
            await interaction.response.send_message(f'{user} was timed out for {duration}', ephemeral=True)
            channel = client.get_channel(1199397328092659724)
            await channel.send(f"{user} was muted by  <@{interaction.user.id}>", reason)
        except:
            await interaction.response.send_message(f'{user} Cannot be Muted', ephemeral=True)

@tree.command(name="unmute", description="unmutes a member")
@app_commands.checks.has_permissions(moderate_members=True)
async def unmute(interaction, user: discord.Member):
      await user.edit(timed_out_until=None)
      await interaction.response.send_message(f"{user} has been unmuted successfully!")
      channel = client.get_channel(1199397328092659724)
      await channel.send(f"{user} was unmuted by  <@{interaction.user.id}>", reason)


@tree.command(name="clear",description="Clears The No. Of Messages")
@app_commands.checks.has_permissions(manage_messages=True)
@app_commands.checks.has_permissions(moderate_members=True)

async def clear(interaction:discord.interactions, amount : int =5):
    try:
        await interaction.response.send_message(f'Deleting {amount} Number Of Messages')
        await interaction.channel.purge(limit=amount+1)

        channel = client.get_channel(1199397328092659724)
        await channel.send(f"{amount} number of messages were cleared by  <@{interaction.user.id}>")
    except:
        await interaction.response.send_message("Something Went Wrong")




client.run(token)
