# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]


import time
from .vars import Var
from WebStreamer.bot.clients import *

print('\n')
print('------------------- Initializing Telegram Bot -------------------')

StreamBot.start()
bot_info = StreamBot.get_me()
__version__ = 1.06
StartTime = time.time()
