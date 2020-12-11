from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
import logging
import os

PORT = int(os.environ.get('PORT', 5000))

from states import *
from text import *
from callback import *
from configimp import *

i = 0

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [InlineKeyboardButton(Language[1], callback_data=str(kaz))],
        [InlineKeyboardButton(Language[0], callback_data=str(rus))],
        [InlineKeyboardButton(Language[2], callback_data=str(eng))],
        [InlineKeyboardButton(Language[3], callback_data=str(kor))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(
        select_language[2],
        reply_markup=reply_markup
    )
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def start_over(update, context):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Language[1], callback_data=str(kaz))],
        [InlineKeyboardButton(Language[0], callback_data=str(rus))],
        [InlineKeyboardButton(Language[2], callback_data=str(eng))],
        [InlineKeyboardButton(Language[3], callback_data=str(kor))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(
        text=select_language[i] + ":",
        reply_markup=reply_markup
    )
    return FIRST


def main_menu(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Press_center[i], url=press_link[i])],
        [InlineKeyboardButton(About_Kazakhstan[i], callback_data=str(about_kz))],
        [InlineKeyboardButton(Embassy_address[i], callback_data=str(caddress))],
        [InlineKeyboardButton(Work_schedule[i], callback_data=str(schedule))],
        [InlineKeyboardButton(Appointment[i], callback_data=str(registration))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return MENU_MAIN


def rus_main(update, context):
    global i
    i = 0
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Press_center[i], url=press_link[i])],
        [InlineKeyboardButton(About_Kazakhstan[i], callback_data=str(about_kz))],
        [InlineKeyboardButton(Embassy_address[i], callback_data=str(caddress))],
        [InlineKeyboardButton(Work_schedule[i], callback_data=str(schedule))],
        [InlineKeyboardButton(Appointment[i], callback_data=str(registration))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return MENU_MAIN


'''Отдел запись на прием здесь'''


def menu_reg(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(menu_select[i], callback_data=str(menu)),
         InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=reg[i],
        reply_markup=reply_markup
    )
    return MENU_CADRESS


'''CONSUL ADRESS HERE'''


def menu_caddress(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Adress_how[i], callback_data=str(addressroute))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language)),
         InlineKeyboardButton(menu_select[i], callback_data=str(menu))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=Adress[i],
        reply_markup=reply_markup
    )
    return MENU_CADRESS


'''HOW TO GET THERE(LINKS)'''


def menu_addressroute(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Google_m, url=google)],
        [InlineKeyboardButton(Kakao_m, url=kakao)],
        [InlineKeyboardButton(Naver_m, url=naver)],
        [InlineKeyboardButton(menu_select[i], callback_data=str(menu)),
         InlineKeyboardButton(Back[i], callback_data=str(caddress))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=Adress_route[i],
        reply_markup=reply_markup
    )
    return MENU_ROUTE


def menu_schedule(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(select_language2[i], callback_data=str(language)),
         InlineKeyboardButton(Back[i], callback_data=str(menu))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=Working_schedule_text[i],
        reply_markup=reply_markup
    )
    return MENU_MAIN


def kaz_main(update, context):
    global i
    i = 1
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Press_center[i], url=press_link[i])],
        [InlineKeyboardButton(About_Kazakhstan[i], callback_data=str(about_kz))],
        [InlineKeyboardButton(Embassy_address[i], callback_data=str(caddress))],
        [InlineKeyboardButton(Work_schedule[i], callback_data=str(schedule))],
        [InlineKeyboardButton(Appointment[i], callback_data=str(registration))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return MENU_MAIN


def eng_main(update, context):
    global i
    i = 2
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Press_center[i], url=press_link[i])],
        [InlineKeyboardButton(About_Kazakhstan[i], callback_data=str(about_kz))],
        [InlineKeyboardButton(Embassy_address[i], callback_data=str(caddress))],
        [InlineKeyboardButton(Work_schedule[i], callback_data=str(schedule))],
        [InlineKeyboardButton(Appointment[i], callback_data=str(registration))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return ENG_KOR


def ke_main(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Press_center[i], url=press_link[i])],
        [InlineKeyboardButton(About_Kazakhstan[i], callback_data=str(about_kz))],
        [InlineKeyboardButton(Embassy_address[i], callback_data=str(caddress))],
        [InlineKeyboardButton(Work_schedule[i], callback_data=str(schedule))],
        [InlineKeyboardButton(Appointment[i], callback_data=str(registration))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return ENG_KOR


def kor_main(update, context):
    global i
    i = 3
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(Press_center[i], url=press_link[i])],
        [InlineKeyboardButton(About_Kazakhstan[i], callback_data=str(about_kz))],
        [InlineKeyboardButton(Embassy_address[i], callback_data=str(caddress))],
        [InlineKeyboardButton(Work_schedule[i], callback_data=str(schedule))],
        [InlineKeyboardButton(Appointment[i], callback_data=str(registration))],
        [InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return ENG_KOR

def menu_about_kz(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(About_Abai[i], url=Abai_link[i])],
        [InlineKeyboardButton(About_AlFarabi[i], url=AlFarabi_link[i])],
        [InlineKeyboardButton(menu_select[i], callback_data=str(menu)),
        InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return MENU_MAIN

def kek_about_kz(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton(About_Abai[i], url=Abai_link[i])],
        [InlineKeyboardButton(About_AlFarabi[i], url=AlFarabi_link[i])],
        [InlineKeyboardButton(menu_select[i], callback_data=str(menu)),
        InlineKeyboardButton(select_language2[i], callback_data=str(language))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=menu_select[i] + ':',
        reply_markup=reply_markup
    )
    return ENG_KOR

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(rus_main, pattern='^' + str(rus) + '$'),
                    CallbackQueryHandler(kaz_main, pattern='^' + str(kaz) + '$'),
                    CallbackQueryHandler(eng_main, pattern='^' + str(eng) + '$'),
                    CallbackQueryHandler(kor_main, pattern='^' + str(kor) + '$')],

            MENU_MAIN: [
                CallbackQueryHandler(kek_about_kz, pattern='^' + str(about_kz) + '$'),
                CallbackQueryHandler(menu_caddress, pattern='^' + str(caddress) + '$'),
                CallbackQueryHandler(menu_reg, pattern='^' + str(registration) + '$'),
                CallbackQueryHandler(menu_schedule, pattern='^' + str(schedule) + '$'),
                CallbackQueryHandler(main_menu, pattern='^' + str(menu) + '$'),
                CallbackQueryHandler(start_over, pattern='^' + str(language) + '$')],

            MENU_CADRESS: [CallbackQueryHandler(menu_addressroute, pattern='^' + str(addressroute) + '$'),
                           CallbackQueryHandler(start_over, pattern='^' + str(language) + '$'),
                           CallbackQueryHandler(main_menu, pattern='^' + str(menu) + '$')],

            MENU_ROUTE: [CallbackQueryHandler(menu_caddress, pattern='^' + str(caddress) + '$'),
                         CallbackQueryHandler(main_menu, pattern='^' + str(menu) + '$')],

            ENG_KOR: [
                CallbackQueryHandler(kek_about_kz, pattern='^' + str(about_kz) + '$'),
                CallbackQueryHandler(menu_caddress, pattern='^' + str(caddress) + '$'),
                CallbackQueryHandler(menu_schedule, pattern='^' + str(schedule) + '$'),
                CallbackQueryHandler(menu_reg, pattern='^' + str(registration) + '$'),
                CallbackQueryHandler(ke_main, pattern='^' + str(menu) + '$'),
                CallbackQueryHandler(start_over, pattern='^' + str(language) + '$')],

        },
        fallbacks=[CommandHandler('start', start)]
    )

    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=token)
    updater.bot.setWebhook('https://serene-earth-63918.herokuapp.com/' + token)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()