from telethon import TelegramClient, events

apiId = ...
apiHash = '...'

client = TelegramClient('user', apiId, apiHash)
client.start()
dp = '...'

@client.on(events.NewMessage(pattern='(?i)hey|Hey|Hi|hi|Hello|hello'))
async def handler(event):
    helloMsg = 'Hello I am Cyber Hacker (It\'s not my real nameπ)\n\nIf you want to know about me please check this. [About Cyber hacker 24315](t.me/Cyber_Hacker_24315_About).\n\nSend this keywords to know more.\n\n    github\n    cyber_hackers_projects\n    skills\n\n Note: This message and message comes by above keywords are programmable messages. But I am a real human. So if you want to contact me wait for I able to come online.'
    sender = await event.get_input_sender()
    await client.send_message(sender, helloMsg, file=dp, link_preview=False)

@client.on(events.NewMessage(pattern='(?i)github'))
async def handler(event):
    githubMsg = 'This is my [My Github Account](https://github.com/SadahamAnuththara24315)'
    sender = await event.get_input_sender()
    await client.send_message(sender, file=dp, link_preview=False)

@client.on(events.NewMessage(pattern='(?i)cyber_hackers_projects'))
async def handler(event):
    projectsMsg = 'Check my projects from [Projects of Cyber Hacker 24315](t.me/Projects_of_Cyber_Hacker_24315)'
    sender = await event.get_input_sender()
    await client.send_message(sender, file=dp, link_preview=False)

@client.on(events.NewMessage(pattern='(?i)skills'))
async def handler(event):
    skillsMsg = '**Skills** :-\n    Programming languages :-\n        Html, Css, Javascript{π‘}\n        Python {π’}\n        Java {π΄}\n        Jquery{π΄}\n\n    **Other skills**:-\n        Telegram bot developing{π’}\n        Python Gui(Graphical user interface) creating (application and game development) {π’}\n        Font end Web developing{π’}\n        OOP (Object Oriented Programming) {π΄}\n\n**While Learning** :-\n    Python OOP{π΄}\n\n            π΄ :- Low Knowledge\n            π  :- Low - Middle knowledge\n            π‘ :- Middle - High knowledge\n            π’ :- High knowledge\n'
    sender = await event.get_input_sender()
    await client.send_message(sender, link_preview=False)

client.run_until_disconnected()
