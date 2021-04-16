import discord
import asyncio
from discord.ext import commands
import time

#client = discord.Client()
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    activity = discord.Game(name="Coded buy wuy#7268", type=3)
    await bot.change_presence(activity=activity)
    print('''We have logged in as
    {0.user}'''.format(bot))
    print('--------------')

@bot.command()
async def info(ctx, *, member : discord.Member):
    inf = "{0} joined at {0.joined_at}, and have {1} role(s)"
    await ctx.send(inf.format(member, len(member.roles) - 1))

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def play(ctx):

    await ctx.message.delete()
    User = ctx.message.author
    mur = ":orange_square:"
    player = ":flushed:"
    vide = ":black_large_square:"
    box = ":green_square:"
    goal = ":star:"

    firstTime = True
    quit = False

    lvl = 0
    init = 0

    playerx = 1
    playery = 1

    boxx = 5
    boxy = 5

    goalx = 8
    goaly = 8

    size = 10

    board = [[vide for a in range(size)] for b in range(size)]
    board [playery] [playerx] = player
    board [boxy] [boxx] = box
    board [goaly] [goalx] = goal

    for o in range(size):
        board [0] [int(o)] = mur
        board [int(o)] [0] = mur
        board [int(size - 1)] [int(o)] = mur
        board [int(o)] [int(size - 1)] = mur
    
    while True :

        board [goaly] [goalx] = goal
        windowstr = ""
        line = ""
        
        if firstTime == True :
            w = await ctx.send("window : tutorial {}".format(ctx.message.author.mention))
        else :
            if lvl == 0 :
                pass
            else :
                await w.edit(content = "window : level {} {}".format(str(lvl), ctx.message.author.mention))

        if lvl == 1 and init == 1:
                init = 0
                print (lvl)

                boxy = 6
                boxx = 2

                playerx = 1
                playery = 1

                board [boxy] [boxx] = box
                board [playery] [playerx] = player

                board [1] [5] = mur
                board [2] [5] = mur
                board [3] [5] = mur
                board [5] [5] = mur
                board [6] [5] = mur
                board [7] [5] = mur
                board [8] [5] = mur

        if lvl == 2 and init == 1 :
            #reset
            init = 0
            board = [[vide for a in range(size)] for b in range(size)]
            for o in range(size):
                board [0] [int(o)] = mur
                board [int(o)] [0] = mur
                board [int(size - 1)] [int(o)] = mur
                board [int(o)] [int(size - 1)] = mur
            playerx = 1
            playery = 1
            board [playery] [playerx] = player
            board [goaly] [goalx] = goal
            print ("initb", init)

            boxx = 2
            boxy = 7
            board [boxy] [boxx] = box

            board [5] [1] = mur
            board [5] [2] = mur
            board [5] [4] = mur
            board [6] [4] = mur
            board [7] [4] = mur
            board [8] [4] = mur


        for i in board:
            line = "".join(i)
            windowstr =  str(windowstr) + "\n" + str(line)

        if firstTime == True :
            window = await ctx.send(windowstr)

            commandes = await ctx.send("movement keys : ")
            await commandes.add_reaction(emoji = '⬆️')
            await commandes.add_reaction(emoji = '⬅️')
            await commandes.add_reaction(emoji = '⬇️')
            await commandes.add_reaction(emoji = '➡️')
            await commandes.add_reaction(emoji = '❌')
            tic = time.perf_counter()
            
        else :
            await window.edit(content = windowstr)
            if boxx == goalx and boxy == goaly :
                boxx = 0
                boxy = 0
                toc = time.perf_counter()
                win = await ctx.send("{} won level{} in {} secondes !".format(ctx.message.author.mention, str(lvl), round(toc - tic, 1)))
                await asyncio.sleep(5)
                #await window.delete()
                #await w.delete()
                await win.delete()
                #await commandes.delete()
                lvl += 1
                init = 1
                print (lvl)
                print ("inita", init)
                board [playery] [playerx] = vide
                continue
                #break

            elif quit == True or init == 1 :
                await window.delete()
                await w.delete()
                await commandes.delete()
           

        def check(reaction, user):
            if user != User :
                return user == ctx.author
            if str(reaction.emoji) == '⬆️':
                return user == ctx.author and str(reaction.emoji) == '⬆️'

            elif str(reaction.emoji) == '⬅️':
                return user == ctx.author and str(reaction.emoji) == '⬅️'

            elif str(reaction.emoji) == '⬇️':
                return user == ctx.author and str(reaction.emoji) == '⬇️'

            elif str(reaction.emoji) == '➡️':
                return user == ctx.author and str(reaction.emoji) == '➡️'
            elif str(reaction.emoji) == '❌':
                return user == ctx.author and str(reaction.emoji) == '❌'


        try:
            reaction, user = await bot.wait_for('reaction_add', check=check)
            if user != User :
               await commandes.remove_reaction(emoji=reaction.emoji, member = user)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")

        #print(playerx, playery)
        print (reaction)

        if str(reaction.emoji) == '⬆️' :
            await commandes.remove_reaction(emoji = '⬆️', member = ctx.message.author)

            if board [playery - 1] [playerx] == mur or playery - 1 == boxy and boxx == playerx and board [boxy - 1] [boxx] == mur :
                board [playery] [playerx] = player

            else :
                if playery - 1 == boxy and boxx == playerx :
                    board [boxy] [boxx] = vide
                    boxy -= 1
                    board [boxy] [boxx] = box
                    
                board [playery] [playerx] = vide
                playery -= 1
                board [playery] [playerx] = player
        
        elif str(reaction.emoji) == '⬅️' :
            await commandes.remove_reaction(emoji = '⬅️', member = ctx.message.author)

            if board [playery] [playerx - 1] == mur or playery == boxy and playerx - 1 == boxx and board [boxy] [boxx - 1] == mur :
                board [playery] [playerx] = player

            else :
                if playery == boxy and playerx - 1 == boxx :
                    board [boxy] [boxx] = vide
                    boxx -= 1
                    board [boxy] [boxx] = box

                board [playery] [playerx] = vide
                playerx -= 1
                board [playery] [playerx] = player
        
        elif str(reaction.emoji) == '⬇️' :
            await commandes.remove_reaction(emoji = '⬇️', member = ctx.message.author)

            if board [playery + 1] [playerx] == mur or playery + 1 == boxy and playerx == boxx and board [boxy + 1] [boxx] == mur :
                board [playery] [playerx] = player

            else :
                if playery + 1 == boxy and playerx == boxx :
                    board [boxy] [boxx] = vide
                    boxy += 1
                    board [boxy] [boxx] = box

                board [playery] [playerx] = vide
                playery += 1
                board [playery] [playerx] = player
        
        elif str(reaction.emoji) == '➡️':
            await commandes.remove_reaction(emoji = '➡️', member = ctx.message.author)

            if board [playery] [playerx + 1] == mur or playery == boxy and playerx + 1 == boxx and board [boxy] [boxx + 1] == mur :
                board [playery] [playerx] = player

            else :
                if playery == boxy and playerx + 1 == boxx :
                    board [boxy] [boxx] = vide
                    boxx += 1
                    board [boxy] [boxx] = box

                board [playery] [playerx] = vide
                playerx += 1
                board [playery] [playerx] = player

        elif str(reaction.emoji) == '❌':
            quit = True

        firstTime = False


@bot.command()
async def embed(ctx):
    vide = ":black_large_square:"
    size = 3

    board = [[vide for a in range(size)] for b in range(size)]
    res = ""
    string = ""

    for x in board:
        string = "".join(x)
        print(string)
        res = str(res) + "\n" + str(string)
        print(res)
    
    await ctx.send(string)
    await ctx.send(res)
    print(string)

@bot.command()
async def clear(ctx, number):
    number = int(number)
    await ctx.channel.purge(limit = number  + 1)
    msg = await ctx.send("I deleted {} messages".format(number))
    await asyncio.sleep(5)
    await msg.delete()

@bot.command()
async def phrase_de_looser(ctx):
    await ctx.send("?clear 10")

@bot.command()
async def latency(ctx):
    ping = bot.latency
    ping *= 1000
    await ctx.send("bot latency : {} ms".format(int(ping)))

bot.run('ODMxNTEzNDAzMTk3NjIwMjI0.YHWVNA.ykNg6_kzXKmS4n_cvJYrLWPIfIw')