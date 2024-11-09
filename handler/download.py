# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts
import requests
import os



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('songs_'))
async def send_song(callback_query: CallbackQuery, state: FSMContext):
    loader_message = await callback_query.message.answer('⏳')

    await callback_query.answer()
    song_index = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    songs_info = data.get("songs_info")
    
    if not songs_info:
        await callback_query.message.reply(texts.NOT_SONGS)
        return

    song_info = songs_info[song_index]
    audio_response = requests.get(song_info['preview_url'])
    file_name = f"{song_info['title']} - {song_info['artist']}.m4a"
    
    with open(file_name, 'wb') as f:
        f.write(audio_response.content)
    
    await bot.send_audio(
        chat_id=callback_query.message.chat.id, 
        audio=open(file_name, 'rb'), 
        title=song_info['title'],  
        performer=song_info['artist']
    )
    
    os.remove(file_name)
    await loader_message.delete()

