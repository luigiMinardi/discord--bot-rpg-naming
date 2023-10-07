# Disclaimer

This bot was made to help me and my friends have a little more imersion in our discord TTRPG games (and facilitate for the GM's to remember the players names).  

If you want to implement it yourself I explain below how, this was made to work in a single server in a very simple way, the bot has the highest role of the server and is admin.  
On discord developers website the Privileged Gateway Intents are all activated to prevent bugs.

Copy the `.env.example` file, rename it to `.env` and complete it with your informations.

# How to use

Download code, then open it on your prefered IDE.  
Then on your terminal:  
## Create venv
```bash
python3 -m venv .venv
```
## Activate venv
### mac/linux
```bash
source .venv/bin/activate
```
### windows
```bash
.venv\Scripts\activate.bat
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run the project
```bash
python3 main.py
```

# Increasing players or adding more games

## Adding new player

To add a new player create a new line on the `member_dict_ids` where the `key` is the name of the player and the `value` is the id of the player on discord.  
Example:  
```python
member_dict_ids = {
    "PlayerName": 123456789101112,
    "OtherPlayerName": 121110987654321
```

Then you add the player to every game with his/her name. If the player don't play you can rename him/her as Unknown.  
Example:
```python
member_dict_names_chuchuco = {
    "PlayerName": "PlayerGameNickname",
    "OtherPlayerName": "Unknown"
```

```python
member_dict_names_ded = {
    "PlayerName": "PlayerGameNickname",
    "OtherPlayerName": "OtherPlayerGameNickname"
```

## Adding new game

To add a new game create a new dictionary of the new game, same as those shown above (`member_dict_names_chuchuco` and `member_dict_names_ded`).  
```python
@bot.command(pass_context=True)
async def game(ctx):
    for ids in member_dict_ids:
        guild = bot.get_guild(guild_id)
        member = guild.get_member(member_dict_ids[ids])
        await member.edit(nick=f"{member_dict_names_ded[ids]}")
        await ctx.send(f'Nickname was changed for {member.mention} ')
```

Remember, you need to edit the name of the function (what is after `def` and before `(ctx)`), in the example it's being called `game`.  
This function name will be the command of the bot that you will call to change the nicknames (ih the eg. `-game`).  
Since the function is the command name the name should not repeat.

