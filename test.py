# # aiogram import
# from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from aiogram.dispatcher import FSMContext


# # kode import
# from loader import dp, bot
# from utils import texts
# from .shazam import search_shazam




# @dp.message_handler(content_types=['text'], state='*')
# async def songs(message: Message, state: FSMContext):
#     term = message.text
#     songs_info = search_shazam(term, limit=10)
#     if songs_info:
#         keyboard = InlineKeyboardMarkup(row_width=5)
#         for i, song in enumerate(songs_info):
#             button = InlineKeyboardButton(text=str(i + 1), callback_data=f'songs_{i}')
#             keyboard.insert(button)
#         song_list = "\n".join(
#                 [f"{i+1}. {song['artist']} - {song['title']}"
#                 for i, song in enumerate(songs_info)]
#             )
#         await message.answer(f"{song_list}", reply_markup=keyboard)
#         await state.update_data(songs_info=songs_info)
#     else:
#         await message.reply(texts.NOT_SONGS)
