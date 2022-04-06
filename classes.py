from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import ast

# from main import user
from text import *
from services import *
CHAT_ID = 895126630
CHANNEL_ID = '@teeessttttt_1'
# CHANNEL_ID = 2131718293


class SherikKerak:
    def __init__(self, user):
        self.user = user
        global m_user
        m_user = user

    def received_message(self, update: Update, context: CallbackContext):
        msg = update.message.text
        log = get_log(self.user.id)
        menu = log[1]
        log = ast.literal_eval(log[3])
        state = log.get('state', 0)
        if state == 1:
            log['Asosiy'] = msg
            log['state'] = 2
            update.message.reply_text(sherik_ariza)
            update.message.reply_text("Ism, familiyangizni kiriting?")
        elif state == 2:
            log['state'] = 3
            log['ism_familya'] = msg
            update.message.reply_text(technology)

        elif state == 3:
            log['state'] = 4
            log['texnolgiya'] = msg
            update.message.reply_text(phone_number, reply_markup=buttons())

        elif state == 4:
            log['state'] = 5
            log['aloqa'] = msg
            update.message.reply_text(location, reply_markup=ReplyKeyboardRemove())
        elif state == 5:
            log['state'] = 6
            log['hudud'] = msg
            update.message.reply_text(price)
        elif state == 6:
            log['state'] = 7
            log['narxi'] = msg
            update.message.reply_text(job)

        elif state == 7:
            log['state'] = 8
            log['kasbi'] = msg
            update.message.reply_text(allowed_time)
        elif state == 8:
            log['state'] = 9
            log['murojat_voqti'] = msg
            update.message.reply_text(purpose)
        elif state == 9:
            log['state'] = 10
            log['maqsad'] = msg

            update_log(self.user.id, log)

            update.message.reply_text(final_result(menu=1))
            update.message.reply_text("Barcha malumotlar to'g'rimi", reply_markup=buttons("ha_yoq"))

        elif state == 10:
            if msg == "Ha":
                context.bot.send_message(chat_id=CHAT_ID, text=final_result(menu), reply_markup=buttons(type="for_inline"))
                update.message.reply_text("So'rovingiz muvofaqiyatli yuborildi", reply_markup=ReplyKeyboardRemove())
            elif msg == "Yo'q":
                update.message.reply_text("Qabul qlinmadi", reply_markup=ReplyKeyboardRemove())
                update.message.reply_text(f"""Assalom alaykum {self.user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=buttons(type="bosh_menu"))
            else:
                update.message.reply_text("Ha yoki Yo'q ni tanlang")

        update_log(self.user.id, log)


class IshJoyiKerak:
    def __init__(self, user):
        self.user = user
        global m_user
        m_user = user

    def received_message(self, update: Update, context: CallbackContext):

        msg = update.message.text
        log = get_log(self.user.id)
        log = ast.literal_eval(log[3])
        state = log.get('state', 0)
        if state == 1:
            log['state'] = 2
            log['Asosiy'] = msg
            update.message.reply_text(IshJoyiKerak_ariza)
            update.message.reply_text("Ism, familiyangizni kiriting?")
        elif state == 2:
            log['state'] = 3
            log['ism_familya'] = msg
            update.message.reply_text(age)
        elif state == 3:
            log['state'] = 4
            log['yosh'] = msg
            update.message.reply_text(technology)
        elif state == 4:
            log['state'] = 5
            log['texnolgiya'] = msg
            update.message.reply_text(phone_number, reply_markup=buttons())
        elif state == 5:
            log['state'] = 6
            log['aloqa'] = msg
            update.message.reply_text(location, reply_markup=ReplyKeyboardRemove())
        elif state == 6:
            log['state'] = 7
            log['hudud'] = msg
            update.message.reply_text(price)
        elif state == 7:
            log['state'] = 8
            log['narxi'] = msg
            update.message.reply_text(job)
        elif state == 8:
            log['state'] = 9
            log['kasbi'] = msg
            update.message.reply_text(allowed_time)
        elif state == 9:
            log['state'] = 10
            log['murojat_voqti'] = msg
            update.message.reply_text(purpose)
        elif state == 10:
            log['state'] = 11
            log['maqsad'] = msg
            update_log(self.user.id, log)

            update.message.reply_text(final_result(menu=2))
            update.message.reply_text("Barcha malumotlar to'g'rimi", reply_markup=buttons("ha_yoq"))
        elif state == 11:
            if msg == 'Ha':
                context.bot.send_message(chat_id=CHAT_ID, text=final_result(menu=2), reply_markup=buttons(type='for_inline'))
                update.message.reply_text("So'rovingiz muvofaqtiyatli yuborildi", reply_markup=ReplyKeyboardRemove())
            elif msg == 'Yo\'q':
                update.message.reply_text('Qabul qlinmadi', reply_markup=ReplyKeyboardRemove())
                update.message.reply_text(f"""Assalom alaykum {self.user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""",  reply_markup=buttons(type="bosh_menu"))
            else:
                update.message.reply_text('Ha yoki Yo\'q ni tanlang')
        update_log(self.user.id, log)


class UstozKerak:
    def __init__(self, user):
        self.user = user
        global m_user
        m_user = user

    def received_message(self, update: Update, context: CallbackContext):
        msg = update.message.text
        log = get_log(self.user.id)
        log = ast.literal_eval(log[3])
        state = log.get('state', 0)

        if state == 1:
            log['state'] = 2
            log['Asosiy'] = msg
            update.message.reply_text(UstozKerak_ariza)
            update.message.reply_text("Ism, familiyangizni kiriting?")
        elif state == 2:
            log['state'] = 3
            log['ism_familya'] = msg
            update.message.reply_text(age)
        elif state == 3:
            log['state'] = 4
            log['yosh'] = msg
            update.message.reply_text(technology)
        elif state == 4:
            log['state'] = 5
            log['texnolgiya'] = msg
            update.message.reply_text(phone_number, reply_markup=buttons())
        elif state == 5:
            log['state'] = 6
            log['aloqa'] = msg
            update.message.reply_text(location, reply_markup=ReplyKeyboardRemove())
        elif state == 6:
            log['state'] = 7
            log['hudud'] = msg
            update.message.reply_text(price)
        elif state == 7:
            log['state'] = 8
            log['narxi'] = msg
            update.message.reply_text(job)
        elif state == 8:
            log['state'] = 9
            log['kasbi'] = msg
            update.message.reply_text(allowed_time)
        elif state == 9:
            log['state'] = 10
            log['murojat_voqti'] = msg
            update.message.reply_text(purpose)
        elif state == 10:
            log['state'] = 11
            log['maqsad'] = msg
            update_log(self.user.id, log)

            update.message.reply_text(final_result(menu=3))
            update.message.reply_text("Barcha malumotlar to'g'rimi", reply_markup=buttons("ha_yoq"))


        elif state == 11:
            if msg == 'Ha':
                context.bot.send_message(chat_id=CHAT_ID, text=final_result(menu=3), reply_markup=buttons('for_inline'))
                update.message.reply_text("So'rovingiz muvofaqtiyatli yuborildi", reply_markup=ReplyKeyboardRemove())
            elif msg == "Yo'q":
                update.message.reply_text("Qabul qlinmadi", reply_markup=ReplyKeyboardRemove())
                update.message.reply_text(f"""Assalom alaykum {self.user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=buttons(type="bosh_menu"))
            else:
                update.message.reply_text("Ha yoki Yo\'q ni tanlang")

        update_log(self.user.id, log)


class HodimKerak:
    def __init__(self, user):
        self.user = user
        global m_user
        m_user = user

    def received_message(self, update: Update, context: CallbackContext):
        msg = update.message.text
        log = get_log(self.user.id)
        log = ast.literal_eval(log[3])
        state = log.get('state', 0)
        if state == 1:
            log['state'] = 2
            log['Asosiy'] = msg
            update.message.reply_text(HodimKerak_ariza)
            update.message.reply_text("🎓 Idora nomi?")
        elif state == 2:
            log['state'] = 3
            log['idora'] = msg
            update.message.reply_text(technology)
        elif state == 3:
            log['state'] = 4
            log['texnolgiya'] = msg
            update.message.reply_text(phone_number)
        elif state == 4:
            log['state'] = 5
            log['aloqa'] = msg
            update.message.reply_text(location)
        elif state == 5:
            log['state'] = 6
            log['hudud'] = msg
            update.message.reply_text("✍️Mas'ul ism sharifi?")
        elif state == 6:
            log['state'] = 7
            log['masul_shaxs'] = msg
            update.message.reply_text(allowed_time)
        elif state == 7:
            log['state'] = 8
            log['murojat_voqti'] = msg
            update.message.reply_text("🕰 Ish vaqtini kiriting?")
        elif state == 8:
            log['state'] = 9
            log['ish_voqti'] = msg
            update.message.reply_text("💰 Maoshni kiriting?")
        elif state == 9:
            log['state'] = 10
            log['maosh'] = msg
            update.message.reply_text("‼️ Qo`shimcha ma`lumotlar?")
        elif state == 10:
            log['state'] = 11
            log['malumot'] = msg
            update_log(self.user.id, log)
            update.message.reply_text(final_result(menu=4))
            update.message.reply_text("Barcha malumotlar to'g'rimi", reply_markup=buttons(type="ha_yoq"))
        elif state == 11:
            if msg == 'Ha':
                context.bot.send_message(chat_id=CHAT_ID, text=final_result(menu=4), reply_markup=buttons('for_inline'))
                update.message.reply_text("So'rovingiz muvofaqtiyatli yuborildi", reply_markup=ReplyKeyboardRemove())
            elif msg == "Yo'q":
                update.message.reply_text("Qabul qlinmadi", reply_markup=ReplyKeyboardRemove())
                update.message.reply_text(f"""Assalom alaykum {self.user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=buttons(type="bosh_menu"))
            else:
                update.message.reply_text("Ha yoki Yo\'q ni tanlang")

        update_log(self.user.id, log)


class ShogirdKerak:
    def __init__(self, user):
        self.user = user
        global m_user
        m_user = user

    def received_message(self, update: Update, context: CallbackContext):
        msg = update.message.text
        log = get_log(self.user.id)
        log = ast.literal_eval(log[3])
        state = log.get('state', 0)
        if state == 1:
            log['state'] = 2
            log['Asosiy'] = msg
            update.message.reply_text(ShogirdKerak_ariza)
            update.message.reply_text("Ism, familiyangizni kiriting?")
        elif state == 2:
            log['state'] = 3
            log['ism_familya'] = msg
            update.message.reply_text(age)
        elif state == 3:
            log['state'] = 4
            log['yosh'] = msg
            update.message.reply_text(technology)
        elif state == 4:
            log['state'] = 5
            log['texnolgiya'] = msg
            update.message.reply_text(phone_number)
        elif state == 5:
            log['state'] = 6
            log['aloqa'] = msg
            update.message.reply_text(location)
        elif state == 6:
            log['state'] = 7
            log['hudud'] = msg
            update.message.reply_text(price)
        elif state == 7:
            log['state'] = 8
            log['narxi'] = msg
            update.message.reply_text(job)
        elif state == 8:
            log['state'] = 9
            log['kasbi'] = msg
            update.message.reply_text(allowed_time)
        elif state == 9:
            log['state'] = 10
            log['murojat_voqti'] = msg
            update.message.reply_text(purpose)
        elif state == 10:
            log['state'] = 11
            log['maqsad'] = msg
            update_log(self.user.id, log)

            update.message.reply_text(final_result(menu=5))
            update.message.reply_text("Barcha malumotlar to'grimi", reply_markup=buttons(type='ha_yoq'))
        elif state == 11:
            if msg == 'Ha':
                context.bot.send_message(chat_id=CHAT_ID, text=final_result(menu=5), reply_markup=buttons('for_inline'))
                update.message.reply_text("So'rovingiz muvofaqtiyatli yuborildi", reply_markup=ReplyKeyboardRemove())
            elif msg == "Yo'q":
                update.message.reply_text("Qabul qlinmadi", reply_markup=ReplyKeyboardRemove())
                update.message.reply_text(f"""Assalom alaykum {self.user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=buttons(type="bosh_menu"))
            else:
                update.message.reply_text("Ha yoki Yo\'q ni tanlang")
            update_log(self.user.id, log)

        update_log(self.user.id, log)


def buttons(type=None):
    if type == "ha_yoq":
        btn = [[KeyboardButton("Ha"), KeyboardButton("Yo'q")]]
    elif type == "for_inline":
        btn = [[InlineKeyboardButton("Ha", callback_data=f'ha'), InlineKeyboardButton("Yo'q", callback_data=f'yoq')]]
        return InlineKeyboardMarkup(btn)
    elif type == 'bosh_menu':
        btn = [
            [KeyboardButton("Sherik kerak"), KeyboardButton("Ish joyi kerak")],
            [KeyboardButton("Ustoz kerak"), KeyboardButton("Hodim kerak")],
            [KeyboardButton("Shogird kerak")]
        ]
    else:
        btn = [[KeyboardButton("Raqamni kritish", request_contact=True)]]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def inline_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    admin = query.from_user
    log = get_log(m_user.id)
    menu = log[1]
    if data == f'ha':
        context.bot.send_message(chat_id=CHANNEL_ID, text=final_result(menu))
        context.bot.delete_message(message_id=query.message.message_id, chat_id=admin.id)
        query.message.reply_text("Kanalga yuborildi")

    elif data == f'yoq':
        query.message.reply_text("So'rov rad etildi")
        context.bot.delete_message(message_id=query.message.message_id, chat_id=admin.id)


def final_result(menu=None):
    log = get_log(m_user.id)
    log = ast.literal_eval(log[3])

    result = ''

    aloqa = log['aloqa']
    telegram = m_user.username
    if telegram is None:
        telegram = log['aloqa']

    if menu == 1:
        asosiy = log['Asosiy']
        ism = log['ism_familya']
        texnologiya = log['texnolgiya']
        hudud = log['hudud']
        narx = log['narxi']
        kasbi = log['kasbi']
        murojat_voqti = log['murojat_voqti']
        maqsad = log['maqsad']

        result = f"""{asosiy}:
        
🏅 Sherik: {ism}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: {telegram} 
📞 Aloqa: {aloqa}
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasbi} 
🕰 Murojaat qilish vaqti: {murojat_voqti} 
🔎 Maqsad: {maqsad} 

#sherik"""

    elif menu == 2:
        asosiy = log['Asosiy']
        ism = log['ism_familya']
        yosh = log['yosh']
        texnologiya = log['texnolgiya']
        aloqa = log['aloqa']
        hudud = log['hudud']
        narx = log['narxi']
        kasbi = log['kasbi']
        murojat_voqti = log['murojat_voqti']
        maqsad = log['maqsad']

        result = f"""{asosiy}:
        
👨‍💼 Xodim: {ism}
🕑 Yosh: {yosh}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: {telegram} 
📞 Aloqa: {aloqa}
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasbi} 
🕰 Murojaat qilish vaqti: {murojat_voqti} 
🔎 Maqsad: {maqsad} 

#xodim"""

    elif menu == 3:
        asosiy = log['Asosiy']
        ism = log['ism_familya']
        yosh = log['yosh']
        texnologiya = log['texnolgiya']
        hudud = log['hudud']
        narx = log['narxi']
        kasbi = log['kasbi']
        murojat_voqti = log['murojat_voqti']
        maqsad = log['maqsad']

        result = f"""{asosiy}:

🎓 Shogird: {ism}
🌐 Yosh: {yosh}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: {telegram}
📞 Aloqa: {aloqa}
🌐 Hudud: {hudud}
💰 Narxi: {narx}
👨🏻‍💻 Kasbi: {kasbi}
🕰 Murojaat qilish vaqti: {murojat_voqti} 
🔎 Maqsad: {maqsad} 

#shogird
"""
    elif menu == 4:
        asosiy = log['Asosiy']
        idora = log['idora']
        texnologiya = log['texnolgiya']
        hudud = log['hudud']
        masul_shaxs = log['masul_shaxs']
        murojat_voqti = log['murojat_voqti']
        ish_voqti = log['ish_voqti']
        maosh = log['maosh']
        malumot = log['malumot']

        result = f"""{asosiy}:

🏢 Idora: {idora}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: {telegram} 
📞 Aloqa: {aloqa} 
🌐 Hudud: {hudud}
✍ Mas'ul: {masul_shaxs}
🕰 Murojaat vaqti: {murojat_voqti} 
🕰 Ish vaqti: {ish_voqti} 
💰 Maosh: {maosh}
‼️ Qo`shimcha: {malumot}

#ishJoyi"""

    elif menu == 5:
        asosiy = log['Asosiy']
        ism = log['ism_familya']
        yosh = log['yosh']
        texnologiya = log['texnolgiya']
        hudud = log['hudud']
        narx = log['narxi']
        kasbi = log['kasbi']
        murojat_voqti = log['murojat_voqti']
        maqsad = log['maqsad']

        result = f"""{asosiy}:

🎓 Ustoz: {ism}
🌐 Yosh: {yosh}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: {telegram}
📞 Aloqa: {aloqa} 
🌐 Hudud: {hudud}
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasbi}
🕰 Murojaat qilish vaqti: {murojat_voqti} 
🔎 Maqsad: {maqsad} 

#shogird"""


    return result

