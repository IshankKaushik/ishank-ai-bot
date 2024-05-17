import os
from re import split
from telegram import Bot, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

""" Required """

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GOOGLE_API_KEY = split(r'[ ,;，；]+', os.environ.get("GOOGLE_API_KEY"))

""" Optional """

ALLOWED_USERS = split(r'[ ,;，；]+', os.getenv("ALLOWED_USERS", '').replace("@", "").lower())
ALLOWED_GROUPS = split(r'[ ,;，；]+', os.getenv("ALLOWED_GROUPS", '').replace("@", "").lower())

# Whether to push logs and enable some admin commands
IS_DEBUG_MODE = os.getenv("IS_DEBUG_MODE", '0')
# The target account that can execute administrator instructions and log push can use /get_my_info to obtain the ID.
ADMIN_ID = os.getenv("ADMIN_ID", "1234567890")

# Determines whether to verify identity. If 0, anyone can use the bot. It is enabled by default.
AUCH_ENABLE = os.getenv("AUCH_ENABLE", "1")

# "1" to use the same chat history in the group, "2" to record chat history individually for each person
GROUP_MODE = os.getenv("GROUP_MODE=", "1")

# After setting up 22 rounds of dialogue, prompt the user to start a new dialogue
prompt_new_threshold = int(22)

# The default prompt when the photo has no accompanying text
default_photo_caption = "describe this picture"

""" Below is some text related to the user """
help_text = "*Send Your Questions or Pictures to the Bot, and I will Provide Answers.*\n"
command_list = "_» created by @IshankKaushik ❤️_"
admin_auch_info = "You are not the Bot Admin, so you can't use this function!!!"
debug_mode_info = "Debug mode is not enabled!"
command_format_error_info = "Wrong command, use /help for help"
command_invalid_error_info = "Wrong command, use /help for help"
user_no_permission_info = "You are not allowed to use this bot 🫤"
group_no_permission_info = "This group does not have permission to use this robot ❌"
gemini_err_info = "Something went wrong!\nThe content you entered may be inappropriate, please modify it and try again"
new_chat_info = "We're starting a new chat."
prompt_new_info = "_type /new to start a new chat_"
unable_to_recognize_content_sent = "The content you sent is not currently supported yet 😬"

""" Below is some text related to the log """
send_message_log = "Send a message. The content returned is:"
send_photo_log = "Send a photo. The content returned is:"
unnamed_user = "UnnamedUser"
unnamed_group = "UnnamedGroup"
event_received = "event received"
group = "group"
the_content_sent_is = "The content sent is:"
the_reply_content_is = "The reply content is:"
the_accompanying_message_is = "The accompanying message is:"
the_logarithm_of_historical_conversations_is = "The logarithm of historical conversations is:"
no_rights_to_use = "No rights to use"
send_unrecognized_content = "Send unrecognized content"

""" read https://ai.google.dev/api/rest/v1/GenerationConfig """
generation_config = {
    "max_output_tokens": 1024,
}

""" read https://ai.google.dev/api/rest/v1/HarmCategory """
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

# Initialize the bot and updater
bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define a command handler for /start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=help_text,
        parse_mode=ParseMode.MARKDOWN
    )

# Define a message handler for regular messages
def handle_message(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Received your message!",
        parse_mode=ParseMode.MARKDOWN
    )

# Add handlers to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
