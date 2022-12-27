from aiogram.utils import executor
from dispacher import dp

if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)