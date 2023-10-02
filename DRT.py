import discord

def get_bot_info(token):
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Logged in as: {client.user.name} ({client.user.id})")
        print(f"Status: {client.user.status}")
        print(f"Profile Picture: {client.user.avatar_url}")
        await client.logout()

    try:
        client.run(token)
    except discord.LoginFailure:
        print("Invalid token or unable to log in.")
    except KeyboardInterrupt:
        print("Bot stopped by the user.")
        client.loop.run_until_complete(client.logout())

if __name__ == "__main__":
    token = input("Enter your Discord bot token: ")
    get_bot_info(token)
