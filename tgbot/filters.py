import telebot
from telebot import types, SimpleCustomFilter, AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter
from tgbot.models.users_model import Admin


select_menu_chapter = CallbackData("chapter", prefix="some_prefix")


class AdminFilter(SimpleCustomFilter):
    key = 'admin'

    def check(self, message):
        # return int(message.chat.id) == int(Admin.ADMIN.value)
        return message.from_user.id in Admin.ADMIN.value


class CallbackFilter(AdvancedCustomFilter):
    key = 'callback_config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


def bind_filters(bot: telebot.TeleBot):
    bot.add_custom_filter(AdminFilter())
    bot.add_custom_filter(CallbackFilter())