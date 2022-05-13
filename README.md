# Cyber_Hacker_24315_Auto_Responder

This is an auto responder to Telegram user account. I also use this. Now I describe code.

## Step 1

First you want to install telethon module. To that run following in your command prompt or any other terminal.
```bash
pip install telethon
```

Then you can download this code.

- Then you want to get your api_id and your api_hash.
- You can get it from [this](https://www/my.telegram.org).
- In this site first you want to verify your number. After verify your number, Click Api development tools. 
- Then give name to your project and give a short name.

### Then you can get your api id and your api hash. Then replace your api id to apiId variable as a Intiger, and replace your api hash to apiHash varible as a String.

Step 2

After that if you want to send file(photos, files) with messages replace file's derect link to dp variable. If you do not need it, you can remove 'file=dp' in 14, 24, 29 lines.

Now you can change ``@client.on(events.NewMessage(pattern='(?i)hey|Hey|Hi|hi|Hello|hello'))``. In this code only change string in ``pattern='(?i)hey|Hey|Hi|hi|Hello|hello')``. In this string don't change '(?i)'. You can change only ``'hey|Hey|Hi|hi|Hello|hello'`` in this string. Use ``|`` as divider in add many strings. In this code If user send hey or Hey or Hi or hi or Hello or hello this auto responder send message in 12th line. Like this you can change other functions. You can copy paste this functions many times, you can add many message filters.
