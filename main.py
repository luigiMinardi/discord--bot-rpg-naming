import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

'''
edit:
    member_dict_ids
    member_dict_names_*

    in those you'll replace with your player names and ids the way you want it.
run:
    python3 main.py
'''
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='-', intents=intents)

guild_id = os.environ.get('GUILD_ID')

member_dict_ids = {
    "Luchesi": 123456789101112131,
    "Luigi": 123456789101112131,
    "Vini": 123456789101112131,
    "Sidney": 123456789101112131,
    "Victor": 123456789101112131,
    "Franz": 123456789101112131
}

member_dict_names_chuchuco = {
    "Luchesi": "Jimmy Collins (Luchesi)",
    "Luigi": "Charles Woodhouse (Luigi)",
    "Vini": "Héctor Pradeux (Vini)",
    "Sidney": "Cássio Bragança (Sidney)",
    "Victor": "Mikael Ackerman (Victor)",
    "Franz": "Mestre (Franz)"
}
member_dict_names_default = {
    "Luchesi": "Menginer (Luchesi)",
    "Luigi": "Rocstar (Luigi)",
    "Vini": "Dollinho (Vini)",
    "Sidney": "Batima (Sidney)",
    "Victor": "Cuaracy (Victor)",
    "Franz": "Mestre (Franz)"
}
member_dict_names_ded = {
    "Luchesi": "Unknown (Luchesi)",
    "Luigi": "Baka (Luigi)",
    "Vini": "Harbork (Vini)",
    "Sidney": "WindWalker (Sidney)",
    "Victor": "Zaratustra (Victor)",
    "Franz": "Mestre (Franz)"
}
member_dict_names_rifts = {
    "Luchesi": "Unknown (Luchesi)",
    "Luigi": "Manco Vegano (Luigi)",
    "Vini": "Daito (Vini)",
    "Sidney": "Y.M. de Milico (Sidney)",
    "Victor": "Trap (Victor)",
    "Franz": "Mestre (Franz)"
}

member_dict_names_skyrim = {
    "Luchesi": "Unknown (Luchesi)",
    "Luigi": "Morto (Luigi)",
    "Vini": "Dagür (Vini)",
    "Sidney": "Mestre (Sidney)",
    "Victor": "Palplen (Victor)",
    "Franz": "Kvorth (Franz)"
}


@bot.command(pass_context=True)
async def chuchuco(ctx):
    for ids in member_dict_ids:
        guild = bot.get_guild(guild_id)
        member = guild.get_member(member_dict_ids[ids])
        await member.edit(nick=f"{member_dict_names_chuchuco[ids]}")
        await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command(pass_context=True)
async def padrao(ctx):
    for ids in member_dict_ids:
        guild = bot.get_guild(guild_id)
        member = guild.get_member(member_dict_ids[ids])
        await member.edit(nick=f"{member_dict_names_default[ids]}")
        await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command(pass_context=True)
async def ded(ctx):
    for ids in member_dict_ids:
        guild = bot.get_guild(guild_id)
        member = guild.get_member(member_dict_ids[ids])
        await member.edit(nick=f"{member_dict_names_ded[ids]}")
        await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command(pass_context=True)
async def rifts(ctx):
    for ids in member_dict_ids:
        guild = bot.get_guild(guild_id)
        member = guild.get_member(member_dict_ids[ids])
        await member.edit(nick=f"{member_dict_names_rifts[ids]}")
        await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command(pass_context=True)
async def skyrim(ctx):
    for ids in member_dict_ids:
        guild = bot.get_guild(guild_id)
        member = guild.get_member(member_dict_ids[ids])
        await member.edit(nick=f"{member_dict_names_skyrim[ids]}")
        await ctx.send(f'Nickname was changed for {member.mention} ')

# run
bot.run(os.environ.get('BOT_TOKEN'))
