# iCloudTG
iCloud feature integration (such as Find My iPhone) with Telegram for easier access on any device!

This is a bot I made, that integrates features of iCloud/iPhones into Telegram for much easier access. I made this as a substitute to some parts of the Apple ecosystem on non-MacOS devices. I am actively working on this bot as it's not finished and more features will be added. Plus I need to fix a few bugs. Any help would be greatly appreciated through my socials (Discord, BradsTheDeveloper#5519, or Telegram, @bradley_austin)

# Features
Currently you can:
* check your phone's battery (with the /battery command)
* play a sound to find your phone (with the /ringmyphone command)
* put your phone in Lost Mode (with the /lostmode command)

More features are coming soon!

# Installation & setup for self-hosting (you won't need to do this once I have figured out the issues below)
Currently you will have to self-host the bot as I haven't found a way to allow the bot to fully rely on Telegram (I need to find a way to allow the user to login with their Apple ID inside of Telegram and not in the terminal) and host it online. (DM me if you know how, I would greatly appreciate it)

1. Install **Python 3** if you don't already have it.
2. Install python-telegram-bot ('pip install python-telegram-bot' in the terminal) and pyiCloud ('pip install pyicloud' in the terminal)
3. Download the main.py file from the repository folder.
4. Add your bot token (get it by creating a new bot in BotFather, [this link](https://core.telegram.org/bots#6-botfather) will show you how if you don't already know), Apple ID email/password and desired lost mode message/phone number in their respected places (the variables at the top of the page, I can't see this information though!).
5. Save and run the file.
6. Start using the bot!
