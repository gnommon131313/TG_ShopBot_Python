from telebot import TeleBot
from telebot import types
from telebot.types import Message
from telebot.types import ReplyParameters
from tgbot.states.register_state import Register
from telebot.states.sync.context import StateContext
from tgbot.filters import select_menu_chapter


def open_menu(message: Message, bot: TeleBot):
    bot.set_state(message.from_user.id, Register.menu, message.chat.id)

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        text="catalog",
        callback_data=select_menu_chapter.new(chapter='catalog')
    )
    button2 = types.InlineKeyboardButton(
        text="basket",
        callback_data=select_menu_chapter.new(chapter='basket')
    )
    keyboard.row(button1, button2)
    bot.send_message(message.chat.id, text="меню:", reply_markup=keyboard)

def open_chapter(call: types.CallbackQuery, bot: TeleBot):
    callback_data: dict = select_menu_chapter.parse(callback_data=call.data)
    bot.edit_message_text(text="chapter:", chat_id=call.message.chat.id, message_id=call.message.id,)

    def load_chapter():
        chapter = callback_data['chapter']

        if chapter == 'catalog':
            print(chapter)
        elif chapter == 'basket':
            print(chapter)

    def load_new_keyboard():
        new_keyboard = types.InlineKeyboardMarkup()
        new_button = types.InlineKeyboardButton(text=f"{callback_data['chapter']}", callback_data="some callback")
        new_keyboard.row(new_button)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=new_keyboard)

    load_chapter()
    load_new_keyboard()