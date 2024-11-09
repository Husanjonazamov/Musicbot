# aiogram import
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts
from .shazam import search_shazam



@dp.message_handler(content_types=['text'], state='*')
async def songs(message: Message, state: FSMContext):
    term = message.text
    songs_info = search_shazam(term, limit=10)
    if songs_info:
        songs_buttons = InlineKeyboardMarkup(row_width=5)
        for i, song in enumerate(songs_info):
            buttons = InlineKeyboardButton(text=str(i+1), callback_data=f"songs_{i}")
            songs_buttons.insert(buttons)
        songs_list = "\n".join(
            [f"{i+1}. {song['artist']} - {song['title']}"
            for i, song in enumerate(songs_info)]
        )
        await message.answer(f"{songs_list}", reply_markup=songs_buttons)
        await state.update_data(songs_info=songs_info)
    else:
        await message.answer(texts.NOT_SONGS)

        