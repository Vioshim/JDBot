import discord

def check(ctx):
  def inner(m):
    return m.author == ctx.author
  return inner

def Membercheck(ctx):
  def inner(m):
    return m.author == ctx.guild.me
  return inner

def warn_permission(ctx, Member):
  if isinstance(ctx.channel, discord.TextChannel):
    
    return ctx.author.guild_permissions.manage_messages and ctx.author.top_role > Member.top_role and ctx.author.guild_permissions >= Member.guild_permissions
    #bug with user with same permissions maybe and other stuff(seems fixed for right now, leaving note just in case.)
    

  if isinstance(ctx.channel, discord.DMChannel):
    return True