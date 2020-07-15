import discord
from discord.ext import commands
 
import sqlite3
from config import settings
from Cybernator import Paginator as pag
import os
 
client = commands.Bot(command_prefix = settings['PREFIX'])
client.remove_command('help')

 
 
@client.event
async def on_member_join(member):
    if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 1)")
        connection.commit()
    else:
        pass


@client.event
async def on_ready():
	print( 'Moblive connected' )

	await client.change_presence( status = discord.Status.online, activity = discord.Game('АНДРЕЙ ПАНОВ ЛУЧШИЙ!!!'))


@client.event
async def on_reaction_add(reaction, user):
    if client.user.id == user.id:
        pass
    else:
        if reaction.emoji == "✅":
            if reaction.count < 7:
                emb = discord.Embed(title='Делать рехост?', description = 'Для рехоста небходимо'  f'{reaction.count}/7')
                await reaction.message.edit(embed = emb) 

            elif reaction.count == 7:
                await reaction.message.channel.send("=clearq")

            elif reaction.count > 7:
                await ctx.send("Максимум достигнут!")



@client.command(aliases = ['report'])
async def __report(ctx, member: discord.Member = None, arg = None):
    message = ctx.message
    channel = client.get_channel(732867175152484362)
    if member == None:
        await ctx.send(embed=discord.Embed(description='Укажите пользователя!', color=discord.Color.red()))
        await ctx.message.add_reaction('❌')
    elif arg == None:
        await ctx.send(embed=discord.Embed(description='Укажите причину жалобы!', color=discord.Color.red()))
        await ctx.message.add_reaction('❌')
    else:
        emb = discord.Embed(title = f'Жалоба на пользователя {member}', color = discord.Color.blue())
        emb.add_field(name ='Автор жалобы:', value = f'{ctx.author}s')
        emb.add_field(name = 'Причина:', value =' ' +arg + '')
        emb.add_field(name = 'ID жалобы:', value = f'{message.id}')
        await channel.send(embed=emb)
        await ctx.send(':white_check_mark: Ваша жалоба успешно отправлена!')
        await ctx.message.add_reaction('✅')

 
@client.command(aliases = ['help'])
@commands.has_permissions(administrator = True)
async def __help(ctx):
    embed1 = discord.Embed(title = 'Команды для пользователей',
        description = '**help - данная команда показывает все команды данного бота**                     **info - данная команда показывает ваши очки**')
    embed2 = discord.Embed(title = 'Страница 2',
        description = 'Шакир')
    embed3 = discord.Embed(title = 'Страница 3',
        description = 'Лох))')
    embeds = [embed1, embed2, embed3]

    message = await ctx.send(embed = embed1)
    page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()


@client.command(aliases=['rh'])
async def __rh(ctx):
    embed = discord.Embed(title = 'Делать рехост?', description = 'Для рехоста небходимо'  '1/7')
    msg = await ctx.send(embed = embed)
    msg = await ctx.channel.history(limit=1).flatten()
    msg = msg[0]
    await msg.add_reaction('✅')

token = os.environ.get['BOT_TOKEN']