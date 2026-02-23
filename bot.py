from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes
)

# ================= CONFIG =================

BOT_TOKEN = "8290722482:AAGb71H5EMauXc3AjOgU-PlZy8oOXzu5dNE"
CHANNEL_ID = -1003784548581   # your private channel/group id

WELCOME_MESSAGE = """
✅ <b>Join Approved Successfully!</b>

🎉 Welcome to the Private Community

You received this message because you requested to join our private channel.

🔞 Please confirm you are 18+
📩 Links & content will be shared soon

Enjoy your access 🚀
"""

# ================= AUTO APPROVE =================

async def approve_user(update: Update, context: ContextTypes.DEFAULT_TYPE):

    request = update.chat_join_request

    user_id = request.from_user.id
    chat_id = request.chat.id

    try:
        # approve request
        await context.bot.approve_chat_join_request(
            chat_id=chat_id,
            user_id=user_id
        )

        print(f"Approved user {user_id}")

        # send DM message
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=WELCOME_MESSAGE,
                parse_mode="HTML"
            )
            print("Message sent to user")

        except Exception as e:
            print("User never started bot (DM blocked)")

    except Exception as e:
        print("Approval error:", e)


# ================= MAIN =================

def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_user))

    print("Auto Approve Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()
