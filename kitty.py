import discord
from discord.ext import commands

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='1M', description='1M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='2M', description='2M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='3M', description='3M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='4M', description='4M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='5M', description='5M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='6M', description='6M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='7M', description='7M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='8M', description='8M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='9M', description='9M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='10M', description='10M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='20M', description='20M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='30M', description='30M Da Hood Cash', emoji='💰'),
            discord.SelectOption(label='UFO', description='1 UFO', emoji='🛸')
        ]

        super().__init__(placeholder='Select:', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == '1M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585385165/1-mil')
        if self.values[0] == '2M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585386752/2-mil')
        if self.values[0] == '3M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585393190/3-mil')
        if self.values[0] == '4M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585394319/4-mil')
        if self.values[0] == '5M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585395377/5-mil')
        if self.values[0] == '6M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585396602/6-mil')
        if self.values[0] == '7M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585398698/7-mil')
        if self.values[0] == '8M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585403839/8-mil')
        if self.values[0] == '9M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585400398/9-mil')
        if self.values[0] == '10M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585402160/10-mil')
        if self.values[0] == '20M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\https://www.roblox.com/catalog/9117140746/20-mil')
        if self.values[0] == '30M':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/9117146807/30-mil')
        if self.values[0] == 'UFO':
            await interaction.response.send_message(f'Оплачивайте, скрин оплаты оставить ниже, ждите ответа продавца.\nhttps://www.roblox.com/catalog/8585382941/1-ufo')


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('$'))

bot = Bot()

@bot.event
async def on_ready():
    print('Ready')

@bot.event
async def on_guild_channel_create(channel):
    await bot.wait_for('message')
    if channel.name.startswith('ticket-'):
        view = DropdownView()
        await channel.send('Выберите количество кеша, которое хотите купить:', view=view)

bot.run('OTUzNjg1MTAyODM0MTEwNDk0.YjIKdw.HBOzi4w7VDQL05coi8z6Dle_F9A')
