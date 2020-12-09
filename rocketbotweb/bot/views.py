import sys
import os

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

from config.auth import token
from config.settings import PORT, HEROKU_APP_NAME

from rocketbotweb.api.views import video

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
mode = os.getenv('MODE')

updater = Updater(token=token)
dispatcher = updater.dispatcher


def whoAmI(update, context):
    """
    This is a method used to describe the goal of this project
    :param update:
    :param context:
    :return: str
    """
    logger.info(f'User {update.effective_user.id} asked about who am i: {datetime.now()}')
    name = update.effective_user.first_name
    update.message.reply_text(f'Hi {name}, \n'
                              f'I am a bot created by Esteban to complete a technical test for a new position as '
                              f'fullstack engineer.')


def start(update, context):
    """
    method that activate the answer message handler
    :param update:
    :param context:
    :return: prompt
    """
    user_id = update.effective_user.id
    logger.info(f'User {user_id} want to start a conversation at: {datetime.now()}')
    update.message.reply_text(f'Would you help me find out in which frame the rocket takes off? write "/findTheFrame"')


def find_the_frame(update, context):
    """
    this method get the user's prompt to calculate which are the frame we are looking for
    :param update:
    :param context:
    :return:
    """
    user_id = update.effective_user.id
    user_reply = update.message.text
    chat_id = update.message.chat_id
    logger.info(f'User {user_id} answered: {user_reply}: {datetime.now()}')
    context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_photo(chat_id=chat_id,
                           photo=video)
    update.message.reply_text('Did the rocket launch yet?')


def main():
    bot = telegram.Bot(token=token)

    logger.info(f'\n Bot information: '
                f'\n    * id:{bot.id}'
                f'\n    * first_name:{bot.first_name}'
                f'\n    * username:{bot.username}')

    if mode == 'dev':
        def run(updater):
            updater.start_polling()
            updater.idle()
    elif mode == 'pro':
        def run(updater):
            updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=token)
            updater.bot.set_webhook(f'https://{HEROKU_APP_NAME}.herokuapp.com/{token}')
    else:
        logger.info(f'the env is not declared')
        sys.exit()

    dispatcher.add_handler(CommandHandler("whoAmI", whoAmI))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("findTheFrame", find_the_frame))

    run(updater)


if __name__ == '__main__':
    main()
