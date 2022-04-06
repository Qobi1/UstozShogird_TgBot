
from telegram.ext import CommandHandler, MessageHandler, Updater, CallbackContext, Filters, CallbackQueryHandler

from TOKEN import TOKEN
from classes import *


def btns(type=None):
    btn = []
    if type == "BoshMenu":
        btn = [
            [KeyboardButton("Bosh menuga qaytish")]
        ]
    else:
        btn = [
            [KeyboardButton("Sherik kerak"), KeyboardButton("Ish joyi kerak")],
            [KeyboardButton("Ustoz kerak"), KeyboardButton("Hodim kerak")],
            [KeyboardButton("Shogird kerak")]
        ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True, one_time_keyboard=True)


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    clear_log(user.id, 0)
    log = get_log(user.id)
    if log is None:
        log = create_log(user.id)
    log = ast.literal_eval(log[3])
    log['state'] = 1

    update.message.reply_text(f"""Assalom alaykum {user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=btns())

    update_log(user.id, log)


def help(update: Update, context: CallbackContext):
    pass


def received_msg(update: Update, context: CallbackContext):
    msg = update.message.text
    user = update.message.from_user
    log = get_log(user.id)
    log = ast.literal_eval(log[3])

    sherik_kerak = SherikKerak(user)
    ish_kerak = IshJoyiKerak(user)
    ustoz_kerak = UstozKerak(user)
    hodim_kerak = HodimKerak(user)
    shogird_kerak = ShogirdKerak(user)

    menu = get_log(user.id)[1]
    if menu == 0:
        if msg == "Sherik kerak":
            menu = 1
        elif msg == "Ish joyi kerak":
            menu = 2
        elif msg == "Ustoz kerak":
            menu = 3
        elif msg == "Hodim kerak":
            menu = 4
        elif msg == "Shogird kerak":
            menu = 5

        else:
            update.message.reply_text("Menudan brini tanlang!")
        update_menu(user.id, menu)

    if menu == 1:
        sherik_kerak.received_message(update, context)
    elif menu == 2:
        ish_kerak.received_message(update, context)
    elif menu == 3:
        ustoz_kerak.received_message(update, context)
    elif menu == 4:
        hodim_kerak.received_message(update, context)
    elif menu == 5:
        shogird_kerak.received_message(update, context)


def contact(update: Update, context: CallbackContext):
        user = update.message.from_user
        contact = update.message.contact
        log = get_log(user.id)
        log = ast.literal_eval(log[3])
        state = log.get('state', 0)
        if state == 4:
            log['aloqa'] = contact.phone_number
            log['state'] = 5
            update.message.reply_text(location, reply_markup=ReplyKeyboardRemove())
        elif state == 5:
            log['aloqa'] = contact.phone_number
            log['state'] = 6
            update.message.reply_text(location, reply_markup=ReplyKeyboardRemove())

        update_log(user.id, log)


def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, received_msg))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
