from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تعریف دستور start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من یک ربات تلگرام هستم.')

# تعریف دستور echo که پیامی که کاربر می‌فرستد را برمی‌گرداند
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # توکن ربات خود را وارد کنید
    token = 'YOUR_BOT_TOKEN'  # جایگزین کنید با توکن واقعی ربات

    # ایجاد یک Updater برای ارتباط با سرور تلگرام
    updater = Updater(token)

    # دسترسی به دیسپاچر برای افزودن هندلرها
    dispatcher = updater.dispatcher

    # افزودن هندلر برای دستور start
    dispatcher.add_handler(CommandHandler("start", start))

    # افزودن هندلر برای پیام‌ها
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع ربات
    updater.start_polling()

    # ربات را تا وقتی که به صورت دستی متوقف نشود اجرا می‌کند
    updater.idle()

if __name__ == '__main__':
    main()
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تعریف دستور start
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.username if user.username else "کاربر ناشناس"
    update.message.reply_text(f'سلام! من یک ربات تلگرام هستم.\nیوزرنیم شما: {username}')

    # ایجاد دکمه برای وصلی کردن
    keyboard = [
        [InlineKeyboardButton("وصلم کن!", callback_data='connect_user')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("اگر می‌خواهید به مخاطب خاصم وصل شوید:", reply_markup=reply_markup)

# تعریف دستور echo که پیامی که کاربر می‌فرستد را برمی‌گرداند
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# هندلر برای دکمه "وصلم کن!"
def connect_user(update: Update, context: CallbackContext) -> None:
    update.callback_query.answer()
    update.callback_query.message.reply_text("شما اکنون به مخاطب خاص وصل شدید!")

def main():
    token = 'YOUR_BOT_TOKEN'  # جایگزین کنید با توکن واقعی ربات

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # افزودن هندلر برای دستور start
    dispatcher.add_handler(CommandHandler("start", start))

    # افزودن هندلر برای پیام‌ها
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # افزودن هندلر برای دکمه "وصلم کن!"
    dispatcher.add_handler(CallbackQueryHandler(connect_user, pattern='connect_user'))

    # شروع ربات
    updater.start_polling()

    # ربات را تا وقتی که به صورت دستی متوقف نشود اجرا می‌کند
    updater.idle()

if __name__ == '__main__':
    main()
