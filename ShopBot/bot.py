from telebot import types
from telebot.types import Message, CallbackQuery

# filters
from tgbot.filters import (bind_filters, select_menu_chapter)

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.shop import open_menu, goto_menu, open_chapter
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import (cancel as user_cancel,
                                start_of_ordering, name_get as user_name_get,
                                phone_get as user_phone_get,
                                address_get as user_address_get,)

# middlewares
from telebot import apihelper
from tgbot.middlewares.antiflood_middleware import antispam_func

# states
from telebot.storage import StateMemoryStorage
from tgbot.states.register_state import Register

# utils
from tgbot.utils.database import Database

# config
from tgbot import config

# Bot initialize
from telebot import TeleBot
state_storage = StateMemoryStorage()  # ! Don't use this in production; switch to redis
apihelper.ENABLE_MIDDLEWARE = True  # Для возможности регистрации middleware (делать перед созданием бота)
bot = TeleBot(config.TOKEN, state_storage=state_storage, num_threads=5)
db = Database()


def register_handlers():
    bot.register_message_handler(admin_user, commands=['debug'], admin=True, pass_bot=True)

    bot.register_message_handler(open_menu, commands=['start'], pass_bot=True)
    bot.register_callback_query_handler(goto_menu, func=lambda call: call.data == 'goto_menu', pass_bot=True)
    bot.register_callback_query_handler(open_chapter, func=None,
                                        callback_config=select_menu_chapter.filter(), pass_bot=True)

    bot.register_message_handler(user_cancel, commands=['cancel'], admin=False, pass_bot=True)
    bot.register_message_handler(start_of_ordering, commands=['order'], admin=False, pass_bot=True)
    bot.register_message_handler(start_of_ordering,
                                 func=lambda message: bot.get_state(message.from_user.id) == Register.start_of_order.name,
                                 admin=False, pass_bot=True)
    bot.register_message_handler(user_name_get,
                                 func=lambda message: bot.get_state(message.from_user.id) == Register.user_name.name,
                                 admin=False, pass_bot=True)
    bot.register_message_handler(user_phone_get,
                                 func=lambda message: bot.get_state(message.from_user.id) == Register.user_phone.name,
                                 admin=False, pass_bot=True)
    bot.register_message_handler(user_address_get,
                                 func=lambda message: bot.get_state(message.from_user.id) == Register.user_address.name,
                                 admin=False, pass_bot=True)

    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)

    @bot.message_handler(func=lambda message: True)
    def general_handler(message: Message):
        print(f"\ngeneral text = {message.text}")

register_handlers()

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=['message'])

# custom filters
bind_filters(bot)

def run():
    bot.infinity_polling()

run()