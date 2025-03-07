#Python discord bot
#The_Gaming_Lounge bot
import discord
import os
import time as t
import random as r
from keep_alive import keep_alive
from discord.ext import commands
import discord.ui

#Globals 
global Type_Of_Crop
global Crop_Positioning

my_secret=os.environ['DISCORD_TOKEN']
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".",intents=intents)

#colours
green = discord.Color.from_rgb(53,94,59)
Red = discord.Color.from_rgb(252, 114, 114)
purple = discord.Color.from_rgb(146, 135, 228)

def TextFile(Text,Crop):  
  File = open('TXT-Files/Stardew-calc/'+ Text)
  Content = File.readlines()
  Percentage = (Content[Crop])
  return Percentage

#classes/OOP
class Crop_Calc(discord.ui.View):
    @discord.ui.button(label="Fruit", style=discord.ButtonStyle.blurple)
    async def Fruit(self,interaction:discord.Interaction,button:discord.ui.Button):
        embedVar = discord.Embed(title="What Type Fruit do you want to plant", color=purple)
        embedVar.set_thumbnail(url = 'https://gameranx.com/wp-content/uploads/2021/12/stardew-valley.jpg')
        await interaction.response.send_message(embed=embedVar,view=Fruits_View())
    
    @discord.ui.button(label="Vegetable", style=discord.ButtonStyle.blurple)
    async def Vegetable(self,interaction:discord.Interaction,button:discord.ui.Button):
        embedVar = discord.Embed(title="What Type Vegetable do you want to plant", color=purple)
        embedVar.set_thumbnail(url = 'https://gameranx.com/wp-content/uploads/2021/12/stardew-valley.jpg')
        

  
@bot.listen('Vegetable')
async def Vegetable():
    @discord.ui.select( 
        placeholder = "What Vegetable", 
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="Amaranth",
            ),
            discord.SelectOption(
                label="Artichoke",
            ),
            discord.SelectOption(
                label="Beet",
            ),
            discord.SelectOption(
                label="Artichoke",
            ),
            discord.SelectOption(
                label="Garlic",
            ),
            discord.SelectOption(
                label="Cauliflower",
            ),
            discord.SelectOption(
                label="Corn",
            ),
            discord.SelectOption(
                label="EggPlant",
            ),
            discord.SelectOption(
                label="Greenbean",
            ),
            discord.SelectOption(
                label="Kale",
            ),
            discord.SelectOption(
                label="Parsnips",
            ),
            discord.SelectOption(
                label="Potatoes",
            ),
            discord.SelectOption(
                label="Pumpkin",
            ),
            discord.SelectOption(
                label="Radish",
            ),
            discord.SelectOption(
                label="Redcabbage",
            ),
            discord.SelectOption(
                label="Rice",
            ),
            discord.SelectOption(
                label="Taroroot",
            ),
            discord.SelectOption(
                label="Tomato",
            ),
            discord.SelectOption(
                label="Yam",
            ),
          ]
      )
    async def select_callback(self, interaction, select):
        Vegetable_Crop =  str({select.values[0]})
        Vegetable_Crop = Vegetable_Crop[2:-2]
        embedVar = discord.Embed(title="How many " + Vegetable_Crop + "s will you be planting", color=purple)
        embedVar.set_thumbnail(url = 'https://gameranx.com/wp-content/uploads/2021/12/stardew-valley.jpg')
        await interaction.response.send_message(embed=embedVar)
    
class Fruits_View(discord.ui.View):
    @discord.ui.select( 
      placeholder = "What Fruit", 
      min_values = 1, 
      max_values = 1, 
      options = [ 
          discord.SelectOption(
              label="Ancientfruit",
          ),
          discord.SelectOption(
              label="Blueberry",
          ),
          discord.SelectOption(
              label="Cactusfruit",
          ),
          discord.SelectOption(
              label="Cranberries",
          ),
          discord.SelectOption(
              label="Grape",
          ),
          discord.SelectOption(
              label="Melon",
          ),
          discord.SelectOption(
              label="Peppers",
          ),
          discord.SelectOption(
              label="Pineapple",
          ),
          discord.SelectOption(
              label="Redcabbage",
          ),
          discord.SelectOption(
              label="Rhubarb",
          ),
          discord.SelectOption(
              label="Starfruit",
          ),
          discord.SelectOption(
              label="Strawberry",
          ),
        ]
    )
    async def select_callback(self, interaction, select): 
        Fruit_Crop =  str({select.values[0]})
        Fruit_Crop = Fruit_Crop[2:-2]
            #print(Crop_Positioning)
        embedVar = discord.Embed(title="How many " + Fruit_Crop + "s will you be planting", color=purple)
        embedVar.set_thumbnail(url = 'https://gameranx.com/wp-content/uploads/2021/12/stardew-valley.jpg')
        await interaction.response.send_message(embed=embedVar)
    
#command to tell me bots online 
@bot.event
async def on_ready():
  Activity = discord.Game(name="Amositty.netlify.app", type=4)
  await bot.change_presence(status=discord.Status.online, activity=Activity)
  await bot.tree.sync()
  print('We have logged in')

#main code

@bot.tree.command(name="crop_calc",description="Calculate the profits of your harvests")
async def crop_calc(interaction:discord.Interaction):
  embedVar = discord.Embed(title="What Type Crop do you want to plant", description="Is it a fruit or vegetable", color=purple)
  embedVar.set_thumbnail(url = 'https://gameranx.com/wp-content/uploads/2021/12/stardew-valley.jpg')
  await interaction.response.send_message(embed=embedVar,view=Crop_Calc())

  
@bot.tree.command(name="crop_info",description="All the info you need on 1 crop of your choice")
async def crop_info(interaction:discord.Interaction):
  await interaction.response.send_message("Yet To Be added")
  
keep_alive()
bot.run(my_secret)



