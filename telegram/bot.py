# python
# pip install telepot
import telepot
import logging
import os
import module

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "token"

def handler(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg,long=True)
    
    if content_type == "text":
        # bot.sendMessage(chat_id, "{}".format(msg["text"]))
        str_message = msg["text"]
        if str_message[0:1] == "/":
            args = str_message.split(" ")
            command = args[0]
            del args[0]

            # /dir c:\\test
            if command == "/dir":
                filepath = " ".join(args)
                if filepath.strip() == "":
                    bot.sendMessage(chat_id, "please input /dir [folder].")
                else:
                    filelist = module.get_dir_list(filepath)
                    bot.sendMessage(chat_id, filelist)
            elif command[0:4] == "/get":
                filepath = " ".join(args)
                if os.path.exists(filepath):
                    try:
                        if command == "/getfile":
                            bot.sendDocument(chat_id, open(filepath, "rb"))
                        elif command == "/getimage":
                            bot.sendPhoto(chat_id, open(filepath, "rb"))
                        elif command == "/getaudio":
                            bot.sendAudio(chat_id, open(filepath, "rb"))
                        elif command == "/getvideo":
                            bot.sendVideo(chat_id, open(filepath, "rb"))
                    except Exception as e:
                        bot.sendMessage(chat_id, "failed. {}".format(e))
                else:
                    bot.sendMessage(chat_id, "file doesn't exist.")
                

bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)