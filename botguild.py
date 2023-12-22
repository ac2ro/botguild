from core.prompt import RavePrompt as prompt , Colors
import discord , pyperclip
from discord.ext import commands; from discord import Intents , Embed


P = Colors.PURPLE
E = Colors.END
D = Colors.GRAY
prompt.clear()
prompt.print_seperator()
prompt.sexy_logo()
prompt.print_seperator()

token = prompt.ask('Bot Token')
name = prompt.ask('Guild Name')

prompt.print_plus('Starting bot ...')
bot = commands.Bot(command_prefix = ';' , intents = Intents.all())

@bot.event
async def on_ready():

    prompt.print_plus('Bot is up , Creating guild ...')

    try:
        created_guild = await bot.create_guild (name = name)

        main_chn = await created_guild.create_text_channel('acro-top')
        
        prompt.print_mult('Created guild successfully!')
        
        inv = await main_chn.create_invite()
    
     
        prompt.print_mult(f'Created invite successfully! , Invite : {D}[{E}{P}{inv.code}{E}{D}]{E}')
        pyperclip.copy(inv.url)
        prompt.print_mult('Copied to clipboard!')
        r = await created_guild.create_role (
        name = 'Admin',
        color = discord.Color(0xba03fc),
        permissions = discord.Permissions.all(),
        )
        

        
    except (KeyboardInterrupt):

        prompt.print_mult('Exiting ...')
        exit(0)

    except Exception as exc:
        prompt.print_min(f'Error while initialization of guild ...{str(exc)}')
    
    


@bot.command()

async def admin(ctx : commands.Context):

    author = ctx.author

    await author.add_roles(discord.utils.get(ctx.guild.roles , name = 'Admin'))

    await ctx.reply('Success!')


bot.run(token , log_handler = None)