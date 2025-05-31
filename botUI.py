from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "6181494511:AAEXedyu8LDjxUI30Y213cQ9_Zhl7gNbWsg"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Bot menu buttons with Exit option and emojis
    keyboard = [
        [KeyboardButton("🌐 Website"), KeyboardButton("📂 Portal")],
        [KeyboardButton("💬 Telegram"), KeyboardButton("🛠️ Tools"), KeyboardButton("💻 Software")],
        [KeyboardButton("❌ Exit")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome! Use the menu below to select a category or exit.",
        reply_markup=reply_markup
    )

# Respond to menu buttons with inline keyboard
async def menu_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Define inline keyboard options based on button clicked
    if text == "🌐 website":
        inline_keyboard = [
            [InlineKeyboardButton("🌐 PP.EDU.COM", url="https://pp.edu.com"), InlineKeyboardButton("🌐 P.CODE.COM", url="https://p.code.com")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await update.message.reply_text("🌐 Website Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif text == "📂 portal":
        inline_keyboard = [
            [InlineKeyboardButton("📂 PP.EDU.PORTAL.COM", url="https://pp.edu.portal.com")],
            [InlineKeyboardButton("📘 Git Resources", callback_data="git_resources")],
            [InlineKeyboardButton("📝 Quiz", callback_data="quiz"), InlineKeyboardButton("🧑‍🎓 Pre-Exam", callback_data="pre_exam"), InlineKeyboardButton("📖 Lesson", callback_data="lesson")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await update.message.reply_text("📂 Portal Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif text == "💬 telegram":
        inline_keyboard = [
            [InlineKeyboardButton("💬 Telegram Group", url="https://t.me/example_group")],
            [InlineKeyboardButton("📢 Telegram Channel", url="https://t.me/example_channel")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await update.message.reply_text("💬 Telegram Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif text == "🛠️ tools":
        inline_keyboard = [
            [InlineKeyboardButton("⬇️ Download", callback_data="download"), InlineKeyboardButton("✏️ Auto Edit", callback_data="auto_edit")],
            [InlineKeyboardButton("👤 Reg Account", callback_data="reg_account"), InlineKeyboardButton("⚙️ Generate", callback_data="generate")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await update.message.reply_text("🛠️ Tools Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif text == "💻 software":
        inline_keyboard = [
            [InlineKeyboardButton("🪟 Windows", callback_data="window")],
            [InlineKeyboardButton("🍎 Mac", callback_data="mac"), InlineKeyboardButton("🐧 Linux", callback_data="linux")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await update.message.reply_text("💻 Software Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif text == "❌ exit":
        # Remove the keyboards and send a "Thanks" message
        await update.message.reply_text(
            "Thanks for using the bot! See you next time! 😊",
            reply_markup=ReplyKeyboardMarkup([], resize_keyboard=True)  # Remove the custom keyboard
        )
        await update.message.reply_text(
            "Goodbye! 👋", reply_markup=InlineKeyboardMarkup([])  # Remove the inline keyboard
        )

    else:
        await update.message.reply_text("Please select a valid menu option.")

# Callback handler for inline button actions
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the callback

    callback_data = query.data
    
    # Handle the various callback options
    if callback_data == "git_resources":
        await query.edit_message_text(
            text="📘 You selected 'Git Resources'. Accessing resources...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_portal")] 
            ])
        )
    elif callback_data == "quiz":
        await query.edit_message_text(
            text="📝 You selected 'Quiz'. Starting quiz...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_portal")] 
            ])
        )
    elif callback_data == "pre_exam":
        await query.edit_message_text(
            text="🧑‍🎓 You selected 'Pre-Exam'. Preparing exam materials...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_portal")] 
            ])
        )
    elif callback_data == "lesson":
        await query.edit_message_text(
            text="📖 You selected 'Lesson'. Loading lessons...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_portal")] 
            ])
        )
    elif callback_data == "download":
        await query.edit_message_text(
            text="⬇️ You selected 'Download'. Preparing download options...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_tools")] 
            ])
        )
    elif callback_data == "auto_edit":
        await query.edit_message_text(
            text="✏️ You selected 'Auto Edit'. Opening editor...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_tools")] 
            ])
        )
    elif callback_data == "reg_account":
        await query.edit_message_text(
            text="👤 You selected 'Reg Account'. Opening registration...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_tools")] 
            ])
        )
    elif callback_data == "generate":
        await query.edit_message_text(
            text="⚙️ You selected 'Generate'. Generating content...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_tools")] 
            ])
        )
    elif callback_data == "window":
        await query.edit_message_text(
            text="🪟 You selected 'Windows'.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_software")] 
            ])
        )
    elif callback_data == "mac":
        await query.edit_message_text(
            text="🍎 You selected 'Mac'.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_software")] 
            ])
        )
    elif callback_data == "linux":
        await query.edit_message_text(
            text="🐧 You selected 'Linux'.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="back_software")] 
            ])
        )
    elif callback_data == "hide":
        await query.edit_message_text(text="⛔ This section was hidden.")

    # Handle back buttons
    elif callback_data == "back_portal":
        inline_keyboard = [
            [InlineKeyboardButton("📂 PP.EDU.PORTAL.COM", url="https://pp.edu.portal.com")],
            [InlineKeyboardButton("📘 Git Resources", callback_data="git_resources")],
            [InlineKeyboardButton("📝 Quiz", callback_data="quiz"), InlineKeyboardButton("🧑‍🎓 Pre-Exam", callback_data="pre_exam"), InlineKeyboardButton("📖 Lesson", callback_data="lesson")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await query.edit_message_text(text="📂 Portal Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif callback_data == "back_tools":
        inline_keyboard = [
            [InlineKeyboardButton("⬇️ Download", callback_data="download"), InlineKeyboardButton("✏️ Auto Edit", callback_data="auto_edit")],
            [InlineKeyboardButton("👤 Reg Account", callback_data="reg_account"), InlineKeyboardButton("⚙️ Generate", callback_data="generate")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await query.edit_message_text(text="🛠️ Tools Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    elif callback_data == "back_software":
        inline_keyboard = [
            [InlineKeyboardButton("🪟 Windows", callback_data="window")],
            [InlineKeyboardButton("🍎 Mac", callback_data="mac"), InlineKeyboardButton("🐧 Linux", callback_data="linux")],
            [InlineKeyboardButton("⛔ Hide", callback_data="hide")]
        ]
        await query.edit_message_text(text="💻 Software Options:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

    else:
        await query.edit_message_text(text="Unknown action.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_response))
    app.add_handler(CallbackQueryHandler(button_callback))

    # Run the bot
    print("Bot is running...")
    app.run_polling()
