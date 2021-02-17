appleid_email = ''
appleid_password = ''
lostmode_phonenumber = ''
lostmode_message = ''

from pyicloud import PyiCloudService
#api = PyiCloudService(appleid_email, appleid_password)
api = PyiCloudService(appleid_email, appleid_password)

if api.requires_2fa:
    print ("Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = api.validate_2fa_code(code)
    print("Code validation result: %s" % result)

    if not result:
        print("Failed to verify security code")
        sys.exit(1)

    if not api.is_trusted_session:
        print("Session is not trusted. Requesting trust...")
        result = api.trust_session()
        print("Session trust result %s" % result)

        if not result:
            print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
elif api.requires_2sa:
    import click
    print("Two-step authentication required. Your trusted devices are:")

    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print("  %s: %s" % (i, device.get('deviceName',
            "SMS to %s" % device.get('phoneNumber'))))

    device = click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")
        sys.exit(1)

    code = click.prompt('Please enter validation code')
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")
        sys.exit(1)

# End of signin section

from telegram.ext import Updater
updater = Updater(token='1648470032:AAGtmwa8eD9IxRveHN3y2EkAyV34hvYHjY0', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to iCloudTG! Type or select a command to get started!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start of ringmyphone section
def ringmyphone(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ringing your phone...")
    api.iphone.play_sound()

from telegram.ext import CommandHandler
ringmyphone_handler = CommandHandler('ringmyphone', ringmyphone)
dispatcher.add_handler(ringmyphone_handler)
# End of ringmyphone section

# Start of battery section
def battery(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Checking your phone's battery percentage...")
    status = api.iphone.status()
    import math
    batteryLevel=str(round(status["batteryLevel"],2)*100)+"%"
    batteryMessage = "Your phone has " + batteryLevel + " battery."
    context.bot.send_message(chat_id=update.effective_chat.id, text=batteryMessage)

from telegram.ext import CommandHandler
battery_handler = CommandHandler('battery', battery)
dispatcher.add_handler(battery_handler)
# End of battery section

# Start of battery section
def lostmode(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Turning on Lost Mode...")
    api.iphone.lost_device(lostmode_phonenumber, lostmode_message)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lost Mode is now on.")

from telegram.ext import CommandHandler
lostmode_handler = CommandHandler('lostmode', lostmode)
dispatcher.add_handler(lostmode_handler)
# End of lostmode section

updater.start_polling()