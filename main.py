import os
import telebot

bot = telebot.TeleBot("5002572407:AAHnM0MzJvxFfxy_TPrvVUtv51EpdcsBndY")

@bot.message_handler(commans=["start"])
def send_welcome(message)
bot.reply_to(message,"Hello! I'm Manager Chat Bot")

@bot.message_handler(commans=["how"])
def send_message(message)
 bot.send_message(message, https://www.google.com/search?q=wallpaper&sxsrf=AOaemvJ6bfOyD9qsC4pRkF01ZDBSQCAggw:1640165876317&tbm=isch&source=iu&ictx=1&fir=RJHvAPiXhbzXuM%252CmULm7CT_9_utqM%252C_%253BIKS91QWZqsszIM%252C6wSFmA6HgVHgSM%252C_%253BzPrPRShHp6WNXM%252CmULm7CT_9_utqM%252C_%253Bfzre3aU9rnarrM%252C0ajj5BOehSCl8M%252C_%253Bbkzg-uyYyGWrSM%252ClhWzaOns1IQZFM%252C_%253BSluRI4VYWRsGOM%252CbckAO52nKqfb8M%252C_%253B9M1EYRxTRPTpCM%252CmnO_VAPp79zIEM%252C_%253Buw1r51e_aOvuvM%252CHaWLKY5S6mzzsM%252C_%253BuzN6eEm6HBmV6M%252CPmbJzrTl7jaseM%252C_%253B3FGT2BGKfYoiiM%252CMyHNid4hx8jmQM%252C_%253Bfz2vHzjoLX_EtM%252CdTI5gDeOhrH8jM%252C_%253BUfxCDdRSVEyS7M%252C2ck3VkeIVMX80M%252C_%253B2hV1LYH0jeyiIM%252CmULm7CT_9_utqM%252C_%253BRF7Sp3OeQomm7M%252CtfXuGd1YzJVLIM%252C_%253BnDD_8zBx8SOjkM%252Cb7_zHYwdlueHWM%252C_%253BGdNAsz49jjjoZM%252C0ajj5BOehSCl8M%252C_%253ByanMw6uUjb0iQM%252CMyHNid4hx8jmQM%252C_%253BLYUYsWrol5zJQM%252CJj023YLKoNgz8M%252C_%253BZO4fGZVQ7XsC3M%252C5OzzJ9TulqdUgM%252C_%253BTpIZiyMgMTpEAM%252COnD4dCk6ZpOMrM%252C_%253BU7LgupY7593D7M%252CbckAO52nKqfb8M%252C_&vet=1&usg=AI4_-kSQ3gi6VUCXrIY9U19WQFSpVsgjvg&sa=X&sqi=2&ved=2ahUKEwjdq7iDjvf0AhUYHLkGHTJvC_gQ9QF6BAgVEAE#imgrc=SluRI4VYWRsGOM"")

bot.polling()