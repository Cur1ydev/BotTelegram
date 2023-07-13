# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import telebot
from telebot import types

# from googletrans import Translator

# Khởi tạo bot
bot = telebot.TeleBot('6316189253:AAGuvkAH-xCU1zCwkQW8-akwCaHkCYIAjAQ')

user_language = {}


@bot.message_handler(commands=['start'])
def hander_start(message):
    bot.reply_to(message, f'Xin chào tôi là trợ lý ảo Robin,tôi có thể giúp gì cho bạn ?')


@bot.message_handler(commands=['help'])
def hander_help(message):
    bot.reply_to(message,
                 'Chào mừng bạn tới dự án Zororium, tôi là trợ lý ảo Robin, sẽ hướng dẫn bạn 🚀🚀🚀 \nNhấn /help để '
                 'xem hướng dẫn sử dụng autobot.\nNhấn /account để xem hướng dẫn cách tạo tài khoản và đăng nhập,'
                 'cách tạo ví metamask và các thông tin bổ sung đẻ giao dịch.\nNhấn /exchange để xem hướng dẫn cách '
                 'mua token, các công cụ thanh toán.\nNhấn /release để xem thông tin chi tiết về cách đợt phát hành '
                 'token và lộ trình niêm yết sàn Pancakeswap, Uniswap, Huobi & Binance.\nNhấn /gift để xem thông tin '
                 'về các chương trình quà tặng, khuyến mãi cho người dùng.\nNhấn /map để xem roadmap của dự án và '
                 'sitemap của hệ thống Zororium.\nNhấn /ib để xem chính sách cho nhà môi giới, phân biệt các cấp độ '
                 'môi giới và cách trả hoa hồng.\nNhấn /language để chọn ngôn ngữ English hoặc Vietnamse.')


@bot.message_handler(commands=['language'])
def handle_language_command(message):
    keyboard = types.InlineKeyboardMarkup()
    button_vietnamese = types.InlineKeyboardButton(text="Tiếng Việt", callback_data='vietnamese')
    button_english = types.InlineKeyboardButton(text="English", callback_data='english')
    keyboard.row(button_vietnamese, button_english)
    bot.send_message(message.chat.id, 'Chọn ngôn ngữ', reply_markup=keyboard)


@bot.message_handler(commands=['account'])
def handle_language_command(message):
    keyboard = types.InlineKeyboardMarkup()
    button_register = types.InlineKeyboardButton(text="Đăng ký tài khoản", callback_data='register')
    button_login = types.InlineKeyboardButton(text="Đăng nhập tài khoản", callback_data='login')
    button_kyc = types.InlineKeyboardButton(text="Xác thực tài khoản", callback_data='kyc')
    button_security = types.InlineKeyboardButton(text="Bảo mật 2 lớp tài khoản", callback_data='security')
    keyboard.row(button_register, button_login, button_kyc, button_security)
    bot.send_message(message.chat.id, 'Đăng ký , Đăng nhập', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_language_selection(call):
    chat_id = call.message.chat.id
    language = call.data

    # Lưu ngôn ngữ người dùng đã chọn
    user_language[chat_id] = language
    print(user_language)
    # Xóa tin nhắn gốc
    bot.delete_message(chat_id, call.message.message_id)


# Xử lý tin nhắn văn bản
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    # Kiểm tra xem người dùng đã chọn ngôn ngữ hay chưa
    if chat_id in user_language:
        language = user_language[chat_id]
        if language == 'vietnamese':
            # Xử lý tin nhắn bằng tiếng Việt
            # ...
            bot.send_message(chat_id, 'Xin chào! Bạn đã chọn ngôn ngữ Tiếng Việt.')
        elif language == 'english':
            # Xử lý tin nhắn bằng tiếng Anh
            # ...
            bot.send_message(chat_id, 'Hello! You have chosen English as your language.')
    else:
        # Gửi tin nhắn nhắc nhở người dùng chọn ngôn ngữ trước
        bot.send_message(chat_id, 'Vui lòng chọn ngôn ngữ trước bằng cách sử dụng /language.')


@bot.message_handler(commands=['test'])
def handle_test(msg):
    chat_id = msg.chat.id
    bot.reply_to(msg, f" {msg.date}")


@bot.message_handler(func=lambda mesage: True)
def hander_message(message):
    bot.reply_to(message, 'Bạn đã nói: ' + message.text)


bot.polling()
