from config import *
from scraping.infobae import *
from scraping.xataka import *
from scraping.iproup import *
import telebot
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start", "noticias"])
def cmd_start(message):
    markup = InlineKeyboardMarkup(row_width = 3)
    b1 = InlineKeyboardButton("♦️ Infobae", callback_data="infobae")
    b2 = InlineKeyboardButton("♦️ Tecno", callback_data="infobae_tecno")
    b3 = InlineKeyboardButton("♦️ Economía", callback_data="infobae_economia")
    b4 = InlineKeyboardButton("🟢 Xataka", callback_data="xataka")
    b5 = InlineKeyboardButton("🔵 iProUP", callback_data="iproup")
    markup.add(b1,b2,b3,b4,b5)
    bot.send_message(
        message.chat.id,
        '¿De qué <b>sitio</b> desea obtener información?',
        parse_mode="html",
        reply_markup=markup)

@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
    """Controla las respuestas al precionar cada botón"""
    match call.data:
        case "infobae":
            cmd_infobae(call.message)
        case "infobae_tecno":
            cmd_infobae_tecno(call.message)
        case "infobae_economia":
            cmd_infobae_economia(call.message)
        case "xataka":
            cmd_xataka(call.message)
        case "iproup":
            cmd_iproup(call.message)

@bot.message_handler(commands=["help"])
def cmd_help(message):
    """Muestra el mensaje de ayuda e instrucciones de uso."""
    texto_msg = 'Utilice el comando <b>/noticias</b> para ver los sitios de los que puede obtener noticias. '
    texto_msg+='Si lo desea, puede utilizar <b>comandos</b> para traer noticias de los diferentes sitios. '
    texto_msg+='Dichos comandos son:' + '\n'
    texto_msg+='<b>/infobae</b> - Muestra las noticias de la sección <b>Últimas Noticias</b> de Infobae' + '\n'
    texto_msg+='<b>/tecno</b> - Muestra las noticias de la sección <b>Tecno</b> de Infobae' + '\n'
    texto_msg+='<b>/economia</b> - Muestra las noticias de la sección <b>Economía</b> de Infobae' + '\n'
    texto_msg+='<b>/xataka</b> - Muestra las noticias del sitio de Xataka' + '\n'
    texto_msg+='<b>/iproup</b> - Muestra las noticias del sitio de iProUP' + '\n'
    bot.reply_to(message, texto_msg, parse_mode="html")

@bot.message_handler(commands=["infobae"])
def cmd_infobae(message):
    """Muestra las noticias de la sección Últimas Noticias de Infobae"""
    lista_noticias = infobae(0)
    texto_msg = ''
    texto_msg+='<b>Infobae - Últimas Noticias</b>' + '\n'
    for noticia in lista_noticias:
        texto_msg+= '<a href="'+noticia[1]+'">'+noticia[0]+'</a>' + '\n'
        texto_msg+= '\n'
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["tecno"])
def cmd_infobae_tecno(message):
    """Muestra las noticias de la sección Tecno de Infobae"""
    lista_noticias = infobae(1)
    texto_msg = ''
    texto_msg+='<b>Infobae - Tecno</b>' + '\n'
    for noticia in lista_noticias:
        texto_msg+= '<a href="'+noticia[1]+'">'+noticia[0]+'</a>' + '\n'
        texto_msg+= '\n'
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["economia"])
def cmd_infobae_economia(message):
    """Muestra las noticias de la sección Economía de Infobae"""
    lista_noticias = infobae(2)
    texto_msg = ''
    texto_msg+='<b>Infobae - Economía</b>' + '\n'
    for noticia in lista_noticias:
        texto_msg+= '<a href="'+noticia[1]+'">'+noticia[0]+'</a>' + '\n'
        texto_msg+= '\n'
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["xataka"])
def cmd_xataka(message):
    """Muestra las noticias de Xataka"""
    lista_noticias = xataka()
    texto_msg = ''
    i=0
    texto_msg+='<b>Xataka</b>' + '\n'
    for noticia in lista_noticias:
        if i==0:
            texto_msg+='<b>Noticias Principales</b>' + '\n'
        if i == len(lista_noticias)//2:
            texto_msg+='<b>Noticias Secundarias</b>' + '\n'
        texto_msg+= '<a href="'+noticia[1]+'">'+noticia[0]+'</a>' + '\n'
        texto_msg+= '\n'
        i=i+1
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["iproup"])
def cmd_iproup(message):
    """Muestra las noticias de iProUP"""
    lista_noticias = iproup()
    texto_msg = ''
    i=0
    texto_msg+='<b>iProUP</b>' + '\n'
    for noticia in lista_noticias:
        texto_msg+= '<a href="'+noticia[1]+'">'+noticia[0]+'</a>' + '\n'
        texto_msg+= '\n'
        i=i+1
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(content_types=["text"])
def text_messages(message):
    """Gestiona los mensajes recibidos, tanto textos simples como comandos no disponibles."""
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "El comando ingresado no existe.")
    else:
        bot.send_message(message.chat.id, "Ingrese un comando. Utilice /help para obtener infomación de ayuda.")


###### MAIN ######
if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand("/help","Muestra las instrucciones de uso"),
        telebot.types.BotCommand("/noticias","Muestra los sitios disponibles para obtener noticias."),
        telebot.types.BotCommand("/infobae","Muestra las noticias de la sección Últimas Noticias de Infobae"),
        telebot.types.BotCommand("/tecno","Muestra las noticias de la sección Tecno de Infobae"),
        telebot.types.BotCommand("/economia","Muestra las noticias de la sección Economía de Infobae"),
        telebot.types.BotCommand("/xataka","Muestra las noticias del sitio de Xataka"),
        telebot.types.BotCommand("/iproup","Muestra las noticias del sitio de iProUP")
    ])
    print ("Corriendo...") 
    bot.infinity_polling()
