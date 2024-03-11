import discord
import aiosqlite
from discord.emoji import Emoji
from discord.enums import ButtonStyle
from discord.interactions import Interaction
from discord.partial_emoji import PartialEmoji
from discord.ui import Button, View, InputText, Modal
from discord.ext import commands, tasks
from DiscordDatabase import DiscordDatabase
from datetime import date
import random
import urllib.request
import ssl
from discord.ui.item import Item
import requests
import imaplib, email
import asyncio
from itertools import chain
from pathlib import Path
from PyPDF2 import PdfMerger
import csv
import uuid
import zipfile
import dropbox

dbx = dropbox.Dropbox(oauth2_access_token="sl.BlEYQdb8BsBcgtL73urGLAKw-mqTeDzgOk_3sjaNH32K351MPqcIRZjBjir20K1Z0_Wqo4ODoOy_DrxLYv-J2URUSl85iXUIW7GwJ9wJJRTYr_gB1cFft453UiGbFhnt83WV1BEgXhpzEF2Dkyt8-nc",
                      oauth2_refresh_token="AHuUgKmz3DoAAAAAAAAAAYAghShsQLxtx0vO165kpKcOxL_UWLmNzUcWg1W8MxJs",
                      app_key="h5iu2aw6caauzy5",
                      app_secret="p6pa7t5d18abn3h")


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

urlOrder = "NA"
apiToken = "4acbba73-80ae-4521-b7d6-835b23555068"
headers = {
    f'Auth: %{apiToken}%'
}



stateData = {
        "AA": "Armed Forces Americas",
		"AE": "Armed Forces Europe",
		"AK": "Alaska",
		"AL": "Alabama",
		"AP": "Armed Forces Pacific",
		"AR": "Arkansas",
		"AS": "American Samoa",
		"AZ": "Arizona",
		"CA": "California",
		"CO": "Colorado",
		"CT": "Connecticut",
		"DC": "District of Columbia",
		"DE": "Delaware",
		"FL": "Florida",
		"GA": "Georgia",
		"GU": "Guam",
		"HI": "Hawaii",
		"IA": "Iowa",
		"ID": "Idaho",
		"IL": "Illinois",
		"IN": "Indiana",
		"KS": "Kansas",
		"KY": "Kentucky",
		"LA": "Louisiana",
		"MA": "Massachusetts",
		"MD": "Maryland",
		"ME": "Maine",
		"MI": "Michigan",
		"MN": "Minnesota",
		"MO": "Missouri",
		"MP": "Northern Mariana Islands",
		"MS": "Mississippi",
		"MT": "Montana",
		"NC": "North Carolina",
		"ND": "North Dakota",
		"NE": "Nebraska",
		"NH": "New Hampshire",
		"NJ": "New Jersey",
		"NM": "New Mexico",
		"NV": "Nevada",
		"NY": "New York",
		"OH": "Ohio",
		"OK": "Oklahoma",
		"OR": "Oregon",
		"PA": "Pennsylvania",
		"PR": "Puerto Rico",
		"RI": "Rhode Island",
		"SC": "South Carolina",
		"SD": "South Dakota",
		"TN": "Tennessee",
		"TX": "Texas",
		"UM": "United States Minor Outlying Islands",
		"UT": "Utah",
		"VA": "Virginia",
		"VI": "Virgin Islands, U.S.",
		"VT": "Vermont",
		"WA": "Washington",
		"WI": "Wisconsin",
		"WV": "West Virginia",
		"WY": "Wyoming",
}

#key = weight, value = price
PriorityRates = {
    8 : 5.00,
    70 : 7.00,

}

ExpressRates = {
    8 : 8.00,
    70 : 13.00,
}

GroundRates = {
    1 : 3.00,
    70 : 4.00
}

labelClass = {
    "priority":"Priority Mail",
    "usps_express":"Priority Mail Express",
    "ground_oz":"USPS Ground Advantage (below 1 lbs)",
    "ground_lbs":"USPS Ground Advantage (above 1 lbs)",
}

priceToLbs = {

}

tempWeight = {}

tempFromName = {}
tempFromCompany = {}
tempFromAddress = {}
tempFromAddress2 = {}
tempFromCity = {}
tempFromZip = {}
tempFromPhone = {}
tempFromState = {}

tempToName = {}
tempToCompany = {}
tempToAddress = {}
tempToAddress2 = {}
tempToCity = {}
tempToZip = {}
tempToPhone = {}
tempToState = {}

user = "voicecrackcentralofficial@gmail.com"
password = ""
imap_url = "imap.gmail.com"
ssl._create_default_https_context = ssl._create_unverified_context
intents = discord.Intents.all()
DB_GUILD_ID = 1158838661706686476
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
word_url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
req = urllib.request.Request(word_url, headers=headers)
response = urllib.request.urlopen(req)
long_txt = response.read().decode()
words = long_txt.splitlines()
default = "NONE"
keyCashAmt = "amount"
keyCashFor = "for"


imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993

bot = commands.Bot(command_prefix='!',intents=intents)

db = DiscordDatabase(bot, DB_GUILD_ID)

# Example user data storage
user_data = {}


async def findPayment(amount, text):
    mail0 = imaplib.IMAP4_SSL(imap_ssl_host)
    mail0.login(user, password)
    mail0.noop()
    mail0.select('Inbox')
    result, data = mail0.search(None, 'FROM', '"{}"'.format('cash@square.com'))
    result, dataVen = mail0.search(None, 'FROM', '"{}"'.format('venmo@venmo.com'))
    msgs = []
    msgsVen = []
    for num in data[0].split():
        typ, data = mail0.fetch(num, '(RFC822)')
        msgs.append(data)
    for num in dataVen[0].split():
        typ, data = mail0.fetch(num, '(RFC822)')
        msgsVen.append(data)
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple:
 
            # encoding set as utf-8
                content = str(sent[1], 'utf-8')
                data = str(content)
 
            # Handling errors related to unicodenecode
                try:
                    indexstart = data.find("ltr")
                    data2 = data[indexstart + 5: len(data)]
 
                # printing the required content which we need
                # to extract from our email i.e our body
                    amount0 = int(amount)
                    compareNum = "$" + str(amount0) + ".00"
                    forDat = data2.find(compareNum)
                    for4 = data2.find(text)
                    if forDat != -1:
                        nums = str(data2[forDat:forDat+len(compareNum)])
                        if nums == compareNum:
                            if for4 != -1:
                                tx = str(data2[for4:for4 + len(text)])
                                if tx == text:
                                    success = True
                                    return success
                                else: 
                                    success = False
                                    return success
                    else:
                        print("Still searching.")
 
                except UnicodeEncodeError as e:
                    print("can't find")
                    pass
    for msg in msgsVen[::-1]:
        for sent in msg:
            if type(sent) is tuple:
 
            # encoding set as utf-8
                content = str(sent[1], 'utf-8')
                data = str(content)
 
            # Handling errors related to unicodenecode
                try:
                    indexstart = data.find("ltr")
                    data2 = data[indexstart + 5: len(data)]
 
                # printing the required content which we need
                # to extract from our email i.e our body
                    amount0 = int(amount)
                    compareNum = "$" + str(amount0) + ".00"
                    forDat = data2.find(compareNum)
                    for4 = data2.find(text)
                    if forDat != -1:
                        nums = str(data2[forDat:forDat+len(compareNum)])
                        if nums == compareNum:
                            if for4 != -1:
                                tx = str(data2[for4:for4 + len(text)])
                                if tx == text:
                                    success = True
                                    return success
                                else: 
                                    success = False
                                    return success
                    else:
                        print("Still searching.")
 
                except UnicodeEncodeError as e:
                    pass
        
    mail0.logout()



blacklist = [1116767052762456254, 1045149855514902579, 444688947659145228, 474054359387340800, 974883167972511806, 707020944379609189, 1104136059153022986]

# Command to process payment and store user data
started_tasks = []

async def payLoop(ctx, t):
    user_id = ctx.author.id
    user = ctx.author
    if t.current_loop == 60:
        await user.send("Payment in queue for too long, please start a new deposit.")
        keyamt = keyCashAmt + str(user_id)
        keyfor = keyCashFor + str(user_id)
        if await database.get(keyamt) != None and await database.get(keyfor) != None:
            await database.delete(keyamt)
            await database.delete(keyfor)
        t.stop()
    print("running...")
    keyamt = keyCashAmt + str(user_id)
    keyfor = keyCashFor + str(user_id)
    if await database.get(keyamt) != None and await database.get(keyfor) != None:
        amt = await database.get(keyamt)
        cash4 = await database.get(keyfor)
        succ = await findPayment(amt, cash4)
        mone = 0
        if succ == True:
            db = await aiosqlite.connect('main.db')
            cursor = await db.cursor()
            await cursor.execute(f"SELECT money FROM economy WHERE user_id = {user_id}")
            bal = await cursor.fetchone()
            mone = bal[0] + int(amt)
            await db.execute(f"UPDATE economy SET money = {mone} WHERE user_id = {user_id}")
            await db.commit()
            await cursor.close()
            await db.close()
            await user.send(f"Payment has been processed successfully! Your new balance is: {mone}" )
            await database.delete(keyamt)
            await database.delete(keyfor)
            t.stop()

def task_generator(ctx):
    t = tasks.loop(seconds=60)(payLoop)
    started_tasks.append(t)
    t.start(ctx, t)

class defaultFromAddress(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.defAd1 = None
        self.defName = None
        self.defAd2 = None
        self.defCity = None
        self.defZip = None
        self.isDef : bool = None
        self.defState : bool = None

        self.add_item(InputText(label="FROM NAME", required=True))
        self.add_item(InputText(label="FROM STREET",required=True))
        self.add_item(InputText(label="FROM STREET 2 (OPTIONAL)",required=False))
        self.add_item(InputText(label="FROM CITY", required=True))
        self.add_item(InputText(label="FROM ZIP AND STATE",placeholder="14653, CA", required=True))
    async def callback(self, interaction: Interaction):
        await interaction.response.defer()
        db = await aiosqlite.connect('main.db')
        
        user_id = interaction.user.id
        await db.execute(f"UPDATE economy SET ad1 = '{self.children[1].value}' WHERE user_id = {user_id}")
        await db.execute(f"UPDATE economy SET name = '{self.children[0].value}' WHERE user_id = {user_id}")
        await db.execute(f"UPDATE economy SET isDef = {1} WHERE user_id = {user_id}")
        if str(self.children[2].value) == "" or str(self.children[2]) == None or not self.children[2]:
            await db.execute(f"UPDATE economy SET ad2 = 'None' WHERE user_id = {user_id}")
        else:
            await db.execute(f"UPDATE economy SET name = '{self.children[2].value}' WHERE user_id = {user_id}")
        await db.execute(f"UPDATE economy SET city = '{self.children[3].value}' WHERE user_id = {user_id}")
        if str(self.children[4].value).find(","):
            x = str(self.children[4].value).split(",")
            y = 0
            for i in x:
                if y == 0:
                    await db.execute(f"UPDATE economy SET zip = '{i}' WHERE user_id = {user_id}")
                if y == 1:
                    await db.execute(f"UPDATE economy SET state = '{i}' WHERE user_id = {user_id}")
                y += 1
        await db.execute(f"UPDATE economy SET isDef = {1} WHERE user_id = {user_id}")
        await db.commit()
        await db.close()     
        self.stop()

class fromAddress(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.addressField = None
        self.isAddress2 : bool = None
        self.isAddress2To : bool = None
        self.toAddressField = None

        self.add_item(InputText(label="Does 'from' address have address 2?", placeholder="(type y for yes or n for no)"))
        self.add_item(InputText(label="From Inputs", placeholder="Name \nAddress 1 \nAddress 2 (if selected Y) \nSaint Louis, MO 63101", style= discord.InputTextStyle.multiline))
        self.add_item(InputText(label="Does 'to' address have address 2?", placeholder="(type y for yes or n for no)"))
        self.add_item(InputText(label="To Inputs", placeholder="Name \nAddress 1 \nAddress 2 (if selected Y) \nSaint Louis, MO 63101", style= discord.InputTextStyle.multiline))
    async def callback(self, interaction: Interaction):
        iAddress2 = str(self.children[0].value).lower()
        toAddress2 = str(self.children[2].value).lower()
        if iAddress2 == "y":
            self.isAddress2 = True
        elif iAddress2 == "n":
            self.isAddress2 = False
        elif iAddress2 == "yes":
            self.isAddress2 = True
        elif iAddress2 == "no":
            self.isAddress2 = False
        else:
            await interaction.response.send_message("Please enter a valid answer for 'Does address have address 2?' line")
            
        if toAddress2 == "y":
            self.isAddress2To = True
        elif toAddress2 == "n":
            self.isAddress2To = False
        elif toAddress2 == "yes":
            self.isAddress2To = True
        elif toAddress2 == "no":
            self.isAddress2To = False
        else:
            await interaction.response.send_message("To Address 2 option not selected")
        embed = discord.Embed(title="Your Details: ", color=discord.Color.from_rgb(255,255,255))
        await interaction.response.send_message(embeds=[embed])
        self.addressField = self.children[1].value
        self.toAddressField = self.children[3].value
        self.stop()

class fromAddressDef(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.toAd1 = None
        self.toAd2 = None
        self.toNme = None
        self.toCty = None
        self.toZp = None
        self.toSte = None
        self.addressField = None
        self.isAddress2 : bool = None
        self.isAddress2To : bool = None
        self.toAddressField = None
        self.toAutoFilled : bool = False
        


        self.add_item(InputText(label="Does 'from' address have address 2?",required=False, placeholder="(type y for yes or n for no)"))
        self.add_item(InputText(label="From Inputs",required=False, placeholder="Name \nAddress 1 \nAddress 2 (if selected Y) \nSaint Louis, MO 63101", style= discord.InputTextStyle.multiline))
        self.add_item(InputText(label="Does 'to' address have address 2?", placeholder="(type y for yes or n for no)"))
        self.add_item(InputText(label="To Inputs", placeholder="Name \nAddress 1 \nAddress 2 (if selected Y) \nSaint Louis, MO 63101", style= discord.InputTextStyle.multiline))
    async def callback(self, interaction: Interaction):
        user_id = interaction.user.id
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT * FROM economy WHERE user_id = {user_id}")
        result = await cursor.fetchone()
        toAddress2 = str(self.children[2].value).lower()
        iAddress2 = str(self.children[0].value).lower()
        if ((str(self.children[0].value) == "" or str(self.children[0].value) == None) and (str(self.children[1].value) == "" or str(self.children[1].value) == None)):
            await interaction.response.defer()
            self.toAutoFilled = True
            self.toAd1 = str(result[12])
            if str(result[13]) == "None":
                self.toAd2 = "n"
            else:
                self.toAd2 = str(result[13])
            self.toNme = str(result[14])
            self.toCty = str(result[15])
            self.toSte = str(result[17])
            self.toZp = str(result[16])
            embed = discord.Embed(title="Your Details: ", color=discord.Color.from_rgb(255,255,255))
            if toAddress2 == "y":
                self.isAddress2To = True
            elif toAddress2 == "n":
                self.isAddress2To = False
            elif toAddress2 == "yes":
                self.isAddress2To = True
            elif toAddress2 == "no":
                self.isAddress2To = False
            else:
                await interaction.response.send_message("To Address 2 option not selected")
            embed = discord.Embed(title="Your Details: ", color=discord.Color.from_rgb(255,255,255))
            await interaction.followup.send(embeds=[embed])
            self.addressField = self.children[1].value
            self.toAddressField = self.children[3].value
            self.stop()
        else:
            if iAddress2 == "y":
                self.isAddress2 = True
            elif iAddress2 == "n":
                self.isAddress2 = False
            elif iAddress2 == "yes":
                self.isAddress2 = True
            elif iAddress2 == "no":
                self.isAddress2 = False
            else:
                await interaction.response.send_message("Please enter a valid answer for 'Does address have address 2?' line")
            
            if toAddress2 == "y":
                self.isAddress2To = True
            elif toAddress2 == "n":
                self.isAddress2To = False
            elif toAddress2 == "yes":
                self.isAddress2To = True
            elif toAddress2 == "no":
                self.isAddress2To = False
            else:
                await interaction.response.send_message("To Address 2 option not selected")
            embed = discord.Embed(title="Your Details: ", color=discord.Color.from_rgb(255,255,255))
            await interaction.response.send_message(embeds=[embed])
            self.addressField = self.children[1].value
            self.toAddressField = self.children[3].value
            self.stop()


class fromAddress0(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.addressField = None
        self.isAddress2 : bool = None
        self.isAddress2To : bool = None
        self.toAddressField = None

        self.add_item(InputText(label="Does 'from' address have address 2?", placeholder="(type y for yes or n for no)"))
        self.add_item(InputText(label="From Inputs", placeholder="Name \nAddress 1 \nAddress 2 (if selected Y) \nSaint Louis, MO 63101", style= discord.InputTextStyle.multiline))
        self.add_item(InputText(label="Does 'to' address have address 2?", placeholder="(type y for yes or n for no)"))
        self.add_item(InputText(label="To Inputs", placeholder="Name \nAddress 1 \nAddress 2 (if selected Y) \nSaint Louis, MO 63101", style= discord.InputTextStyle.multiline))
    async def callback(self, interaction: Interaction):
        iAddress2 = str(self.children[0].value).lower()
        toAddress2 = str(self.children[2].value).lower()
        if iAddress2 == "y":
            self.isAddress2 = True
        elif iAddress2 == "n":
            self.isAddress2 = False
        elif iAddress2 == "yes":
            self.isAddress2 = True
        elif iAddress2 == "no":
            self.isAddress2 = False
        else:
            await interaction.response.send_message("Please enter a valid answer for 'Does address have address 2?' line")
            
        if toAddress2 == "y":
            self.isAddress2To = True
        elif toAddress2 == "n":
            self.isAddress2To = False
        elif toAddress2 == "yes":
            self.isAddress2To = True
        elif toAddress2 == "no":
            self.isAddress2To = False
        else:
            await interaction.response.send_message("To Address 2 option not selected")
        embed = discord.Embed(title="Your Details: ", color=discord.Color.from_rgb(255,255,255))
        await interaction.response.send_message(embeds=[embed])
        self.addressField = self.children[1].value
        self.toAddressField = self.children[3].value
        self.stop()


class amountSend(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.val = None
        self.add_item(InputText(label="How much would you like to deposit?", placeholder="Enter a whole number e.g. 25"))
        
    async def callback(self, interaction: Interaction):
        embed = discord.Embed(title="Payment: ", color=discord.Color.from_rgb(255,255,255))
        embed.add_field(name="Amount: ", value=self.children[0].value, inline=False)
        self.val = int(self.children[0].value)
        await interaction.response.send_message(embeds=[embed])
        self.stop()

users = {}
confirm = {}
labelC = {}
async def open_account0(member:discord.Member):
    db0 = await aiosqlite.connect('ratesCus.db')
    cursor0 = await db0.cursor()
    await cursor0.execute(f"SELECT * FROM rates WHERE user_id = {member.id}")
    result0 = await cursor0.fetchone()
    if result0:
        #print("yo")
        return
    if not result0:
        await cursor0.execute(f"INSERT INTO rates(user_id, usps_priority, usps_priorityOp2, usps_priorityRate0, usps_priorityRate1, usps_priorityRate, ga, gaOp2, gaRate0, gaRate1, gaRate, express, expressOp2, expressRate0, expressRate1, expressRate, ga_oz, ga_ozOp2, ga_ozRate0, ga_ozRate1, ga_ozRate, ground, groundOp2, groundRate0, groundRate1, groundRate) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (member.id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    await db0.commit()
    await cursor0.close()
    await db0.close()

async def open_account(member:discord.Member):
    #print("hi")
    db = await aiosqlite.connect('main.db')
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM economy WHERE user_id = {member.id}")
    result = await cursor.fetchone()

    if result:
        #print("yo")
        return
    if not result:
        await cursor.execute(f"INSERT INTO economy(user_id, money, spent, labelsCreated, bulk, orders, rate, isRate, type, rate18, rate970, isRateOp2, ad1, ad2, name, city, zip, state, isDef) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (member.id, 0, 0, 0, 0, 0, 0, 0, "None", 0, 0, 0, "None", "None", "None", "None", "None", "None", 0))
    await db.commit()
    await cursor.close()
    await db.close()

async def computePrice0(user_id, weightVal, lClass):
    db = await aiosqlite.connect('main.db')
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM economy WHERE user_id = {user_id}")
    result = await cursor.fetchone()
    db0 = await aiosqlite.connect('ratesCus.db')
    cursor0 = await db0.cursor()
    await cursor0.execute(f"SELECT * FROM rates WHERE user_id = {user_id}")
    result0 = await cursor0.fetchone()
    key0 = str(user_id) + "freeLabels"
    price = 0
    print(lClass)
    if lClass == "priority":
        if weightVal >= 1 and weightVal <= 8:
            if result0[1] == 1:
                price = float(result0[5])
            elif result0[2] == 1:
                #print("Hi")
                price = float(result0[3])
            else:
                price = 5.00
        elif weightVal >= 9 and weightVal <= 70:
            if result0[1] == 1:
                price = float(result0[5])
            elif result0[2] == 1:
                price = float(result0[4])
            else:
                price = 7.00     
    elif lClass == "usps_express":
        if weightVal >= 1 and weightVal <= 8:
            if result0[11] == 1:
                price = float(result0[15])
            elif result0[12] == 1:
                price = float(result0[13])
            else:
                price = 8.00
        elif weightVal >= 9 and weightVal <= 35:
            if result0[11] == 1:
                price = float(result0[15])
            elif result0[12] == 1:
                price = float(result[14])
            else:
                price = 12.00
    elif lClass == "ground_oz":
        if weightVal >= 1 and weightVal < 16:
            if result0[16] == 1:
                price = float(result0[20])
            else:
                price = 3.00
    elif lClass == "ground_lbs":
        if weightVal >= 1 and weightVal <= 70:
            if result0[6] == 1:
                price = float(result0[10])
            else:
                price = 3.00
    if int(await database.get(key0)) >= 1:
        price = 0
    return lClass, price

async def computePrice(user_id, weightVal):
    global labelC
    db = await aiosqlite.connect('main.db')
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM economy WHERE user_id = {user_id}")
    result = await cursor.fetchone()
    db0 = await aiosqlite.connect('ratesCus.db')
    cursor0 = await db0.cursor()
    await cursor0.execute(f"SELECT * FROM rates WHERE user_id = {user_id}")
    result0 = await cursor0.fetchone()
    price = 0
    lClass = labelC[user_id]['labelClass']
    print(lClass)
    if lClass == "priority":
        if weightVal >= 1 and weightVal <= 8:
            if result0[1] == 1:
                price = float(result0[5])
            elif result0[2] == 1:
                #print("Hi")
                price = float(result0[3])
            else:
                price = 5.00
        elif weightVal >= 9 and weightVal <= 70:
            if result0[1] == 1:
                price = float(result0[5])
            elif result0[2] == 1:
                price = float(result0[4])
            else:
                price = 7.00     
    elif lClass == "usps_express":
        if weightVal >= 1 and weightVal <= 8:
            if result0[11] == 1:
                price = float(result0[15])
            elif result0[12] == 1:
                price = float(result0[13])
            else:
                price = 8.00
        elif weightVal >= 9 and weightVal <= 35:
            if result0[11] == 1:
                price = float(result0[15])
            elif result0[12] == 1:
                price = float(result[14])
            else:
                price = 12.00
    elif lClass == "ground_oz":
        if weightVal >= 1 and weightVal < 16:
            if result0[16] == 1:
                price = float(result0[20])
            else:
                price = 3.00
    elif lClass == "ground_lbs":
        if weightVal >= 1 and weightVal <= 70:
            if result0[6] == 1:
                price = float(result0[10])
            else:
                price = 3.00
    return lClass, price
    

class WeightButton(Button):
    def __init__(self, rol_name,style):
        super().__init__(label=rol_name,style=style)


    async def callback(self, interaction:discord.Interaction):
        global confirm
        if self.label == 'Confirm':
            confirm[interaction.user.id]['confirm'] = True
            await interaction.response.send_message('Confirmed!')
            
        else:
            weightVal = weight(title = "Enter Weight:")
            await interaction.response.send_modal(weightVal)
        await interaction.message.delete()

class weight(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.val = None
        self.add_item(InputText(label="Insert Weight: ", placeholder="e.g 50"))
        
    async def callback(self, interaction: Interaction):

        global users
        try:
            users[interaction.user.id]['weight'] = float(self.children[0].value)
        except:
            await user.send("Invalid weight.")
            self.stop()
        
        lClass, price = await computePrice(interaction.user.id, float(self.children[0].value))
        self.val = float(self.children[0].value)
        freeLabels = await database.get(str(interaction.user.id) + "freeLabels")
        freeLabels = int(freeLabels)
        if freeLabels >= 1:
            price = "Free"
        embed = discord.Embed(title="Label Details: ", color=discord.Color.from_rgb(128,0,128))
        embed.add_field(name="Label Class: ", value=labelClass[lClass], inline=False)
        embed.add_field(name="Weight: ", value=self.children[0].value, inline=False)
        embed.add_field(name="Cost: ", value=price, inline=False)
        
        view = View()
        view.add_item(WeightButton('Confirm',discord.ButtonStyle.green))
        view.add_item(WeightButton('Edit',discord.ButtonStyle.red))
        await interaction.response.send_message(embed=embed,view=view)
        

        



class LabelClass(discord.ui.View):
    answer1 = None
    answer2 = None
    fromAddress1 = None
    fromAddress2 = None
    fromCity = None
    fromName = None
    fromNumber = None
    fromZip = None
    fromCompany = None
    fromState = None
    toAddress1 = None
    toAddress2 = None
    toCity = None
    toName = None
    toNumber = None
    toZip = None
    toCompany = None
    toState = None
    
    @discord.ui.select(
        placeholder="Select a label class:",
        options=[
            discord.SelectOption(label="USPS Priority", value="priority"),
            discord.SelectOption(label = "USPS Express", value="usps_express"),
            discord.SelectOption(label="USPS Ground Advantage (below 1 lbs)", value="ground_oz"),
            discord.SelectOption(label="USPS Ground Advantage (above 1 lbs)", value="ground_lbs"),
        ]

    )

    async def select_label(self, select, interaction : discord.Interaction):
        global labelC
        global users
        global confirm
        if interaction.user.id not in users:
            users[interaction.user.id] = {'weight':None}
        if interaction.user.id not in confirm:
            confirm[interaction.user.id] = {'confirm':False}
        elif confirm[interaction.user.id]['confirm'] == True:
            confirm[interaction.user.id]['confirm'] = False
        if interaction.user.id not in labelC:
            labelC[interaction.user.id] = {'labelClass':None}
        labelC[interaction.user.id] = {'labelClass':select.values[0]}
        labelClas = labelC[interaction.user.id]
        self.answer1 = select.values[0]
        self.children[0].disabled = True
        weightVal = None
        if labelClas == "ground_oz":
            weightVal = weight(title = "Enter Weight in OZ (1-16)")
        else:
            weightVal = weight(title = "Enter Weight:")
        await interaction.response.send_modal(weightVal)
        await weightVal.wait()
        while confirm[interaction.user.id]['confirm'] == False:
            #print("not confirmed yet")
            await asyncio.sleep(1)
        self.answer2 = users[interaction.user.id]['weight']
        #labelC[interaction.user.id]['labelClass'] = select.values[0]
        await interaction.message.edit(view=self)
        self.stop()

            

class fromButton(discord.ui.View):
    tAd1 = None
    tAd2 = None
    tNme = None
    tCty = None
    tZp = None
    tSte = None
    fromBut : bool = None
    fromFieldInfo = None
    isAdd2 : bool = None
    toField = None
    toisAdd2 : bool = None
    editedWeight : bool = None
    autofilled : bool = None
    wght = None


    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    """ async def on_timeout(self) -> None:
        await self.message.channel.send("Timed Out")
        await self.disable_all_items() """


    @discord.ui.button(label="Continue",
                       style = discord.ButtonStyle.green)

    async def fromIn(self, button: discord.ui.Button, interaction: discord.Interaction):
        user_id = interaction.user.id
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT isDef FROM economy WHERE user_id = {user_id}")
        result = await cursor.fetchone()
        autof = result[0]
        if autof == 1:
            await self.disable_all_items()
            fromFi = fromAddressDef(title= "Enter label info: ")
            await interaction.response.send_modal(fromFi)
            await fromFi.wait()
            if fromFi.toAutoFilled == True:
                self.autofilled = True
                if fromFi.toAd2 == "n":
                    self.isAdd2 = False
                else:
                    self.isAdd2 = True
                    self.tAd2 = fromFi.toAd2
                self.tAd1 = fromFi.toAd1
                self.tCty = fromFi.toCty
                self.tSte = fromFi.toSte
                self.tZp = fromFi.toZp
                self.tNme = fromFi.toNme
                self.fromBut = True
                self.editedWeight = False
                self.toField = fromFi.toAddressField
                self.toisAdd2 = fromFi.isAddress2To
                self.stop()   
            else:
                self.autofilled = False
                self.fromFieldInfo = fromFi.addressField
                self.isAdd2 = fromFi.isAddress2
                self.toField = fromFi.toAddressField
                self.toisAdd2 = fromFi.isAddress2To
                self.fromBut = True
                self.editedWeight = False
                await self.disable_all_items()
                self.stop()        
        else:
            fromFi = fromAddress0(title= "Enter from info: ")
            await interaction.response.send_modal(fromFi)
            await fromFi.wait()
            self.fromFieldInfo = fromFi.addressField
            self.autofilled = False
            #print(fromFi.addressField)
            #print("hi")
            self.isAdd2 = fromFi.isAddress2
            self.toField = fromFi.toAddressField
            self.toisAdd2 = fromFi.isAddress2To
            self.fromBut = True
            self.editedWeight = False
            await self.disable_all_items()
            self.stop()


class isAddCorrectPrompt(discord.ui.View):
    confirm : bool = None
    add : bool = None

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)


    async def on_timeout(self) -> None:
        self.confirm = False
        await self.message.channel.send("Timed Out")
        await self.disable_all_items()

    @discord.ui.button(label="Confirm",
                       style = discord.ButtonStyle.green)
    
    async def confirmBut(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.confirm = True
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label= "Edit", 
                       style=discord.ButtonStyle.red)

    async def editBut(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.confirm = False
        await interaction.response.defer()
        self.stop()
    @discord.ui.button(label="Add Another Label",
                       style = discord.ButtonStyle.primary)
    
    async def addLabel(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.add = True
        await interaction.response.defer()
        self.stop()



class paymentType(discord.ui.View):
    cashapp : bool = None
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timed Out")
        await self.disable_all_items()
    @discord.ui.button(label="Cashapp",
                       style = discord.ButtonStyle.primary)
    async def Cashapp(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        self.cashapp = True
        self.stop()


class selectLabelButton(discord.ui.View):
    uspsCarrier : bool = None
    depositBal : bool = None
    history : bool = None
    checkbal : bool = None
    amount = None

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timed Out")
        await self.disable_all_items()

    @discord.ui.button(label="USPS",
                       style = discord.ButtonStyle.primary)

    async def USPS(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        self.uspsCarrier = True
        self.stop()
    @discord.ui.button(label= "UPS", 
                       style=discord.ButtonStyle.gray, disabled=True)
    async def UPS(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()


class button0(discord.ui.View):
    uspsCarrier : bool = None
    depositBal : bool = None
    history : bool = None
    checkbal : bool = None
    amount = None

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timed Out")
        await self.disable_all_items()

    @discord.ui.button(label="USPS",
                       style = discord.ButtonStyle.primary)

    async def USPS(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        self.uspsCarrier = True
        self.stop()

    @discord.ui.button(label= "UPS", 
                       style=discord.ButtonStyle.gray, disabled=True)
    async def UPS(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

    @discord.ui.button(label="Deposit Balance",
                    style = discord.ButtonStyle.green, row=3, disabled=True)
    
    async def Deposit(self, button: discord.ui.Button, interaction: discord.Interaction):
        dep = amountSend(title = "Enter Amount: (Minimum $1)")
        await interaction.response.send_modal(dep)
        await dep.wait()
        self.amount = dep.val
        self.depositBal = True
        self.uspsCarrier = False
        self.history = False
        self.checkbal = False
        self.stop()

    @discord.ui.button(label="History",
                       style = discord.ButtonStyle.primary, row=3)
    
    async def History(self, button: discord.ui.Button, interaction: discord.Interaction):
        orderIdsKey = "orders" + str(interaction.user.id)
        await interaction.response.send_message("This feature is disabled for now!")
        return
        if await database.get(orderIdsKey) == None:
            await interaction.response.send_message("No labels created :(")
        else:
            data = await database.get(orderIdsKey)
            #response = requests.get(url=f"api/v1/orders/{idOR}", headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'})
            print(data)
            index = 0
            embed = discord.Embed(title="Order History: ", color=discord.Color.from_rgb(128,0,128))
            await interaction.response.defer()
            await interaction.followup.send("Loading order history, this may take a moment...")
            for i in data:
                index += 1
                response = requests.get(url=f"api/v1/orders/{i}", headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'}).json()
                print(response)
                name = response['order']['to_name']
                typeLabel = response['order']['class']
                tracking = response['order']['tracking']
                embed.add_field(name=f"Order #{index}", value=f"Tracking: {tracking} | To: {name} | Type: {typeLabel}", inline=False)
            await interaction.followup.send(embeds=[embed])
            await interaction.followup.send("If you would like to download a custom amount of files please use the '!download HELP' command.")
            #this grayed portion is disabled, work in progress for new database.

    @discord.ui.button(label="Overview",
                       style = discord.ButtonStyle.primary, row=2)
    
    async def Overview(self, button: discord.ui.Button, interaction: discord.Interaction):
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT * FROM economy WHERE user_id = {interaction.user.id}")
        await interaction.response.defer()
        result = await cursor.fetchone()
        embed = discord.Embed(title="Overview: ", color=discord.Color.from_rgb(128,0,128))
        embed.add_field(name="Amount Spent ($):", value="{0:.2f}".format(result[2]), inline=False)
        embed.add_field(name="Labels Created:", value=f"{result[3]}", inline=False)
        await interaction.followup.send(embeds=[embed])

    @discord.ui.button(label="Wallet",
                       style = discord.ButtonStyle.primary, row=2)
    
    async def Wallet(self, button: discord.ui.Button, interaction: discord.Interaction):
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT * FROM economy WHERE user_id = {interaction.user.id}")
        result = await cursor.fetchone()
        await interaction.response.defer()
        embed = discord.Embed(title="Wallet: ", color=discord.Color.from_rgb(128,0,128))
        embed.add_field(name="Credits ($):", value="{0:.2f}".format(result[1]), inline=False)
        await interaction.followup.send(embeds=[embed])

    @discord.ui.button(label="Support",
                       style = discord.ButtonStyle.primary, row=2)
    
    async def Support(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("<#1091971085584580628>")

    @discord.ui.button(label="Set Default From Address",
                       style = discord.ButtonStyle.danger, row=2)
    
    async def Set(self, button: discord.ui.Button, interaction: discord.Interaction):
        fromad = defaultFromAddress(title = "Default From Address")
        await interaction.response.send_modal(fromad)
        await fromad.wait()
        await interaction.message.edit(view=self)
        self.stop()
        #await interaction.response.send_message("This option is currently under development")

    @discord.ui.button(label="CSV",
                       disabled=False,
                       style = discord.ButtonStyle.primary, row=4)
    
    async def CSV(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Download the CSV format Template in 'csv-tutorial' channel and read/watch the guide on how to use this feature.\nOnce completed, add the CSV file as an attachment in dm's of the bot. \nUse '!makeCSV' command as the message attachment, and wait patiently for the bot to send your zip file. ")

def searchKey(val):
    for key, value in stateData.items():
        if val == value:
            return key
    return False

class buttonCSV(discord.ui.View):
    confirm : bool = None

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timed Out")
        await self.disable_all_items()

    @discord.ui.button(label="Confirm",
                       style = discord.ButtonStyle.green)
    async def Confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.confirm = True
        await interaction.response.defer()
        self.stop()



    
@bot.command()
@commands.max_concurrency(number=1, per=commands.BucketType.user, wait=False)
async def makeCSV(ctx):
    user_id = ctx.author.id
    user = ctx.author
    for i in blacklist:
        if user_id == i:
            await user.send("Your kind isn't allowed to use our bot!")
            return

    extens = str(user_id)
    await open_account(member=ctx.author)
    await open_account0(member=ctx.author)
    db = await aiosqlite.connect('main.db')
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM economy WHERE user_id = {ctx.author.id}")
    result = await cursor.fetchone()
    db0 = await aiosqlite.connect('ratesCus.db')
    cursor0 = await db0.cursor()
    await cursor0.execute(f"SELECT * FROM rates WHERE user_id = {ctx.author.id}")
    result0 = await cursor0.fetchone()
    split_v1 = str(ctx.message.attachments).split("filename='")[1]
    #print(split_v1)
    filename = str(split_v1 + extens).split("' ")[0]
    labelQuantity = 0

    if ctx.message.attachments == []:
        await user.send("No file found!")
        return
            
    else:
        extens = str(user_id)
        split_v1 = str(ctx.message.attachments).split("filename='")[1]
        #print(split_v1)
        filename = str(split_v1 + extens).split("' ")[0]
        if filename.endswith(".csv"):
            finalDict = []
            price = 0
            isValid = True
            lastLabel = None
            await ctx.message.attachments[0].save(fp="tmpdata/{}".format(extens + filename))
            with open("tmpdata/" + str(extens + filename), 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                index = 0
                for line in csv_reader:
                    index += 1
                    lClass = str(line['class'])
                    if lastLabel == None:
                        lastLabel = lClass
                    weightVal = int(float(line['weight']))
                    #print(line['to_name'], line['to_address1'])
                    if lClass == lastLabel:
                        if lClass == "priority":
                            if weightVal >= 1 and weightVal <= 8:
                                if result0[1] == 1:
                                    price += float(result0[5])
                                elif result0[2] == 1:
                                    #print("Hi")
                                    price += float(result0[3])
                                else:
                                    price += 5.00
                            elif weightVal >= 9 and weightVal <= 70:
                                if result0[1] == 1:
                                    price += float(result0[5])
                                elif result0[2] == 1:
                                    price += float(result0[4])
                                else:
                                    price += 7.00     
                            else:
                                isValid = False
                                await user.send("Line: " + str(index)+ ", Error: Value must be 1-70 lbs")
                                return
                        elif lClass == "usps_express":
                            isValid = False
                            await user.send("Line: " + str(index)+ ", Express not supported in CSV. Please make a manual express label.")
                            return
                        elif lClass == "ground_oz":
                            if weightVal >= 1 and weightVal < 16:
                                if result0[16] == 1:
                                    price += float(result0[20])
                                else:
                                    price += 3.00
                            else:
                                isValid = False
                                await user.send("Line: " + str(index)+ ", Error: Value must be less than (<) but not equal to 16 oz")
                                return
                        elif lClass == "ground_lbs":
                            if weightVal >= 1 and weightVal <= 70:
                                if result0[6] == 1:
                                    price += float(result0[10])
                                else:
                                    price += 3.00
                            else:
                                isValid = False
                                await user.send("Line: " + str(index)+ ", Error: Value must be greater than (>) 1 lbs")
                                return
                        else:
                            await user.send("Line: " + str(index)+ ", Invalid Provider")
                            isValid = False
                            return
                    else:
                        await user.send("Cannot combine different label types into one CSV, please make them separately.")
                        return

                    if str(line['from_name']) == '' or str(line['to_name']) == '':
                        await user.send("Line: " + str(index)+ f", Error: To or From Name cannot be empty!")
                        isValid = False
                    if str(line['from_address1']) == '' or str(line['to_address1']) == '':
                        await user.send("Line: " + str(index)+ f", Error: To or From Address1 cannot be empty!")
                        isValid = False
                    if str(line['from_city']) == '' or str(line['to_city']) == '':
                        await user.send("Line: " + str(index)+ f", Error: To or From City cannot be empty!")
                        isValid = False
                    if str(line['from_state']) == '' or str(line['to_state']) == '':
                        await user.send("Line: " + str(index)+ f", Error: To or From State cannot be empty!")
                        isValid = False
                    if str(line['from_postcode']) == '' or str(line['to_postcode']) == '':
                        await user.send("Line: " + str(index)+ f", Error: To or From postcode cannot be empty!")
                        isValid = False
                    if str(line['from_country']) == '' or str(line['to_country']) == '':
                        await user.send("Line: " + str(index)+ f", Error: To or From Country cannot be empty!")
                        isValid = False
                    if str(line['weight']) == '':
                        await user.send("Line: " + str(index)+ f", Error: Weight cannot be empty!")
                        isValid = False
                    if str(line['provider']) == '':
                        await user.send("Line: " + str(index)+ f", Error: Provider cannot be empty!")
                        isValid = False
                    if str(line['class']) == '':
                        await user.send("Line: " + str(index)+ f", Error: Class cannot be empty!")
                        isValid = False
                    data = {
                                    "provider_code": "usps",
	                                "class": str(line['class']),
	                                "weight": int(line['weight']),
	                                "from_name": str(line['from_name']),
	                                "from_phone": "3342278854",
	                                "from_address1": str(line['from_address1']),
	                                "from_address2": str(line['from_address2']),
	                                "from_city": str(line['from_city']),
	                                "from_state": str(line['from_state']),
	                                "from_postcode": str(line['from_postcode']),
	                                "from_country": str(line['from_country']),
	                                "to_name": str(line['to_name']),
	                                "to_phone": "3342278854",
	                                "to_address1": str(line['to_address1']),
	                                "to_address2": str(line['to_address2']),
	                                "to_city": str(line['to_city']),
	                                "to_state": str(line['to_state']),
	                                "to_postcode": str(line['to_postcode']),
	                                "to_country": str(line['to_country'])
                                }
                    today = date.today()
                    try:
                        data0 = {
                                "Weight": int(line['weight']),
                                "Date": str(today.strftime("%d/%m/%Y")),
                                "FromCountry": str(line['from_country']),
                                "FromName": str(line['from_name']),
                                "FromCompany": str(line['from_company']),
                                "FromPhone": "",
                                "FromStreet": str(line['from_address1']),
                                "FromStreet2": str(line['from_address2']),
                                "FromZip": str(line['from_postcode']),
                                "FromCity": str(line['from_city']),
                                "FromState": str(line['from_state']),
                                "ToCountry": str(line['to_country']),
                                "ToName": str(line['to_name']),
                                "ToCompany": str(line['to_company']),
                                "ToPhone": "",
                                "ToStreet": str(line['to_address1']),
                                "ToStreet2": str(line['to_address2']),
                                "ToZip": str(line['to_postcode']),
                                "ToCity": str(line['to_city']),
                                "ToState": str(line['to_state']),
                                "Height": int(line['height']),
                                'Length': int(line['length']),
                                "Width": int(line['width'])
                            }
                    except:
                        await user.send("Issue with CSV format, please check for format errors and try again.")
                        return

                    print(data0)
                    finalDict.append(data0)
                    labelQuantity += 1
                    
                print(isValid)
                if isValid and labelQuantity <= 200:
                    embed0 = discord.Embed(title="CSV Details: ", color=discord.Color.from_rgb(128,0,128))
                    embed0.add_field(name="Total Cost ($): ", value="$" + "{0:.2f}".format(price), inline=False)
                    await user.send(embeds=[embed0])
                    view = buttonCSV(timeout=None)
                    await user.send(view=view)
                    await view.wait()
                    await view.disable_all_items()
                    if view.confirm is None:
                        await user.send("Timed out")
                        return
                    elif view.confirm is True:
                        money = float(result[1])
                        if money >= float(price):
                            dat = {"labelType": str(lastLabel),
                                   "data": finalDict}
                            print(dat)
                            waitAlgTries = 0
                            initQueueWait = 10
                            labelsSuccess = False
                            response = requests.post(url="url", json=dat, headers={'x-api-key': 'd928af43-c610-4ccc-8618-46e486cc35cc'})
        
                            while waitAlgTries <= 15:
                                await asyncio.sleep(initQueueWait)
                                if response.status_code == 200:
                                    print(response.json())
                                    response = response.json()
                                    labelsSuccess = True
                                    break
                                else:
                                    print("labels not found")
                                    waitAlgTries += 1
                                    #await asyncio.sleep(initQueueWait)
                                    
                            if labelsSuccess == False:
                                await user.send("Error with CSV, please open a ticket! Your account has been charged.")
                                money = float(result[1])
                                money -= price
                                if result[2] != None:
                                    mon = float(result[2])
                                    mon += price
                                    await db.execute(f"UPDATE economy SET spent = {mon} WHERE user_id = {user_id}")
                                    await db.commit()
                                else:
                                    await db.execute(f"UPDATE economy SET spent = {price} WHERE user_id = {user_id}")
                                    await db.commit()
                                if result[3] != None:
                                    lab = int(result[3])
                                    lab += int(labelQuantity)
                                    await db.execute(f"UPDATE economy SET labelsCreated = {lab} WHERE user_id = {user_id}")
                                    await db.commit()
                                else:
                                    await db.execute(f"UPDATE economy SET labelsCreated = {1} WHERE user_id = {user_id}")
                                    await db.commit()
                                await db.execute(f"UPDATE economy SET money = {money} WHERE user_id = {user_id}")
                                await db.commit()
                                return
                            await user.send("Creating labels, please wait...")
                            if response['type'] != 'success':
                                await user.send("Failed to make label, please contact Samurai Labels for assistance. Your account has not been charged.")
                                return
                            else:
                                print()
                                #print(finalDict)
                                if labelQuantity <= 10:
                                    await asyncio.sleep(10)
                                elif labelQuantity > 10 and labelQuantity <= 50:
                                    await asyncio.sleep(25)
                                elif labelQuantity > 50 and labelQuantity <= 100:
                                    await asyncio.sleep(50)
                                elif labelQuantity > 100 and labelQuantity <= 150:
                                    await asyncio.sleep(70)
                                elif labelQuantity > 150 and labelQuantity <= 200:
                                    await asyncio.sleep(90)
                                else:
                                    await user.send("Max labels is 200 per CSV")
                                    return
                                idOR = response['bulkOrder']['uuid']
                                labelQuantity = response['bulkOrder']['total']
                                
                                response = requests.get(url=f"{url}/api/v2/order/download-bulk-order/{idOR}", headers={'x-api-key': 'd928af43-c610-4ccc-8618-46e486cc35cc'})
                                file = open(f"{user_id}-{idOR}.zip", "wb")
                                file.write(response.content)
                                file.close()
                                merger = PdfMerger()
                                pdf_files = []
                                with zipfile.ZipFile(f"{user_id}-{idOR}.zip", 'r') as z:
                                    for name in z.namelist():
                                        if name.endswith(".pdf"):
                                            i = random.randint(1,999999)
                                            file = open(f"{user_id}-{i}.pdf", "wb")
                                            pdf_files.append(f"{user_id}-{i}.pdf")
                                            file.write(z.read(name))
                                            file.close()
                                for pdf in pdf_files:
                                    merger.append(pdf)
                                merger.write(f"{user_id}-{idOR}.pdf")
                                merger.close()

                                file0 = discord.File(f"{user_id}-{idOR}.pdf")
                                try:
                                    await user.send(file=file0)
                                except:
                                    with open(f"{user_id}-{idOR}.pdf", 'rb') as f:
                                        respo = dbx.files_upload(f.read(), f"/{user_id}_{filename}.pdf")
                                        shared_link_metadata = dbx.sharing_create_shared_link(respo.path_display)
                                        file_link = shared_link_metadata.url
                                        file_link = file_link.replace("?dl=1", "?dl=0")
                                        embed0 = discord.Embed(title="Label Details: ", color=discord.Color.from_rgb(128,0,128))
                                        embed0.add_field(name="Link: ", value=f"[Labels]({file_link})", inline=False)
                                        await user.send(embed=embed0)
                                money = float(result[1])
                                money -= price

                                if result[2] != None:
                                    mon = float(result[2])
                                    mon += price
                                    await db.execute(f"UPDATE economy SET spent = {mon} WHERE user_id = {user_id}")
                                    await db.commit()
                                else:
                                    await db.execute(f"UPDATE economy SET spent = {price} WHERE user_id = {user_id}")
                                    await db.commit()
                                if result[3] != None:
                                    lab = int(result[3])
                                    lab += int(labelQuantity)
                                    await db.execute(f"UPDATE economy SET labelsCreated = {lab} WHERE user_id = {user_id}")
                                    await db.commit()
                                else:
                                    await db.execute(f"UPDATE economy SET labelsCreated = {1} WHERE user_id = {user_id}")
                                    await db.commit()

                                await db.execute(f"UPDATE economy SET money = {money} WHERE user_id = {user_id}")
                                await db.commit()

                        else:
                            await user.send("Insufficient balance! Please Deposit.")
                            return
                else:
                    await user.send("Something went wrong, limit is 300 orders at a time!")
                    return
                    



@bot.slash_command()
async def send_modal(ctx):
    await ctx.respond(view=View())

async def addAnotherLabel(ctx, tempBal):
    user_id = ctx.author.id
    user = ctx.author
    db = await aiosqlite.connect('main.db')
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM economy WHERE user_id = {user_id}")
    result = await cursor.fetchone()
    db0 = await aiosqlite.connect('ratesCus.db')
    cursor0 = await db0.cursor()
    await cursor0.execute(f"SELECT * FROM rates WHERE user_id = {user_id}")
    result0 = await cursor0.fetchone()
    view = selectLabelButton()
    message = await user.send(view=view)
    view.message = message
    key0 = str(user_id) + "freeLabels"
    await view.wait()
    await view.disable_all_items()
    if view.uspsCarrier is None:
        await user.send("Closing Active Window")
    elif view.uspsCarrier is True:
        if await database.get(key0) == None:
            await database.set(key0, 0)
        print("okay")
        views = LabelClass()
        await user.send(view=views)
        price = 0
        await views.wait()
        isValid = True
        lClass = views.answer1
        weightVal = views.answer2
        weightInt = weightVal
        #print(views.answer1)
        if lClass == "priority":
            if weightVal >= 1 and weightVal <= 8:
                if result0[1] == 1:
                    price = float(result0[5])
                elif result0[2] == 1:
                #print("Hi")
                    price = float(result0[3])
                else:
                    price = 5.00
            elif weightVal >= 9 and weightVal <= 70:
                if result0[1] == 1:
                    price = float(result0[5])
                elif result0[2] == 1:
                    price = float(result0[4])
                else:
                    price = 7.00     
            else:
                isValid = False
                await user.send("Value must be 1-70 lbs")
            
        elif lClass == "usps_express":
            if weightVal >= 1 and weightVal <= 8:
                if result0[11] == 1:
                    price = float(result0[15])
                elif result0[12] == 1:
                    price = float(result0[13])
                else:
                    price = 8.00
            elif weightVal >= 9 and weightVal <= 35:
                if result0[11] == 1:
                    price = float(result0[15])
                elif result0[12] == 1:
                    price = float(result[14])
                else:
                    price = 12.00
            else:
                isValid = False
                await user.send("Value must be 1-35 lbs")
        elif lClass == "ground_oz":
            if weightVal >= 1 and weightVal < 16:
                if result0[16] == 1:
                    price = float(result0[20])
                else:
                    price = 3.00
            else:
                isValid = False
                await user.send("Invalid weight, please enter a value less than 16 oz")
        elif lClass == "ground_lbs":
            if weightVal >= 1 and weightVal <= 70:
                if result0[6] == 1:
                    price = float(result0[10])
                else:
                    price = 3.00	
            else:
                isValid = False
                await user.send("Please enter a value between 1-70 lbs")
        if isValid:
            if await database.get(user_id) == None:
                await database.set(user_id, 0)
            freeLabels = await database.get(key0)
            if float(tempBal) >= price or int(freeLabels) >= 1:
                if int(freeLabels) >= 1:
                    price = 0
                embed = discord.Embed(title="Label Details: ", color=discord.Color.from_rgb(128,0,128))
                embed.add_field(name="Label Class: ", value=labelClass[lClass], inline=False)
                embed.add_field(name="Weight: ", value=weightInt, inline=False)
                embed.add_field(name="Cost: ", value=price, inline=False)
                await user.send(embeds=[embed])
                view = fromButton()
                message = await user.send(view=view)
                view.message = message
                await view.wait()
                await view.disable_all_items()
                print(view.editedWeight) 
                fromAddress1 = None
                fromAddress2 = None
                fromCity = None
                fromName = None
                fromZip = None
                fromState = None
                toAddress1 = None
                toAddress2 = None
                toCity = None
                toName = None
                toZip = None
                toState = None
                if view.fromBut is True:
                    if view.autofilled == False:
                        print(view.fromFieldInfo)
                        fromAd2 = view.isAdd2
                        line = view.fromFieldInfo.split('\n')
                        i = 0
                        for lin in line:
                            i += 1
                            if fromAd2 == True:
                                if i == 1:
                                    fromName = lin.upper()
                                if i == 2:
                                    fromAddress1 = lin.upper()
                                if i == 3:
                                    fromAddress2 = lin.upper()
                                if i == 4:
                                    x = lin.split(',')
                                    y = 0
                                    for word in x:
                                        y += 1
                                        if y == 1:
                                            fromCity = word.upper()
                                        if y == 2:
                                            z = 0
                                            word0 = word.split(" ")
                                            for next in word0:
                                                z += 1
                                                if z == 2:
                                                    fromState = next.upper()
                                                if z == 3:
                                                    fromZip = next

                            else:
                                if i == 1:
                                    fromName = lin.upper()
                                if i == 2:
                                    fromAddress1 = lin.upper()
                                    fromAddress2 = ""
                                if i == 3:
                                    x = lin.split(',')
                                    y = 0
                                    for word in x:
                                        y += 1
                                        if y == 1:
                                            fromCity = word.upper()
                                        if y == 2:
                                            z = 0
                                            word0 = word.split(" ")
                                            for next in word0:
                                                z += 1
                                                if z == 2:
                                                    fromState = next.upper()
                                                if z == 3:
                                                    fromZip = next
                    else:
                        print("here")
                        if view.isAdd2 == True:
                            fromAddress2 = view.tAd2
                        else:
                            fromAddress2 = ""
                        fromAddress1 = view.tAd1
                        fromState = view.tSte
                        fromCity = view.tCty
                        fromZip = view.tZp
                        fromName = view.tNme

                    toAd2 = view.toisAdd2
                    line0 = view.toField.split('\n')
                    i = 0
                    for lin in line0:
                        i += 1
                        if toAd2 == True:
                            if i == 1:
                                toName = lin.upper()
                            if i == 2:
                                toAddress1 = lin.upper()
                            if i == 3:
                                toAddress2 = lin.upper()
                            if i == 4:
                                x = lin.split(',')
                                y = 0
                                for word in x:
                                    y += 1
                                    if y == 1:
                                        toCity = word.upper()
                                    if y == 2:
                                        z = 0
                                        word0 = word.split(" ")
                                        for next in word0:
                                            z += 1
                                            if z == 2:
                                                toState = next.upper()
                                            if z == 3:
                                                toZip = next

                        else:
                            if i == 1:
                                toName = lin.upper()
                            if i == 2:
                                toAddress1 = lin.upper()
                                toAddress2 = ""
                            if i == 3:
                                x = lin.split(',')
                                y = 0
                                for word in x:
                                    y += 1
                                    if y == 1:
                                        toCity = word.upper()
                                    if y == 2:
                                        z = 0
                                        word0 = word.split(" ")
                                        for next in word0:
                                            z += 1
                                            if z == 2:
                                                toState = next.upper()
                                            if z == 3:
                                                toZip = next

                    err = False
                    if fromName == None:
                        await user.send("From Name is missing.")
                        err = True
                    elif fromAddress1 == None:
                        await user.send("From Address 1 is missing.")
                        err = True
                    elif fromCity == None:
                        await user.send("From State or Zip, City is missing.")
                        err = True
                    elif fromState == None:
                        await user.send("From State, Zip or City is missing.")
                        err = True
                    elif fromZip == None:
                        await user.send("From State, Zip or City is missing.")
                        err = True
                    elif toName == None:
                        await user.send("To Name is missing.")
                        err = True
                    elif toAddress1 == None:
                        await user.send("To Address 1 is missing")
                        err = True
                    elif toCity == None:
                        await user.send("To State, Zip or City is missing.")
                        err = True
                    elif toState == None:
                        await user.send("To State, Zip or City is missing.")
                        err = True
                    elif toZip == None:
                        await user.send("To State, Zip or City is missing.")
                        err = True

                    if err == True:
                        await user.send("Please fix the errors and restart the label creation process.")
                        return
                    embed0 = discord.Embed(title="From Details: ", color=discord.Color.from_rgb(128,0,128))
                    embed0.add_field(name="Name: ", value=fromName, inline=False)
                    embed0.add_field(name="Address 1: ", value=fromAddress1, inline=False)
                    embed0.add_field(name="Address 2: ", value=fromAddress2, inline=False)
                    embed0.add_field(name="City: ", value=fromCity, inline=False)
                    embed0.add_field(name="State: ", value=fromState, inline=False)
                    embed0.add_field(name="Zip: ", value=fromZip, inline=False)
                    embed0.add_field(name="To Details: ", value="", inline=False)
                    embed0.add_field(name="Name: ", value=toName, inline=False)
                    embed0.add_field(name="Address 1: ", value=toAddress1, inline=False)
                    embed0.add_field(name="Address 2: ", value=toAddress2, inline=False)
                    embed0.add_field(name="City: ", value=toCity, inline=False)
                    embed0.add_field(name="State: ", value=toState, inline=False)
                    embed0.add_field(name="Zip: ", value=toZip, inline=False)
                    await user.send(embeds=[embed0])
                    if int(freeLabels) >= 1:
                        freeLabels = int(freeLabels)
                        freeLabels -= 1
                        await database.set(key0, freeLabels)
                    view = isAddCorrectPrompt()
                    message = await user.send(view=view)
                    view.message = message
                    await view.wait()
                    await view.disable_all_items()
                    from datetime import date
                    today = date.today()
                    data = {}
                    if str(lClass) != "usps_express":
                        print("here")
                        data = {
                            "labelType": str(lClass),
                            "Weight": int(weightVal),
                            "Date": str(today.strftime("%d/%m/%Y")),
                            "FromCountry": "US",
                            "FromName":  str(fromName),
                            "FromCompany": "",
                            "FromPhone": "",
                            "FromStreet": str(fromAddress1),
                            "FromStreet2": str(fromAddress2),
                            "FromZip": str(fromZip),
                            "FromCity": str(fromCity),
                            "FromState": str(fromState),
                            "ToCountry": "US",
                            "ToName": str(toName),
                            "ToCompany": "",
                            "ToPhone": "",
                            "ToStreet": str(toAddress1),
                            "ToStreet2": str(toAddress2),
                            "ToZip": str(toZip),
                            "ToCity": str(toCity),
                            "ToState": str(toState),
                            "Height": 10,
                            "Length": 10,
                            "Width": 10
                        }
                    else:
                        data = {
                            "provider_code": "usps",
                            "class": str(lClass),
                            "weight": int(weightVal),
                            "from_name": str(fromName),
                            "from_phone": "3342278854",
                            "from_address1": str(fromAddress1),
                            "from_address2": str(fromAddress2),
                            "from_city": str(fromCity),
                            "from_state": str(fromState),
                            "from_postcode": str(fromZip),
                            "from_country": "US",
                            "to_name": str(toName),
                            "to_phone": "3342278854",
                            "to_address1": str(toAddress1),
                            "to_address2": str(toAddress2),
                            "to_city": str(toCity),
                            "to_state": str(toState),
                            "to_postcode": str(toZip),
                            "to_country": "US"
                        }
                    #print("hi")
                    print(data)
                    if view.confirm == True:
                        print("confirm")
                        return data, price, False
                    elif view.add == True:
                        print("add")
                        return data, price, True
                    else:
                        return None, None, False
            else:
                await user.send("Not enough balance! Please deposit more.")
                return "Balance", None, False
            
class removeLab(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.val = None
        self.add_item(InputText(label="Which label would you like to remove?", placeholder="Enter a number from the 'Order #' to remove from orders"))
        
    async def callback(self, interaction: Interaction):
        embed = discord.Embed(title="Message: ", color=discord.Color.from_rgb(255,255,255))
        embed.add_field(name="Removing Label: ", value=f"#{self.children[0].value}", inline=False)
        self.val = str(self.children[0].value)
        await interaction.response.send_message(embeds=[embed])
        self.stop()                

class cancelAdd(discord.ui.View):
    removeLabel = None
    didRemove : bool = None
    cont : bool = None
    cancel : bool = None
    def __init__(self):
        super().__init__(timeout=None)

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    @discord.ui.button(label="Checkout",
                       style = discord.ButtonStyle.green)
    
    async def checkout(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.cont = True
        await interaction.response.defer()
        self.stop()
    @discord.ui.button(label="Remove From Orders",
                       style = discord.ButtonStyle.red)
    async def remove(self, button: discord.ui.Button, interaction: discord.Interaction):
        dep = removeLab(title = "Label To Remove From Orders: ")
        await interaction.response.send_modal(dep)
        await dep.wait()
        self.removeLabel = dep.val
        self.didRemove = True
        self.stop()
    @discord.ui.button(label="Cancel",
                       style = discord.ButtonStyle.red)
    async def canc(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.cancel = True
        await interaction.response.defer()
        self.stop()


class cancelB(discord.ui.View):
    cancel : bool = None
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Cancel",
                       style = discord.ButtonStyle.green)
    
    async def confirmBut(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.cancel = True
        await interaction.response.send_message("Button was pressed", ephemeral=True)
        self.stop()



@bot.command()
@commands.max_concurrency(number=1, per=commands.BucketType.user, wait=False)
async def label(ctx):

    await open_account(member=ctx.author)
    await open_account0(member=ctx.author)
    db = await aiosqlite.connect('main.db')
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM economy WHERE user_id = {ctx.author.id}")
    result = await cursor.fetchone()
    db0 = await aiosqlite.connect('ratesCus.db')
    cursor0 = await db0.cursor()
    await cursor0.execute(f"SELECT * FROM rates WHERE user_id = {ctx.author.id}")
    result0 = await cursor0.fetchone()
    user_id = ctx.author.id
    user = ctx.author
    for i in blacklist:
        if user_id == i:
            await user.send("Your kind isn't allowed to use our bot!")
            return
    view = button0()
    message = await user.send(view=view)
    view.message = message
    key0 = str(user_id) + "freeLabels"
    await view.wait()
    await view.disable_all_items()
    print(result[11])

    if view.uspsCarrier is None:
        await user.send("Closing Active Window")
    elif view.uspsCarrier is True:
        if await database.get(key0) == None:
            await database.set(key0, 0)
        print("okay")
        views = LabelClass()
        await user.send(view=views)
        price = 0
        await views.wait()
        isValid = True
        lClass = views.answer1
        weightVal = views.answer2
        #print(views.answer1)
        if lClass == "priority":
            if weightVal >= 1 and weightVal <= 8:
                if result0[1] == 1:
                    price = float(result0[5])
                elif result0[2] == 1:
                    #print("Hi")
                    price = float(result0[3])
                else:
                    price = 5.00
            elif weightVal >= 9 and weightVal <= 70:
                if result0[1] == 1:
                    price = float(result0[5])
                elif result0[2] == 1:
                    price = float(result0[4])
                else:
                    price = 7.00     
            else:
                isValid = False
                await user.send("Value must be 1-70 lbs")
            
        elif lClass == "usps_express":
            if weightVal >= 1 and weightVal <= 8:
                if result0[11] == 1:
                    price = float(result0[15])
                elif result0[12] == 1:
                    price = float(result0[13])
                else:
                    price = 8.00
            elif weightVal >= 9 and weightVal <= 35:
                if result0[11] == 1:
                    price = float(result0[15])
                elif result0[12] == 1:
                    price = float(result[14])
                else:
                    price = 12.00
            else:
                isValid = False
                await user.send("Value must be 1-35 lbs")
        elif lClass == "ground_oz":
            if weightVal >= 1 and weightVal < 16:
                if result0[16] == 1:
                    price = float(result0[20])
                else:
                    price = 3.00
            else:
                isValid = False
                await user.send("Invalid weight, please enter a value less than 16 oz")
        elif lClass == "ground_lbs":
            if weightVal >= 1 and weightVal <= 70:
                if result0[6] == 1:
                    price = float(result0[10])
                else:
                    price = 3.00
            else:
                isValid = False
                await user.send("Please enter a value between 1-70 lbs")
        else:
            await user.send("No class selected, closing active window!")
            isValid = False
            return
        if isValid:
            if await database.get(key0) == None:
                await database.set(key0, 0)
            freeLabels = await database.get(key0)
            if float(result[1]) >= price  or int(freeLabels) >= 1:
                if int(freeLabels) >= 1:
                    price = 0
                    freeLabels = int(freeLabels)
                    freeLabels -= 1
                    await database.set(key0, freeLabels)
                view = fromButton()
                message = await user.send(view=view)
                view.message = message
                await view.wait()
                await view.disable_all_items()
                print(view.editedWeight) 
                fromAddress1 = None
                fromAddress2 = None
                fromCity = None
                fromName = None
                fromZip = None
                fromState = None
                toAddress1 = None
                toAddress2 = None
                toCity = None
                toName = None
                toZip = None
                toState = None
                if view.fromBut is True:
                    if view.autofilled == False:
                        fromAd2 = view.isAdd2
                        line = view.fromFieldInfo.split('\n')
                        i = 0
                        for lin in line:
                            i += 1
                            if fromAd2 == True:
                                if i == 1:
                                    fromName = lin.upper()
                                if i == 2:
                                    fromAddress1 = lin.upper()
                                if i == 3:
                                    fromAddress2 = lin.upper()
                                if i == 4:
                                    x = lin.split(',')
                                    y = 0
                                    for word in x:
                                        y += 1
                                        if y == 1:
                                            fromCity = word.upper()
                                        if y == 2:
                                            z = 0
                                            word0 = word.split(" ")
                                            for next in word0:
                                                z += 1
                                                if z == 2:
                                                    fromState = next.upper()
                                                if z == 3:
                                                    fromZip = next

                            else:
                                if i == 1:
                                    fromName = lin.upper()
                                if i == 2:
                                    fromAddress1 = lin.upper()
                                    fromAddress2 = ""
                                if i == 3:
                                    x = lin.split(',')
                                    y = 0
                                    for word in x:
                                        y += 1
                                        if y == 1:
                                            fromCity = word.upper()
                                        if y == 2:
                                            z = 0
                                            word0 = word.split(" ")
                                            for next in word0:
                                                z += 1
                                                if z == 2:
                                                    fromState = next.upper()
                                                if z == 3:
                                                    fromZip = next
                    else:
                        if view.isAdd2 == True:
                            fromAddress2 = view.tAd2
                        else:
                            fromAddress2 = ""
                        fromAddress1 = view.tAd1
                        fromState = view.tSte
                        fromCity = view.tCty
                        fromZip = view.tZp
                        fromName = view.tNme

                    toAd2 = view.toisAdd2
                    line0 = view.toField.split('\n')
                    i = 0
                    for lin in line0:
                        i += 1
                        if toAd2 == True:
                            if i == 1:
                                toName = lin.upper()
                            if i == 2:
                                toAddress1 = lin.upper()
                            if i == 3:
                                toAddress2 = lin.upper()
                            if i == 4:
                                x = lin.split(',')
                                y = 0
                                for word in x:
                                    y += 1
                                    if y == 1:
                                        toCity = word.upper()
                                    if y == 2:
                                        z = 0
                                        word0 = word.split(" ")
                                        for next in word0:
                                            z += 1
                                            if z == 2:
                                                toState = next.upper()
                                            if z == 3:
                                                toZip = next

                        else:
                            if i == 1:
                                toName = lin.upper()
                            if i == 2:
                                toAddress1 = lin.upper()
                                toAddress2 = ""
                            if i == 3:
                                x = lin.split(',')
                                y = 0
                                for word in x:
                                    y += 1
                                    if y == 1:
                                        toCity = word.upper()
                                    if y == 2:
                                        z = 0
                                        word0 = word.split(" ")
                                        for next in word0:
                                            z += 1
                                            if z == 2:
                                                toState = next.upper()
                                            if z == 3:
                                                toZip = next

                    err = False
                    if fromName == None:
                        await user.send("From Name is missing.")
                        err = True
                    elif fromAddress1 == None:
                        await user.send("From Address 1 is missing.")
                        err = True
                    elif fromCity == None:
                        await user.send("From State or Zip, City is missing.")
                        err = True
                    elif fromState == None:
                        await user.send("From State, Zip or City is missing.")
                        err = True
                    elif fromZip == None:
                        await user.send("From State, Zip or City is missing.")
                        err = True
                    elif toName == None:
                        await user.send("To Name is missing.")
                        err = True
                    elif toAddress1 == None:
                        await user.send("To Address 1 is missing")
                        err = True
                    elif toCity == None:
                        await user.send("To State, Zip or City is missing.")
                        err = True
                    elif toState == None:
                        await user.send("To State, Zip or City is missing.")
                        err = True
                    elif toZip == None:
                        await user.send("To State, Zip or City is missing.")
                        err = True

                    if err == True:
                        await user.send("Please fix the errors and restart the label creation process.")
                        return
                    embed0 = discord.Embed(title="From Details: ", color=discord.Color.from_rgb(128,0,128))
                    embed0.add_field(name="Name: ", value=fromName, inline=False)
                    embed0.add_field(name="Address 1: ", value=fromAddress1, inline=False)
                    embed0.add_field(name="Address 2: ", value=fromAddress2, inline=False)
                    embed0.add_field(name="City: ", value=fromCity, inline=False)
                    embed0.add_field(name="State: ", value=fromState, inline=False)
                    embed0.add_field(name="Zip: ", value=fromZip, inline=False)
                    embed0.add_field(name="To Details: ", value="", inline=False)
                    embed0.add_field(name="Name: ", value=toName, inline=False)
                    embed0.add_field(name="Address 1: ", value=toAddress1, inline=False)
                    embed0.add_field(name="Address 2: ", value=toAddress2, inline=False)
                    embed0.add_field(name="City: ", value=toCity, inline=False)
                    embed0.add_field(name="State: ", value=toState, inline=False)
                    embed0.add_field(name="Zip: ", value=toZip, inline=False)
                    await user.send(embeds=[embed0])
                    view = isAddCorrectPrompt()
                    message = await user.send(view=view)
                    view.message = message
                    await view.wait()
                    await view.disable_all_items()

                    isReady = view.confirm
                    
                    dataArr = []
                    today = date.today()
                    data = None
                    if str(lClass) != "usps_express":
                        data = {
                            "labelType": str(lClass),
                            "Weight": int(weightVal),
                            "Date": str(today.strftime("%d/%m/%Y")),
                            "FromCountry": "US",
                            "FromName":  str(fromName),
                            "FromCompany": "",
                            "FromPhone": "",
                            "FromStreet": str(fromAddress1),
                            "FromStreet2": str(fromAddress2),
                            "FromZip": str(fromZip),
                            "FromCity": str(fromCity),
                            "FromState": str(fromState),
                            "ToCountry": "US",
                            "ToName": str(toName),
                            "ToCompany": "",
                            "ToPhone": "",
                            "ToStreet": str(toAddress1),
                            "ToStreet2": str(toAddress2),
                            "ToZip": str(toZip),
                            "ToCity": str(toCity),
                            "ToState": str(toState),
                            "Height": 10,
                            'Length': 10,
                            "Width": 10
                        }
                    else:
                        data = {
                            "provider_code": "usps",
                            "class": str(lClass),
                            "weight": int(weightVal),
                            "from_name": str(fromName),
                            "from_phone": "3342278854",
                            "from_address1": str(fromAddress1),
                            "from_address2": str(fromAddress2),
                            "from_city": str(fromCity),
                            "from_state": str(fromState),
                            "from_postcode": str(fromZip),
                            "from_country": "US",
                            "to_name": str(toName),
                            "to_phone": "3342278854",
                            "to_address1": str(toAddress1),
                            "to_address2": str(toAddress2),
                            "to_city": str(toCity),
                            "to_state": str(toState),
                            "to_postcode": str(toZip),
                            "to_country": "US"
                        }
                    dataArr.append(data)
                    tempBal = float(result[1])
                    tempBal -= price
                    embed0 = discord.Embed(title="New Cost ($): ", color=discord.Color.from_rgb(128,0,128))
                    embed0.add_field(name= "Order: ", value= f"Order #1: Price: ${price}, To: {toName}", inline=False)
                    if view.add == True:
                        embed2 = discord.Embed(title="Current Cart: ", color=discord.Color.from_rgb(128,0,128))
                        embed2.add_field(name="Number of Labels ", value = f"{len(dataArr)}",inline=False)
                        embed2.add_field(name="Total Cost: ", value = "${0:.2f}".format(price),inline=False)
                        await user.send(embeds=[embed2])
                        isReady = False
                        data0, price0, again = await addAnotherLabel(ctx, tempBal)
                        if data0 == "Balance":
                            isReady = True
                        elif again == True and data0 != None:
                                dataArr.append(data0)
                                price += price0
                                try:
                                    embed0.add_field(name="Order: ", value = f"Order #2: Price: ${price0}, To: {data0['ToName']}",inline=False)
                                except:
                                    embed0.add_field(name="Order: ", value = f"Order #2: Price: ${price0}, To: {data0['to_name']}",inline=False)
                        elif again == False and data0 != None:
                            dataArr.append(data0)
                            price += price0
                            isReady = False
                            try:
                                embed0.add_field(name="Order: ", value = f"Order #2: Price: ${price0}, To: {data0['ToName']}",inline=False)
                            except:
                                embed0.add_field(name="Order: ", value = f"Order #2: Price: ${price0}, To: {data0['to_name']}",inline=False)
                        elif again == False and data0 == None:
                            isReady = False
                        ind = 2
                        while again == True:
                            ind += 1
                            embed2 = discord.Embed(title="Current Cart: ", color=discord.Color.from_rgb(128,0,128))
                            embed2.add_field(name="Number of Labels ", value = f"{len(dataArr)}",inline=False)
                            embed2.add_field(name="Total Cost: ", value ="${0:.2f}".format(price),inline=False)
                            await user.send(embeds=[embed2])
                            data0, price0, again = await addAnotherLabel(ctx, tempBal)
                            #print(price)
                            if data0 == "Balance":
                                isReady = True
                                break
                            elif again == True and data0 != None:
                                dataArr.append(data0)
                                price += price0
                                try:
                                    embed0.add_field(name="Order: ", value = f"Order #{ind}: Price: ${price0}, To: {data0['ToName']}",inline=False)
                                except:
                                    embed0.add_field(name="Order: ", value = f"Order #{ind}: Price: ${price0}, To: {data0['to_name']}",inline=False)
                            elif again == False and data0 != None:
                                dataArr.append(data0)
                                price += price0
                                isReady = False
                                try:
                                    embed0.add_field(name="Order: ", value = f"Order #{ind}: Price: ${price0}, To: {data0['ToName']}",inline=False)
                                except:
                                    embed0.add_field(name="Order: ", value = f"Order #{ind}: Price: ${price0}, To: {data0['to_name']}",inline=False)
                                break
                            elif again == False and data0 == None:
                                isReady = False
                                break
                        embed0.add_field(name="Cost: ", value="${0:.2f}".format(price), inline=False)
                        await user.send(embeds=[embed0])
                        view10 = cancelAdd()
                        await user.send(view=view10)
                        await view10.wait()
                        await view10.disable_all_items()
                        errRe = True
                        cont = False
                        if view10.cont == True:
                            isReady = True
                            cont = True
                        elif view10.cancel == True:
                            cont = True
                            return
                        elif view10.didRemove == True:
                            ind = 0
                            embed0 = discord.Embed(title="New Cost ($): ", color=discord.Color.from_rgb(128,0,128))
                            cont = False
                            print("hehehe")
                            for i in range(len(dataArr)):
                                ind += 1
                                print(i)
                                if i == int(view10.removeLabel) - 1:
                                    tempLC = None
                                    try:
                                        tempLC = dataArr[i]['labelType']
                                    except:
                                        tempLC = dataArr[i]['class']
                                    lc, priceTem = await computePrice0(user_id, dataArr[i]['Weight'], tempLC)
                                    price -= priceTem
                                    dataArr.pop(i)
                                    #print(dataArr[i])
                                    print("deleted from data")
                                    errRe = False

                            ind0 = 0
                            for i in range(len(dataArr)):
                                ind0 += 1
                                tempLC = None
                                try:
                                    tempLC = dataArr[i]['labelType']
                                except:
                                    tempLC = dataArr[i]['class']
                                lc, priceTem = await computePrice0(user_id, dataArr[i]['Weight'], tempLC)
                                try:
                                    embed0.add_field(name="Order: ", value = f"Order #{ind0}: Price: ${priceTem}, To: {dataArr[i]['ToName']}",inline=False)
                                except:
                                    embed0.add_field(name="Order: ", value = f"Order #{ind0}: Price: ${priceTem}, To: {dataArr[i]['to_name']}",inline=False)
                            embed0.add_field(name="Cost: ", value="${0:.2f}".format(price), inline=False)
                            await user.send(embeds=[embed0])
                                
                            if errRe == True:
                                await user.send("Error removing label! (Value does not exist. Proceeding to checkout!)")
                            isReady = True
                        
                        while cont == False:
                            errRe = True
                            view10 = cancelAdd()
                            await user.send(view=view10)
                            await view10.wait()
                            await view10.disable_all_items()
                            if view10.cont == True:
                                isReady = True
                                cont = True
                            elif view10.cancel == True:
                                cont = True
                                return
                            elif view10.didRemove == True:
                                ind = 0
                                embed0 = discord.Embed(title="New Cost ($): ", color=discord.Color.from_rgb(128,0,128))
                                cont = False
                                print("hehehe")
                                for i in range(len(dataArr)):
                                    ind += 1
                                    print(i)
                                    #lc, priceTem = await computePrice(user_id, dataArr[i]['Weight'])
                                    if i == int(view10.removeLabel) - 1:
                                        tempLC = None
                                        try:
                                            tempLC = dataArr[i]['labelType']
                                        except:
                                            tempLC = dataArr[i]['class']
                                        lc, priceTem = await computePrice0(user_id, dataArr[i]['Weight'], tempLC)
                                        price -= priceTem
                                        dataArr.pop(i)
                                        errRe = False
                                        break
                                ind = 0
                                for i in range(len(dataArr)):
                                    ind += 1
                                    tempLC = None
                                    try:
                                        tempLC = dataArr[i]['labelType']
                                    except:
                                        tempLC = dataArr[i]['class']
                                    lc, priceTem = await computePrice0(user_id, dataArr[i]['Weight'], tempLC)
                                    try:
                                        embed0.add_field(name="Order: ", value = f"Order #{ind}: Price: ${priceTem}, To: {dataArr[i]['ToName']}",inline=False)
                                    except:
                                        embed0.add_field(name="Order: ", value = f"Order #{ind}: Price: ${priceTem}, To: {dataArr[i]['to_name']}",inline=False)
                                embed0.add_field(name="Cost: ", value="${0:.2f}".format(price), inline=False)
                                await user.send(embeds=[embed0])
                                    
                                if errRe == True:
                                    await user.send("Error removing label! (Value does not exist. Proceeding to checkout!)")
                                isReady = True



                        #print(dataArr)  
                    elif view.confirm == None:
                        isReady = False
                    today = date.today()
                    data = None
                    if str(lClass) != "usps_express":
                        data = {
                            "labelType": str(lClass),
                            "Weight": int(weightVal),
                            "Date": str(today.strftime("%d/%m/%Y")),
                            "FromCountry": "US",
                            "FromName":  str(fromName),
                            "FromCompany": "",
                            "FromPhone": "",
                            "FromStreet": str(fromAddress1),
                            "FromStreet2": str(fromAddress2),
                            "FromZip": str(fromZip),
                            "FromCity": str(fromCity),
                            "FromState": str(fromState),
                            "ToCountry": "US",
                            "ToName": str(toName),
                            "ToCompany": "",
                            "ToPhone": "",
                            "ToStreet": str(toAddress1),
                            "ToStreet2": str(toAddress2),
                            "ToZip": str(toZip),
                            "ToCity": str(toCity),
                            "ToState": str(toState),
                            "Height": 10,
                            'Length': 10,
                            "Width": 10
                        }
                    else:
                        data = {
                            "provider_code": "usps",
                            "class": str(lClass),
                            "weight": int(weightVal),
                            "from_name": str(fromName),
                            "from_phone": "3342278854",
                            "from_address1": str(fromAddress1),
                            "from_address2": str(fromAddress2),
                            "from_city": str(fromCity),
                            "from_state": str(fromState),
                            "from_postcode": str(fromZip),
                            "from_country": "US",
                            "to_name": str(toName),
                            "to_phone": "3342278854",
                            "to_address1": str(toAddress1),
                            "to_address2": str(toAddress2),
                            "to_city": str(toCity),
                            "to_state": str(toState),
                            "to_postcode": str(toZip),
                            "to_country": "US"
                        }
                    if isReady == True and float(result[1]) >= price:
                        #print("hiii")
                        labelsC = 0
                        for i in range(len(dataArr)):
                            print(dataArr[i])
                            labelsC += 1
                            response = None
                            express = False
                            if dataArr[i].get('class'):
                                express = True
                                response = requests.post(url="api/v1/orders", json=dataArr[i], headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'}).json()
                            else:
                                express = False
                                response = requests.post(url='api/v2/order/create-order', json=dataArr[i], headers={'x-api-key': 'd928af43-c610-4ccc-8618-46e486cc35cc'}).json()
                                
                            print(response)
                                
                            await user.send("Creating label, please wait...")
                            idOR = None
                            if express == False:
                                idOR = response['label']['_id']
                            else:
                                idOR = response['order']['id']
                            await asyncio.sleep(7)
                            response = None
                            if express == False:
                                response = requests.get(url=f"api/v2/order/download/{idOR}", headers={'x-api-key': 'd928af43-c610-4ccc-8618-46e486cc35cc'})
                            else:
                                response = requests.get(url=f"api/v1/orders/{idOR}.pdf", headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'})
                            file = open(f"{user_id}_{idOR}.pdf", "wb")
                            file.write(response.content)

                            file.close()

                            file0 = discord.File(f"{user_id}_{idOR}.pdf")
                            try:
                                await user.send(file=file0)
                            except:
                                with open(f"{user_id}_{idOR}.pdf", 'rb') as f:
                                    respo = dbx.files_upload(f.read(), f"/{user_id}_{idOR}.pdf")
                                    shared_link_metadata = dbx.sharing_create_shared_link(respo.path_display)
                                    file_link = shared_link_metadata.url
                                    file_link = file_link.replace("?dl=1", "?dl=0")
                                    embed0 = discord.Embed(title="Label Details: ", color=discord.Color.from_rgb(128,0,128))
                                    embed0.add_field(name="Link: ", value=f"[Labels]({file_link})", inline=False)
                                    await user.send(embed=embed0)
                            money = result[1]
                            money -= price
                            print(price)
                            if result[2] != None:
                                mon = float(result[2])
                                mon += float(price)
                                await db.execute(f"UPDATE economy SET spent = {mon} WHERE user_id = {user_id}")
                                await db.commit()
                            else:
                                await db.execute(f"UPDATE economy SET spent = {price} WHERE user_id = {user_id}")
                                await db.commit()
                            if result[3] != None:
                                lab = int(result[3])
                                lab += labelsC
                                await db.execute(f"UPDATE economy SET labelsCreated = {lab} WHERE user_id = {user_id}")
                                await db.commit()
                            else:
                                await db.execute(f"UPDATE economy SET labelsCreated = {1} WHERE user_id = {user_id}")
                                await db.commit()
                        await db.execute(f"UPDATE economy SET money = {money} WHERE user_id = {user_id}")
                        await db.commit()
                    else:
                        await user.send("Timed out!")
                                
            else:
                await user.send("Not enough balance!")
                return
        else:
            await user.send("Error Occured Trying to Create Label, Must Restart Label Creation Process")

    elif view.depositBal == True:
        if view.amount >= 1:
            amount = float(view.amount)
            if amount.is_integer():
                random = str(uuid.uuid4()) # Convert UUID format to a Python string.
                random = random.upper() # Make all characters uppercase.
                random = random.replace("-","") # Remove the UUID '-'.
                cashFor0 = str(random[0:6])
                embed0 = discord.Embed(title="Deposit (Minimum: $1) ", color=discord.Color.from_rgb(128,0,128))
                embed0.add_field(name="Cashapp: ", value="$samurailabels", inline=False)
                embed0.add_field(name="Venmo: ", value="@samurailabels", inline=False)
                embed0.add_field(name="Amount To Send: ", value=str(amount), inline=False)
                embed0.add_field(name="'For' Code: ", value=cashFor0, inline=False)
                await user.send(embeds=[embed0])
                adjustAmt = int(amount)
                key0 = keyCashAmt + str(user_id)
                key1 = keyCashFor + str(user_id)
                await database.set(key0, adjustAmt)
                await database.set(key1, cashFor0)
                await user.send("After payment has been sent, we will notify you when payment has processed successfully into your balance!\nThe payment window will only last an hour. ")
                task_generator(ctx)
                return
            else:
                await user.send("Amount must be a whole number!")
                return
        else:
            await user.send("Value must be greater than or equal to $1!")

    else:
        print("Cancel")

@label.error
async def on_command_error(ctx,error):
    if isinstance(error, commands.MaxConcurrencyReached):
        user = ctx.author
        if error.per == commands.BucketType.user:
            await user.send("Window already active, cannot use command unless window closes, or is completed.")



@bot.command()
async def download(ctx, arguments):
    user = ctx.author
    user_id = ctx.author.id
    orderIdsKey = "orders" + str(user_id)
    labels = None
    if await database.get(orderIdsKey) != None:
        labels = await database.get(orderIdsKey)
    else:
        await user.send("No labels found!")
        return
    if arguments == "HELP":
        await user.send("To download files from History, please follow the instructions:")
        await user.send("To download files from a starting point to an end point, Type '!download 1-50' (This will download files from file 1 to file 50).")
        await user.send("If you need to download multiple files separately type '!download 1,5,8,10' This will ONLY download file(s) 1,5,8,10")
        await user.send("If you want to download all the files, type '!download ALL'")
        await user.send("Remember, you can't download more files than you have in your 'History'!")
    elif arguments == 'ALL':
        merger = PdfMerger()
        import random
        x = random.randint(1,50000000)
        pdf_files = []
        for i in labels:
            response = requests.get(url=f"api/v1/orders/{i}.pdf", headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'})
            file = open(f"{user_id}-{i}.pdf", "wb")
            pdf_files.append(f"{user_id}-{i}.pdf")
            file.write(response.content)
            file.close()
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        merger.write(f"{user_id}-{x}.pdf")
        merger.close()
        file0 = discord.File(f"{user_id}-{x}.pdf")
        await user.send(file=file0)
    elif str(arguments).find("-") != -1:
        rangeFind = str(arguments).split("-")
        merger = PdfMerger()
        import random
        x = random.randint(1,50000000)
        pdf_files = []
        if labels[int(rangeFind[0]) - 1] and labels[int(rangeFind[1])]:
            print("successsssss")
            for i in range(int(rangeFind[0]) - 1, int(rangeFind[1])):
                response = requests.get(url=f"api/v1/orders/{labels[i]}.pdf", headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'})
                file = open(f"{user_id}-{labels[i]}.pdf", "wb")
                pdf_files.append(f"{user_id}-{labels[i]}.pdf")
                file.write(response.content)
                file.close()
            for pdf_file in pdf_files:
                merger.append(pdf_file)
            merger.write(f"{user_id}-{x}.pdf")
            merger.close()
            file0 = discord.File(f"{user_id}-{x}.pdf")
            await user.send(file=file0)
        else:
            await user.send("Label out of range error!, try lowering the end point.")
            return
    elif str(arguments).find(',') != -1:
        #print("Hi")
        sequence = str(arguments).split(",")
        merger = PdfMerger()
        import random
        x = random.randint(1,50000000)
        pdf_files = []
        print(sequence)
        for i in range(len(sequence)):
            print(sequence[i])
            if labels[int(sequence[i]) - 1]:
                response = requests.get(url=f"api/v1/orders/{labels[i]}.pdf", headers={'Auth': '4acbba73-80ae-4521-b7d6-835b23555068'})
                file = open(f"{user_id}-{labels[i]}.pdf", "wb")
                pdf_files.append(f"{user_id}-{labels[i]}.pdf")
                file.write(response.content)
                file.close()
            else:
                await user.send("List out of range error.")
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        merger.write(f"{user_id}-{x}.pdf")
        merger.close()
        file0 = discord.File(f"{user_id}-{x}.pdf")
        await user.send(file=file0)
        return
    else:
        await user.send("Invalid response")
        return


@bot.command()
async def setMon(ctx, user, amount):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160 or user_id == 647962580983218180:
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"UPDATE economy SET money = {int(amount)} WHERE user_id = {user}")
        await db.commit()
        await cursor.close()
        await db.close()
        
@bot.command()
async def add(ctx, user, amount):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160 or user_id == 647962580983218180:
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT money FROM economy WHERE user_id = {user}")
        data = await cursor.fetchone()
        money = data[0] + float(amount)
        await cursor.execute(f"UPDATE economy SET money = {money} WHERE user_id = {user}")
        await db.commit()
        await cursor.close()
        await db.close()

@bot.command()
async def remove(ctx, user, amount):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT money FROM economy WHERE user_id = {user}")
        data = await cursor.fetchone()
        money = data[0] - float(amount)
        await cursor.execute(f"UPDATE economy SET money = {money} WHERE user_id = {user}")
        await db.commit()
        await cursor.close()
        await db.close()

@bot.command()
async def delete(ctx):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160 or user_id == 647962580983218180:
        orderIdsKey = "orders" + str(user_id)
        await database.delete(orderIdsKey)

@bot.command()
async def profile(ctx, user):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        await cursor.execute(f"SELECT * FROM economy WHERE user_id = {user}")
        result = await cursor.fetchone()
        UUSer = ctx.author
        money = result[1]
        moneyID = result[2]
        labelCreated = result[3]
        rateKey = result[6]
        rateKey0 = result[9]
        rateKey1 = result[10]
        typeLabel = result[8]
        embed0 = discord.Embed(title="Customer Details: ", color=discord.Color.from_rgb(128,0,128))
        embed0.add_field(name="Money Spent ($) ", value="$" + str(moneyID), inline=False)
        embed0.add_field(name="Wallet ($) ", value="$" + str(money), inline=False)
        embed0.add_field(name="Labels Created: ", value=str(labelCreated), inline=False)
        embed0.add_field(name="Label Type: ", value=str(typeLabel), inline=False)
        embed0.add_field(name="Rates (1-70): ", value=str(rateKey), inline=False)
        embed0.add_field(name="Rates (1-8): ", value=str(rateKey0), inline=False)
        embed0.add_field(name="Rates (9-70): ", value=str(rateKey1), inline=False)
        await UUSer.send(embeds=[embed0])




@bot.command()
async def passRate(ctx, user, rate, type):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        db = await aiosqlite.connect('ratesCus.db')
        cursor = await db.cursor()
        if type == "priority":
            await cursor.execute(f"UPDATE rates SET usps_priority = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET usps_priorityRate = {float(rate)} WHERE user_id = {user}")
        elif type == "ground_oz":
            await cursor.execute(f"UPDATE rates SET ga_oz = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET ga_ozRate = {float(rate)} WHERE user_id = {user}")
        elif type == "ground_lbs":
            await cursor.execute(f"UPDATE rates SET ga = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET gaRate = {float(rate)} WHERE user_id = {user}")
        elif type == "express":
            await cursor.execute(f"UPDATE rates SET express = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET expressRate = {float(rate)} WHERE user_id = {user}")
        await db.commit()
        await cursor.close()
        await db.close()

@bot.command()
async def removeRate(ctx, user, type):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        db = await aiosqlite.connect('ratesCus.db')
        cursor = await db.cursor()
        if type == "priority":
            await cursor.execute(f"UPDATE rates SET usps_priority = {0} WHERE user_id = {user}")
        elif type == "ground_oz":
            await cursor.execute(f"UPDATE rates SET ga_oz = {0} WHERE user_id = {user}")
        elif type == "ground_lbs":
            await cursor.execute(f"UPDATE rates SET ga = {0} WHERE user_id = {user}")
        elif type == "express":
            await cursor.execute(f"UPDATE rates SET express = {0} WHERE user_id = {user}")
        await db.commit()
        await cursor.close()
        await db.close()

@bot.command()
async def passRateOp2(ctx, user, rate0, rate1, type):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        db = await aiosqlite.connect('ratesCus.db')
        cursor = await db.cursor()
        if type == "priority":
            await cursor.execute(f"UPDATE rates SET usps_priorityOp2 = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET usps_priorityRate0 = {float(rate0)} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET usps_priorityRate1 = {float(rate1)} WHERE user_id = {user}")
        elif type == "ground_oz":
            await cursor.execute(f"UPDATE rates SET ga_ozOp2 = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET ga_ozRate0 = {float(rate0)} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET ga_ozRate1 = {float(rate1)} WHERE user_id = {user}")
        elif type == "ground_lbs":
            await cursor.execute(f"UPDATE rates SET gaOp2 = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET gaRate0 = {float(rate0)} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET gaRate1 = {float(rate1)} WHERE user_id = {user}")
        elif type == "express":
            await cursor.execute(f"UPDATE rates SET expressOp2 = {1} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET expressRate0 = {float(rate0)} WHERE user_id = {user}")
            await cursor.execute(f"UPDATE rates SET expressRate1 = {float(rate1)} WHERE user_id = {user}")

        await db.commit()
        await cursor.close()
        await db.close()
@bot.command()
async def removeRateOp2(ctx, user, type):
    user_id = ctx.author.id
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        db = await aiosqlite.connect('ratesCus.db')
        cursor = await db.cursor()
        if type == "priority":
            await cursor.execute(f"UPDATE rates SET usps_priorityOp2 = {0} WHERE user_id = {user}")
        elif type == "ground_oz":
            await cursor.execute(f"UPDATE rates SET ga_ozOp2 = {0} WHERE user_id = {user}")
        elif type == "ground_lbs":
            await cursor.execute(f"UPDATE rates SET gaOp2 = {0} WHERE user_id = {user}")
        elif type == "express":
            await cursor.execute(f"UPDATE rates SET expressOp2 = {0} WHERE user_id = {user}")
        await db.commit()
        await cursor.close() 
        await db.close()
    

@bot.command() 
async def givelabel(ctx, user, amount):
    user_id = ctx.author.id
    key0 = str(user) + "freeLabels"
    labels = await database.get(key0)
    if user_id == 489237955559292949 or user_id == 438169261903708160:
        if labels == None:
            await database.set(key0, amount)
        else:
            finalVal = labels + amount
            await database.set(key0, finalVal)
        user0 = bot.get_user(int(user))
        await user0.send("You have been selected for the giveaway, thanks for participating!")
        await user0.send(str(amount) + " labels has been added to your account. NOTE: labels cannot be redeemed through CSV!")




@bot.event
async def on_ready():
    print('is ready')
    global database
    database = await db.new("IGNORE","data")



# Run the bot
bot.run('MTIwMzcxNjY3NTI5MjIzMzc4OA.GLDnwP.EpvOFliYBUrYH0-nZYwrQTMtU2Nv5HEvov2I5M')