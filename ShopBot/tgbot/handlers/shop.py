from telebot import TeleBot
from telebot import types
from telebot.types import Message
from telebot.types import ReplyParameters
from tgbot.states.register_state import Register
from telebot.states.sync.context import StateContext
from tgbot.filters import select_menu_chapter


def open_menu(message: Message, bot: TeleBot):
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

    if "/" in message.text:
        bot.send_message(message.chat.id, text="menu:", reply_markup=keyboard)
    else:
        # Команды нельзя отредактировать (+бот может редактировать только свои собственные сообщения)
        bot.edit_message_text(text="menu:", chat_id=message.chat.id, message_id=message.message_id, reply_markup=keyboard)

def goto_menu(call: types.CallbackQuery, bot: TeleBot):
    open_menu(message=call.message, bot=bot)

def open_chapter(call: types.CallbackQuery, bot: TeleBot):
    callback_data: dict = select_menu_chapter.parse(callback_data=call.data)
    bot.edit_message_text(text=f"{callback_data['chapter']}:", chat_id=call.message.chat.id, message_id=call.message.id,)

    def load_chapter():
        chapter = callback_data['chapter']
        print(chapter)

        if chapter == 'catalog':
            goods_db = [{'id': '0', 'name': 'товар 0', 'description': 'лучший в мире товар', 'price': 100, 'image_path': 'file/xxx'},
                     {'id': '1', 'name': 'товар 1', 'description': 'лучший в мире товар', 'price': 111, 'image_path': 'file/xxx'},
                     {'id': '2', 'name': 'товар 2', 'description': 'лучший в мире товар', 'price': 222, 'image_path': 'file/xxx'},
                     {'id': '3', 'name': 'товар 3', 'description': 'лучший в мире товар', 'price': 333, 'image_path': 'file/xxx'},
                     {'id': '4', 'name': 'товар 4', 'description': 'лучший в мире товар', 'price': 444, 'image_path': 'file/xxx'},
                     {'id': '5', 'name': 'товар 5', 'description': 'лучший в мире товар', 'price': 555, 'image_path': 'file/xxx'},
                     {'id': '6', 'name': 'товар 6', 'description': 'лучший в мире товар', 'price': 666, 'image_path': 'file/xxx'},
                     {'id': '7', 'name': 'товар 7', 'description': 'лучший в мире товар', 'price': 777, 'image_path': 'file/xxx'},
                     {'id': '8', 'name': 'товар 8', 'description': 'лучший в мире товар', 'price': 888, 'image_path': 'file/xxx'},
                     {'id': '9', 'name': 'товар 9', 'description': 'лучший в мире товар', 'price': 999, 'image_path': 'file/xxx'},
                     {'id': '10', 'name': 'товар 10', 'description': 'лучший в мире товар', 'price': 1000, 'image_path': 'file/xxx'},
                     {'id': '11', 'name': 'товар 11', 'description': 'лучший в мире товар', 'price': 1111, 'image_path': 'file/xxx'},
                     {'id': '12', 'name': 'товар 12', 'description': 'лучший в мире товар', 'price': 1222, 'image_path': 'file/xxx'},
                     {'id': '13', 'name': 'товар 13', 'description': 'лучший в мире товар', 'price': 1333, 'image_path': 'file/xxx'},]

            def create_keyboard():
                keyboard = types.InlineKeyboardMarkup(row_width=5)
                keyboard.add(*[
                    types.InlineKeyboardButton(
                        text=f"{element['name']}",
                        callback_data='pass'
                    )
                    for element in goods_db
                ])
                back_button = types.InlineKeyboardButton(
                    text="back",
                    callback_data='goto_menu')
                previous_button = types.InlineKeyboardButton(
                    text="<",
                    callback_data='XXXXXXXXXX')
                next_button = types.InlineKeyboardButton(
                    text=">",
                    callback_data='XXXXXXXXXX')
                keyboard.row(previous_button, back_button, next_button)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=keyboard)

            create_keyboard()
        elif chapter == 'basket':
            pass

    load_chapter()