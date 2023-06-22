# pylint: disable=missing-function-docstring
import logging
import urllib.parse
from collections import Counter
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

movies = []
votes = Counter()

# basic /start command for bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am a bot developed by MaxFax")


# getting link to the movie by searching on imdb
def get_imdb_link(movie_title):
    encoded_title = urllib.parse.quote(movie_title)
    imdb_link = f"https://www.imdb.com/find?q={encoded_title}"
    return imdb_link


# error command
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this command does not exist")


# adding movie to the list of movies
async def add_movie(update, context):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="After command /add please enter the movie name, ex: /add Titanic")
    else:
        # joining the words in the movie title
        movie_title = ' '.join(context.args)
        movies.append(movie_title)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Added a movie: {movie_title}")


# showing the list of added movies
async def list_movies(update, context):
    if len(movies) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You have not added any movies yet")
    else:
        movie_list = ''
        for movie in movies:
            imdb_link = get_imdb_link(movie)
            movie_list += f"{movie} - [IMDb]({imdb_link})\n"

        await context.bot.send_message(chat_id=update.effective_chat.id, text=movie_list, parse_mode='Markdown')


# removing movies from the list
async def remove_movie(update, context):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="After the /remove command, enter the name of the movie, for example: /remove Titanic")
    else:
        # joining the words in the movie title
        movie_title = ' '.join(context.args)
        # converting the title into lower register
        movie_title_lower = movie_title.lower()
        removed_movies = []

        for movie in movies:
            if movie.lower() == movie_title_lower:
                movies.remove(movie)
                removed_movies.append(movie)

        if removed_movies:
            removed_movies_str = '\n'.join(removed_movies)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Movies removed:\n{removed_movies_str}")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Movies not found in the list.")


# voting for movie
async def vote_movie(update, context):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="After the /vote command, enter the name of the movie, for example: /vote Titanic")
    else:
        movie_title = ' '.join(context.args)
    if movie_title in movies:
        votes[update.effective_user.id] += 1
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Voted for movie: {movie_title}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Movie is not found in the list.")


# showing the vote results
async def show_votes(update, context):
    votes_count = dict(votes)
    if len(votes_count) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="There are no votes yet.")
    else:
        votes_message = '\n'.join(
            [f"{user_id}: {count}" for user_id, count in votes_count.items()])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Votes:\n{votes_message}")


if __name__ == '__main__':
    application = ApplicationBuilder().token(
        'YOUR_BOT_API_TOKEN').build()

    start_handler = CommandHandler('start', start)
    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_movie))
    application.add_handler(CommandHandler("list", list_movies))
    application.add_handler(CommandHandler("remove", remove_movie))
    application.add_handler(CommandHandler("vote", vote_movie))
    application.add_handler(CommandHandler("votes", show_votes))
    application.add_handler(unknown_handler)

    application.run_polling()
