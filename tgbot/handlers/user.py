from telebot import TeleBot
from telebot.types import Message
from telebot.types import ReplyParameters
from tgbot.states.register_state import Register
from telebot.states.sync.context import StateContext


def cancel(message: Message, bot: TeleBot):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, text="Ваша информация была очищена")
    bot.send_message(message.chat.id, text="/start чтобы начать снова")

def start_of_ordering(message: Message, bot: TeleBot):
    print(bot.get_state(message.from_user.id))
    bot.set_state(message.from_user.id, Register.user_name, message.chat.id)
    print(bot.get_state(message.from_user.id))

    bot.send_message(message.chat.id, text=f"Перед оформлением заказ укажите свои данные данные:\nУкажите имя")

def name_get(message: Message, bot: TeleBot):
    print(f"{bot.get_state(message.from_user.id)}")

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text

    bot.set_state(message.from_user.id, Register.user_phone, message.chat.id)

    bot.send_message(message.chat.id, text="Укажите номер телефона")

def phone_get(message: Message, bot: TeleBot):
    print(f"{bot.get_state(message.from_user.id)}")

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.text

    bot.set_state(message.from_user.id, Register.user_address, message.chat.id)

    bot.send_message(message.chat.id, text="Укажите адрес")

def address_get(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, text="Заказ успешно оформлен!")
    bot.delete_state(message.from_user.id, message.chat.id)