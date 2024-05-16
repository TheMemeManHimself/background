import discord
from discord.commands import slash_command
from discord.ext import commands
import requests


class avatar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[1211812480385290311, 1043949659971915897],
                   name='avatar',
                   description='get avatar items of a user')
    async def avatar(self, ctx, id: discord.Option(discord.SlashCommandOptionType.string)):


        def fetch_avatar_url(user_id):
            try:
                url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=720x720&format=Png&isCircular=false"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    return data['data'][0]['imageUrl']
                else:
                    return None
            except requests.exceptions.RequestException as e:
                print("Error fetching avatar URL:", e)
                return None

        
        def fetch_username(user_id):
            try:
                response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
                if response.status_code == 200:
                    user_data = response.json()
                    return user_data.get('displayName')
                else:
                    return None
            except requests.exceptions.RequestException as e:
                print("Error fetching username:", e)
                return None


        def fetch_description(user_id):
            try:
                response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
                if response.status_code == 200:
                    user_data = response.json()
                    return user_data.get('description')
                else:
                    return None
            except requests.exceptions.RequestException as e:
                print("Error fetching username:", e)
                return None

        
        def construct_item_url(asset_id):
            base_url = "https://www.roblox.com/catalog/"
            return f"{base_url}{asset_id}/"
        
        r = requests.get("https://avatar.roblox.com/v1/users/" + id +
                         "/currently-wearing")
        if r.status_code == 200:
            # Parse the JSON response
            json_data = r.json()

            # Access the list of asset IDs
            asset_ids = json_data['assetIds']
            with open("file.txt", "w") as text_file:
                for asset_id in asset_ids:
                    # Construct the URL for each item
                    item_url = construct_item_url(asset_id)
                    text_file.write(item_url + "\n")
        with open("file.txt", "r") as f:
            avatarurl=fetch_avatar_url(id)
            username=fetch_username(id)
            desc=fetch_description(id)
            embed = discord.Embed(
                title=username,
                description=desc,
                
                color=discord.Colour.nitro_pink(), # Pycord provides a class with default colors you can choose from
            )
            embed.add_field(name="Equipped avatar items:", value=f.read())
            embed.set_thumbnail(url=avatarurl),
        
        
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(avatar(bot))
