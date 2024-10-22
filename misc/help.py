import discord


def helpMessage():
  embed = discord.Embed(
    title='Zero Two Help Commands',
    colour=discord.Colour.blue(),
    description=
    'Shadow uses Slash Commands, so please enable them for your server!',
  )
  embed.set_author(name='Help')
  embed.add_field(name='/anime <title>',
                  value="Search anime by title or ID.",
                  inline=False)
  embed.add_field(name='/manga <title>',
                  value="Search manga by title or ID.",
                  inline=False)
  embed.add_field(name='/user <anilist username>',
                  value="Search up a user by their username.",
                  inline=False)
  embed.add_field(name='/reverse <image link>',
                  value="Search an anime by a link to an image.",
                  inline=False)
  embed.add_field(name='/studio <studio name>',
                  value="Search a studio by their name.",
                  inline=False)
  embed.add_field(name='/staff <staff name>',
                  value="Search an actor by their name.",
                  inline=False)
  embed.add_field(name='/character <character name>',
                  value="Search a character by their name.",
                  inline=False)
  embed.add_field(name='/avatar <user name>',
                  value="Shows The Avatar Of The Selected User",
                  inline=False)
  embed.add_field(name='/kick <user name>',
                  value="Kicks The Selected User, Can Be Used By Thosee Who Have Perms",
                  inline=False)
  embed.add_field(name='/ban <user name>',
                  value="Bans The Selected User, Can Be Used By Thosee Who Have Perms",
                  inline=False)

                  
  return embed
