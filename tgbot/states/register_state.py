from telebot.handler_backends import State, StatesGroup


class Register(StatesGroup):
    menu = State()
    catalog = State()
    basket = State()
    product_card = State()
    start_of_order = State()
    user_name = State()
    user_phone = State()
    user_address = State()