import os
from re import split
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

""" Required """
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GOOGLE_API_KEY = split(r'[ ,;，；]+', os.environ.get("GOOGLE_API_KEY"))

""" Optional """
ALLOWED_USERS = split(r'[ ,;，；]+', os.getenv("ALLOWED_USERS", '').replace("@", "").lower())
ALLOWED_GROUPS = split(r'[ ,;，；]+', os.getenv("ALLOWED_GROUPS", '').replace("@", "").lower())

IS_DEBUG_MODE = os.getenv("IS_DEBUG_MODE", '0')
ADMIN_ID = os.getenv("ADMIN_ID", "1234567890")
AUCH_ENABLE = os.getenv("AUCH_ENABLE", "1")
GROUP_MODE = os.getenv("GROUP_MODE=", "1")

prompt_new_threshold = int(22)
defaut_photo_caption = "describe this picture"

""" Below is some text related to the user """
help_text = "**Send Your Questions or Pictures to the Bot, and I will Provide Answers.**\n"
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

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(help_text + command_list, parse_mode=ParseMode.MARKDOWN)

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(help_text + command_list, parse_mode=ParseMode.MARKDOWN)

def main() -> None:
    """Start the bot."""
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
