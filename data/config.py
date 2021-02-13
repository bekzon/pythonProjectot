import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [

]

ip = os.getenv("ip")

aiogram_redis = {
    'hosts': ip
}

#redis = {
  #  'addres': (ip, 6379),
  #  'encoding': 'utf8'
#}