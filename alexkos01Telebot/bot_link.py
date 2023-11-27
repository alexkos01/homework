
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, InlineKeyboardButton, InlineKeyboardMarkup
import time

bot = Bot(token='6781746793:AAFUBB_PE7kuic9hTh5DNfXSU7mrN5BMa5A')
dp = Dispatcher(bot)

user_but = ReplyKeyboardMarkup(keyboard=[[KeyboardButton('текущее время и дата')], [KeyboardButton('новости'), KeyboardButton('погода'), KeyboardButton('курсы валют')]],
                               resize_keyboard=True)

@dp.message_handler(commands='start')
async def cmd_start(mes: Message):
    await mes.reply(f'Hi, {mes.from_user.first_name} !!!', reply_markup=user_but)

@dp.message_handler()
async def choice_link(mes: Message):
    if mes.text == 'новости':
        await mes.reply('https://www.onliner.by/')
    if mes.text == 'погода':
        await mes.reply('https://yandex.by/pogoda/minsk?lat=53.847031&lon=27.454462')
    if mes.text == 'курсы валют':
        await mes.reply('https://myfin.by/currency/minsk')
    if mes.text == 'текущее время и дата':
        await mes.answer(f'{time.ctime()}')


if __name__ == '__main__':
    executor.start_polling(dp)

