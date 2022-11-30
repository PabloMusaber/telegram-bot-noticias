from config import *
from scraping.infobae import *
from scraping.xataka import *
from scraping.iproup import *
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)

#Respuesta comando start y help
@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    """Muestra los comandos disponibles y el instructivo de uso."""
    bot.reply_to(message, "Bienvenido")

@bot.message_handler(commands=["infobae"])
def cmd_infobae(message):
    """Muestra las noticias de la sección Últimas Noticias de Infobae"""
    noticiasDic = infobae(0)
    texto_msg = ''
    texto_msg+='<b>Infobae - Últimas Noticias</b>' + '\n'
    for noticia in list(noticiasDic.items()):
        texto_msg+= '<a href="'+noticia[1]['url']+'">'+noticia[1]['titulo']+'</a>' + '\n'
        texto_msg+= '\n'
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["tecno"])
def cmd_infobae(message):
    """Muestra las noticias de la sección Tecno de Infobae"""
    noticiasDic = infobae(1)
    texto_msg = ''
    texto_msg+='<b>Infobae - Tecno</b>' + '\n'
    for noticia in list(noticiasDic.items()):
        texto_msg+= '<a href="'+noticia[1]['url']+'">'+noticia[1]['titulo']+'</a>' + '\n'
        texto_msg+= '\n'
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["economia"])
def cmd_infobae(message):
    """Muestra las noticias de la sección Economía de Infobae"""
    noticiasDic = infobae(2)
    texto_msg = ''
    texto_msg+='<b>Infobae - Economía</b>' + '\n'
    for noticia in list(noticiasDic.items()):
        texto_msg+= '<a href="'+noticia[1]['url']+'">'+noticia[1]['titulo']+'</a>' + '\n'
        texto_msg+= '\n'
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["xataka"])
def cmd_xataka(message):
    """Muestra las noticias de Xataka"""
    noticiasDic = xataka()
    texto_msg = ''
    i=0
    texto_msg+='<b>Xataka</b>' + '\n'
    for noticia in list(noticiasDic.items()):
        if i==0:
            texto_msg+='<b>Noticias Principales</b>' + '\n'
        if i == len(list(noticiasDic.items()))//2:
            texto_msg+='<b>Noticias Secundarias</b>' + '\n'
        texto_msg+= '<a href="'+noticia[1]['url']+'">'+noticia[1]['titulo']+'</a>' + '\n'
        texto_msg+= '\n'
        i=i+1
    bot.reply_to(message, texto_msg, parse_mode="html", disable_web_page_preview=True)

@bot.message_handler(commands=["iproup"])
def cmd_xataka(message):
    """Muestra las noticias de iProUP"""
    noticiasDic = iproup()
    texto_msg = ''
    i=0
    texto_msg+='<b>iProUP</b>' + '\n'
    for noticia in list(noticiasDic.items()):
        texto_msg+= '<a href="'+noticia[1]['url']+'">'+noticia[1]['titulo']+'</a>' + '\n'
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
        telebot.types.BotCommand("/infobae","Muestra las noticias de la sección Últimas Noticias de Infobae"),
        telebot.types.BotCommand("/tecno","Muestra las noticias de la sección Tecno de Infobae"),
        telebot.types.BotCommand("/economia","Muestra las noticias de la sección Economía de Infobae"),
        telebot.types.BotCommand("/xataka","Muestra las noticias del sitio de Xataka"),
        telebot.types.BotCommand("/iproup","Muestra las noticias del sitio de iProUP")
    ])
    print ("Corriendo...") 
    bot.infinity_polling()
