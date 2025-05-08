from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
import asyncio

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("coba klik tombol ini", callback_data='gift')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    opening_message = (
        "Halo, manusia paling cantik sejagad rayaaa 🌎✨\n"
        "Aku dikirim khusus dari planet Bucin untuk menyampaikan pesan penting banget nih...\n\n"
        "🎉🎂 SELAMAT ULANG TAHUNNN!! 🎂🎉\n\n"
        "Hari ini, seluruh jagat semesta berhenti sebentar…\n"
        "Kenapa? Karenaaaa... kamu ulang tahunnn~ 🎈\n\n"
        "🐣 Usia nambah, tapi tetap awet muda (pasti pakai serum bidadari ya?)\n"
        "🐾 Harapan nambah, tapi tetap rendah hati dan gemoy!\n"
        "🍰 Kue boleh manis, tapi kamu yang paling manisss\n\n"
        "Pokoknya, semoga kamu selalu bahagia, sehat, dan semua mimpi-mimpimu bisa tercapai yaa!\n\n"
        "Dan ingat...\n\n"
        "🌟 kamu spesial banget! buat aku\n\n"
        "🌟 makasih untuk semua perhatiannya\n\n"
        "📦 silahkan klik tombol dibawah ini"
    )
    await update.message.reply_text(opening_message, reply_markup=reply_markup)

# Callback for button presses
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'gift':
        keyboard = [
            [InlineKeyboardButton("🎁 Kotak Hadiah", callback_data='blue')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Klik kotaknya untuk membuka hadiah:", reply_markup=reply_markup)

    elif query.data == 'blue':
        await query.edit_message_text("🎁 Kotak Hadiah Berhasil Dibuka!!")

        # Kirim voice message
        voice_path = "ucapandariteman.mp3"
        with open(voice_path, "rb") as voice:
            await query.message.reply_voice(
                voice=InputFile(voice),
                caption="🗣️ Ucapan dari temanku biar yang ngucapin ultah ke kamu banyak 😁 💕"
            )

        # Kirim link hadiah
        await query.message.reply_text(
            "🎁 Klik link ini untuk membuka kejutan lainnya:\n"
            "🔗 https://link.dana.id/danakaget?c=s89stf5z3&r=gcSt7Q&orderId=20250508101214423715010300166325321749866"
        )

# Main function to run the bot
if __name__ == '__main__':
    import os

    TOKEN = "7587160420:AAHVyw83yOmhAjDYnvCkFCj5dXbmsdqa3Y8"

    # Menambahkan timeout di application builder
    app = ApplicationBuilder().token(TOKEN).request_kwargs({
        'timeout': 30  # Set timeout 30 detik
    }).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()
