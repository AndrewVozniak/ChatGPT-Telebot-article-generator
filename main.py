import telebot
import handlers.generateHandler as gen

bot_token = "5823067057:AAH2cOiLIzKDdp5C0XNV4Mex8gdFZKQgkac"
bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types='text')
def startMSG(message):
    bot.send_message(chat_id=message.chat.id, text=f"Введіть тематику статті")
    bot.register_next_step_handler(message, getLanguageStep)


def getLanguageStep(message):
    title = message.text

    bot.send_message(chat_id=message.chat.id, text="Введіть мову на якій необхідно написати статтю")

    bot.register_next_step_handler(message, getLengthStep, title)

def getLengthStep(message, title, lang=None):
    title = title
    lang = message.text

    bot.send_message(chat_id=message.chat.id, text="Введіть кількість символів")
    bot.register_next_step_handler(message, generateArticleStep, title, lang)

def generateArticleStep(message, title, lang):
    title = title
    lang = lang
    
    try:
        lenght = int(message.text)
        if(int(lenght) > 3000):
            bot.send_message(chat_id=message.chat.id, text="Макс к-сть символів - 3000")
            (message, title)
            return getLengthStep(message, title, lang)
        pass

    except:
        bot.send_message(chat_id=message.chat.id, text="К-сть символів необхідно ввести в числовому форматі")
        (message, title)
        return getLengthStep(message, title, lang)
        
    bot.send_message(chat_id=message.chat.id, text=f"""
Тема: {title}
Мова: {lang}
Приблизна к-сть символів: {lenght} 
""")



    bot.send_message(chat_id=message.chat.id, text="Генерація...")
    
    generated_article = gen.generate_article(title, lang, lenght)
    bot.send_message(chat_id=message.chat.id, text="Готово!")
    bot.send_message(chat_id=message.chat.id, text=f"""{generated_article}""")
    print("---------------------------------------------- FINAL GETTED TEXT ----------------------------------------------")
    print(generated_article)
    print("---------------------------------------------- FINAL GETTED TEXT ----------------------------------------------")

if __name__ == '__main__':
    bot.infinity_polling()