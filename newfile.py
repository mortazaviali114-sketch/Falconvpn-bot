import telebot
from telebot import types

TOKEN = "8771323622:AAHeI8ApDJEhIMBK_Cj9L4UfvpEuD7zO3NA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton("🛒 خرید سرویس", callback_data="buy")
    )

    markup.add(
        types.InlineKeyboardButton("💳 شماره کارت", callback_data="card")
    )

    markup.add(
        types.InlineKeyboardButton("🎁 اکانت تست", callback_data="test")
    )

    markup.add(
        types.InlineKeyboardButton("📞 پشتیبانی", callback_data="support")
    )

    bot.send_message(
        message.chat.id,
        """🦅 Falcon VPN

🚀 سرعت بالا
🛡 امنیت بالا
🌐 مناسب تمام اپراتورها

یکی از گزینه‌ها را انتخاب کنید:""",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "buy":

        markup = types.InlineKeyboardMarkup(row_width=1)

        markup.add(
            types.InlineKeyboardButton(
                "💎 10 گیگ | 30 روز | 130,000 تومان",
                callback_data="10"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "💎 20 گیگ | 30 روز | 180,000 تومان",
                callback_data="20"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "💎 30 گیگ | 30 روز | 250,000 تومان",
                callback_data="30"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="back"
            )
        )

        bot.edit_message_text(
            """🚀 سرویس Falcon VPN

حجم مورد نظر خود را انتخاب کنید 👇""",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif call.data in ["10", "20", "30"]:

        prices = {
            "10": "130,000",
            "20": "180,000",
            "30": "250,000"
        }

        markup = types.InlineKeyboardMarkup(row_width=1)

        markup.add(
            types.InlineKeyboardButton(
                "✅ پرداخت کردم",
                callback_data="paid"
            )
        )

        bot.send_message(
            call.message.chat.id,
            f"""✅ پلن انتخابی

📦 {call.data} گیگ | 30 روز

💰 مبلغ:
{prices[call.data]} تومان

💳 شماره کارت:
6037-9974-3346-2919

👤 خلیلی

👇 پس از پرداخت روی دکمه زیر بزنید""",
            reply_markup=markup
        )

    elif call.data == "paid":

        bot.send_message(
            call.message.chat.id,
            """✅ پرداخت شما ثبت شد

📸 لطفاً رسید پرداخت را ارسال کنید.

⏳ پس از بررسی، سرویس شما ارسال خواهد شد.

📞 پشتیبانی:
@sandman745"""
        )

    elif call.data == "card":

        bot.send_message(
            call.message.chat.id,
            """💳 شماره کارت

6037-9974-3346-2919

👤 خلیلی"""
        )

    elif call.data == "support":

        bot.send_message(
            call.message.chat.id,
            "📞 پشتیبانی\n\n@sandman745"
        )

    elif call.data == "test":

        bot.send_message(
            call.message.chat.id,
            """🎁 اکانت تست

برای دریافت اکانت تست به آیدی زیر پیام دهید:

@sandman745"""
        )

    elif call.data == "back":
        start(call.message)

print("Bot Started...")
bot.infinity_polling()
