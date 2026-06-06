import telebot
from telebot import types

TOKEN = "8771323622:AAHeI8ApDJEhIMBK_Cj9L4UfvpEuD7zO3NA"

bot = telebot.TeleBot(TOKEN)

# منوی اصلی پایین
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )

    btn1 = types.KeyboardButton("🛒 خرید سرویس")
    btn2 = types.KeyboardButton("🖥 حساب کاربری")
    btn3 = types.KeyboardButton("🎁 تست رایگان")
    btn4 = types.KeyboardButton("📞 پشتیبانی")
    btn5 = types.KeyboardButton("💰 کیف پول")
    btn6 = types.KeyboardButton("💡 همکاری و کسب درآمد")
    btn7 = types.KeyboardButton("📖 نحوه اتصال")

    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4, btn5)
    markup.add(btn6, btn7)

    bot.send_message(
        message.chat.id,
        """🦅 Falcon VPN

🚀 سرعت بالا
🛡 امنیت بالا
🌐 مناسب تمام اپراتورها

یکی از گزینه‌های زیر را انتخاب کنید 👇""",
        reply_markup=markup
    )

# منوی متن پیام
@bot.message_handler(func=lambda message: True)
def menu(message):

    if message.text == "🛒 خرید سرویس":

        markup = types.InlineKeyboardMarkup(row_width=1)

        markup.add(
            types.InlineKeyboardButton(
                "10 گیگ | 30 روز | 130,000 تومان",
                callback_data="10"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "20 گیگ | 30 روز | 180,000 تومان",
                callback_data="20"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "30 گیگ | 30 روز | 240,000 تومان",
                callback_data="30"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="back"
            )
        )

        bot.send_message(
            message.chat.id,
            """🚀 بالاترین سرعت و پایداری

✔ بدون قطعی
✔ مناسب تمامی کارها
✔ اتصال دائم

👇 حجم مورد نظر خودتون را انتخاب کنید""",
            reply_markup=markup
        )

    elif message.text == "📞 پشتیبانی":
        bot.send_message(message.chat.id, "@sandman745")

    elif message.text == "🎁 تست رایگان":
        bot.send_message(
            message.chat.id,
            "برای دریافت تست رایگان به پشتیبانی پیام دهید:\n@sandman745"
        )

    elif message.text == "💰 کیف پول":
        bot.send_message(
            message.chat.id,
            "موجودی کیف پول شما: 0 تومان"
        )

    elif message.text == "🖥 حساب کاربری":
        bot.send_message(
            message.chat.id,
            f"آیدی عددی شما:\n{message.from_user.id}"
        )

    elif message.text == "📖 نحوه اتصال":
        bot.send_message(
            message.chat.id,
            "آموزش اتصال به زودی اضافه می‌شود."
        )

    elif message.text == "💡 همکاری و کسب درآمد":
        bot.send_message(
            message.chat.id,
            "برای همکاری به پشتیبانی پیام دهید:\n@sandman745"
        )

# callback ها برای خرید و تایید پرداخت
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    prices = {"10": "130,000", "20": "180,000", "30": "240,000"}

    if call.data in ["10", "20", "30"]:

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(
                "💳 تایید و پرداخت",
                callback_data=f"pay{call.data}"
            ),
            types.InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="buy"
            )
        )

        bot.send_message(
            call.message.chat.id,
            f"""📦 {call.data} گیگ یک ماهه

📊 حجم: {call.data} گیگ
⏳ مدت: 30 روز
👤 تعداد کاربر: 1
💰 قیمت: {prices[call.data]} تومان
📥 دسته: V2ray

آیا خرید سرویس را تایید می‌کنید؟""",
            reply_markup=markup
        )

    elif call.data.startswith("pay"):
        bot.send_message(
            call.message.chat.id,
            """✅ پرداخت شما ثبت شد

📸 لطفاً رسید پرداخت را ارسال کنید.

💳 شماره کارت برای واریز:
6037-9974-3346-2919
👤 خلیلی

⏳ پس از بررسی، سرویس شما ارسال خواهد شد.

📞 پشتیبانی:
@sandman745"""
        )

    elif call.data == "back":
        start(call.message)

print("Bot Started...")
bot.infinity_polling()