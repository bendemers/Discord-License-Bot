import discord
import asyncio
import csv
import requests
import pandas as pd
import os
import io

found = False
client = discord.Client()

url='https://docs.google.com/spreadsheets/d/10cgQNGKzKVcu2dKs4zQgdthwCrwHimpI_Rst6mnulbI/export?format=csv'
message_list = []
message_count = 0
target_server_id = '482754678979821569'
target_role_id = '&490541302111535151'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='!email for a role'))
#def search_email(email):

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!email'):
        print("!email sent")
        message_list.append(message)
        await client.send_message(message_list[len(message_list)-1].author, "Welcome to Cook Cove! What is your email?")
        await client.delete_message(message)
        return
    if message.content.find('@'):
        email = message.content
        print(email)
        for message1 in message_list:
            if message1.author == message.author:
                member = message1.author
        server = client.get_server('475519440448913418')
        role = discord.utils.get(server.roles, name= 'monitor access')
        s = requests.get(url).content
        reader = pd.read_csv(io.StringIO(s.decode('utf-8')))
        for index, row in pd.DataFrame(reader).iterrows():
            if email == row[0]:
                await client.add_roles(member, role)
                print(member)
                print(role)
                print("Role added!")
                not_found = False
                print(not_found)
                await client.send_message(member, "Added!")
                return
            else:
                not_found= True
    if not_found:
        await client.send_message(message.author, "Please do !email!")          



client.run('NDkwNTMyOTkwMjg0MzMzMDY2.Dn9G6w.FfafT_r93g7jlF8zXWb5ueALbk8')