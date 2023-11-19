from PIL.ImageDraw import ImageDraw
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from PIL import Image, ImageFont, ImageDraw
import time
import os


bot = Bot(token='')
dp = Dispatcher(bot)

user_but = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='vk'), KeyboardButton(text='email')]],
                               resize_keyboard=True)


@dp.message_handler(commands='start')
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}', reply_markup=user_but)


@dp.message_handler()
async def choice(message: Message):
    user_but_inline1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='VK', url='https://vk.com/feed')]])
    user_but_inline2 = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='email', url='https://e.mail.ru/inbox?utm_source=portal&utm_medium=portal_navigation_under_search_exp&utm_campaign=e.mail.ru&mt_sub5=108&mt_sub1=e.mail.ru&mt_click_id=mt-jlsxn4-1700421792-2737324530')]])
    if message.text == 'vk':
        await message.reply(text='перейти', reply_markup=user_but_inline1)
    if message.text == 'email':
        await message.reply(text='перейти', reply_markup=user_but_inline2)





if __name__ == '__main__':
    executor.start_polling(dp)