from discord.ext.commands import Bot
import json
import pynder
import asyncio

config = json.loads(open("config.json").read())
BOT_PREFIX = ('?', '!')

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def tinder(ctx):
    FBTOKEN = config["FB_TOKEN"]
    if str(ctx.author) not in config["WHITELIST"] and (len(config["WHITELIST"]) != 0):
        await ctx.send("You don't have permission to run this command")
    else:
        lock = 0
        try:
            session = pynder.Session(facebook_token=FBTOKEN)
        except:
            error = await ctx.send("Invalid or Expired Token! Try to renew it")
            await asyncio.sleep(10)
            await error.delete()
            return 1


        matches = session.matches()
        users = session.nearby_users()

        print(matches)


        for user in users:
            if lock != 0:
                break
            chk = 0
            picpointer = 0
            photos = list(user.photos)
            while chk == 0:
                msg = await ctx.channel.send((((((((user.name + ': ') + str(user.age)) + ' | ') + str(round(user.distance_km, 2))) + ' Km away.\n Bio:' + user.bio + '\nThis user has ') + str(len(photos))) + ' photos!\n') + photos[picpointer])

                if picpointer != 0:
                    await msg.add_reaction('⬅')

                await msg.add_reaction('👍')
                await msg.add_reaction('👎')

                if picpointer < (len(photos) - 1):
                    await msg.add_reaction('➡')

                await msg.add_reaction('❌')
                await asyncio.sleep(0.2)

                def check(reaction,user):
                    return str(reaction.emoji) in ['👍', '👎', '➡', '⬅', '❌']

                reaction = await client.wait_for('reaction_add', check=check)

                emoji = str(reaction[0])
                print(emoji)
                if emoji == '👍':
                    print(user.like)
                    print('Liked!')
                    chk = 1
                if emoji == '👎':
                    print(user.dislike)
                    print('Passed!')
                    chk = 1
                if emoji == '⬅':
                    picpointer -= 1
                    print('Previous Photo!')
                if emoji == '➡':
                    print('Next Photo!')
                    picpointer += 1
                if emoji == '❌':
                    lock = 1
                    await msg.delete()
                    break
                await msg.delete()
        await ctx.send('Tinder closed!')

client.run(config["BOT_TOKEN"])

