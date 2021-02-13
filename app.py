from loader import db

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp


    try:
        db.create_table_users()
    except Exception as e:
        print(e)
   # db.delete_users()
   # print(db.select_all_users)



executor.start_polling(dp)
