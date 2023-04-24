import logging
import requests
from telegram.ext import Application, MessageHandler, filters, CommandHandler  # StringCommandHandler
from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup, KeyboardButton


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)  # Запускаем логирование Debuger

logger = logging.getLogger(__name__)
location_button = KeyboardButton("Отправить геопозицию", request_location=True)
my_keyboard_geo = ReplyKeyboardMarkup([[location_button]], resize_keyboard=True, one_time_keyboard=True)
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
reply_keyboard_start = [['/Obtsepit', '/Products', "/Auto", "/Kyltyra"],
                      ['/Medicine', '/Magazine', "/Krasota", "/Otdix"]]
markup_start = ReplyKeyboardMarkup(reply_keyboard_start, one_time_keyboard=False)


async def echo(update, context):
    await update.message.reply_text(f"Извините я не понимаю обычный текст, пожалуйста общайтесь со мной командами")


async def start(update, context):
    global markup_start
    user = update.effective_user  # Отправляет сообщение когда получена команда /start
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я чат-бот. Я помогу вам найти нужное место рядом с вами.",
        reply_markup=markup_start)


async def help_command(update, context):
    await update.message.reply_text("По всем вопросам обращайтесь к разработчику: andrey.medvedev.55.78@yandex.ru")


async def Obtsepit(update, context):
    reply_keyboard = ['/Kafe', '/Restoran', "/Vse"],
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text("Выбирите что-либо из предложенного:", reply_markup=markup)


async def Products(update, context):
    kuda.append("Магазин продуктов")
    await update.message.reply_text("Для того чтобы найти продуктовые магазины рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def Avto(update, context):
    reply_keyboard = ['/Automoika', '/Automasterskaia', "/Autozapthasti", "/Autosalon"],
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text("Выбирите что-либо из предложенного:", reply_markup=markup)


async def Medecine(update, context):
    reply_keyboard = ['/Apteka', '/Bolnitsa', "/Stomatologiya"],
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text("Выбирите что-либо из предложенного:", reply_markup=markup)


async def Magazin(update, context):
    reply_keyboard = [['/Detskiy', '/Sadovod', "/Kanstovari", '/Obuv'],
                      ["/Odezda", "/Tsevetov", '/Sportive', '/Supermarket']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text("Выбирите что-либо из предложенного:", reply_markup=markup)


async def krasota(update, context):
    reply_keyboard = [['/Salonkrasoti', '/Parikxmaxerskai', "/Kosmetika", '/Parfumeria']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text("Выберите что-либо из предложенного:", reply_markup=markup)


async def kafe(update, context):
    kuda.append("Кафе")
    await update.message.reply_text("Для того чтобы найти кафе рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def restoran(update, context):
    kuda.append("Ресторан")
    await update.message.reply_text("Для того чтобы найти рестораны рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def vse_ob(update, context):
    kuda.append("Еда")
    await update.message.reply_text("Для того чтобы найти все возможные места питания рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def auto_moika(update, context):
    kuda.append("Автомойка")
    await update.message.reply_text("Для того чтобы найти автомойки рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def auto_masterskaia(update, context):
    kuda.append("Автосервис")
    await update.message.reply_text("Для того чтобы найти автомастерскии рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def auto_zapthasti(update, context):
    kuda.append("Магазин автозапчастей и авто товаров")
    await update.message.reply_text("Для того чтобы найти магазины авто запчастей рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def auto_salon(update, context):
    kuda.append("Автосалон")
    await update.message.reply_text("Для того чтобы найти авто салоны рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def stomatologiya(update, context):
    kuda.append("Стоматологическая клиника")
    await update.message.reply_text("Для того чтобы найти стоматологическую клинику рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def apteka(update, context):
    kuda.append("Аптека")
    await update.message.reply_text("Для того чтобы найти аптеки рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def bolnitsa(update, context):
    kuda.append("Больница")
    await update.message.reply_text("Для того чтобы найти больницы рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def detskiy(update, context):
    kuda.append("Детский магазин")
    await update.message.reply_text("Для того чтобы найти детские магазины рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def sadovod(update, context):
    kuda.append("Магазин для садоводов")
    await update.message.reply_text("Для того чтобы найти садоводческие магазины рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def kanstovari(update, context):
    kuda.append("Магазин канцтоваров")
    await update.message.reply_text("Для того чтобы найти магазины канцтоваров больницы рядом мне нужна ваша"
                                    " геолокация.", reply_markup=my_keyboard_geo)


async def obuv(update, context):
    kuda.append("Магазин обуви")
    await update.message.reply_text("Для того чтобы найти обувные магазины рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def odezda(update, context):
    kuda.append("Магазин одежды")
    await update.message.reply_text("Для того чтобы найти магазины одежды рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def tsevetov(update, context):
    kuda.append("Магазин цветов")
    await update.message.reply_text("Для того чтобы найти магазины цветов рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def sportive(update, context):
    kuda.append("Спортивный магазин")
    await update.message.reply_text("Для того чтобы найти спортивные магазины рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def supermarket(update, context):
    kuda.append("Супермаркет")
    await update.message.reply_text("Для того чтобы найти супермаркеты рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def salonkrasoti(update, context):
    kuda.append("Салон красоты")
    await update.message.reply_text("Для того чтобы найти салоны красоты рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def parikxmaxerskai(update, context):
    kuda.append("Парикмахерская")
    await update.message.reply_text("Для того чтобы найти парикмахерские рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def kosmetika(update, context):
    kuda.append("Магазин косметики")
    await update.message.reply_text("Для того чтобы найти магазины косметики рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def parfumeria(update, context):
    kuda.append("Магазин парфюмерии")
    await update.message.reply_text("Для того чтобы найти магазины парфюмерии рядом мне нужна ваша геолокация.",
                                    reply_markup=my_keyboard_geo)


async def location(update, context):
    message = update.message   # получаем объект сообщения (локации)
    current_position = (message.location.longitude, message.location.latitude)  # вытаскиваем из него долготу и ширину
    coords = f"{current_position[0]},{current_position[1]}"  # создаем строку в виде долготы, широты
    if foto(coords):
        await context.bot.send_photo(
            update.message.chat_id,
            foto(coords),
            caption="Нашёл. Хотите найти что-то ещё?", reply_markup=markup_start)
    else:
        await update.message.reply_text(f"Извините при поиске {kuda[-1]} произошла ошибка, попробуйте найти что-нибудь "
                                        f"другое.", reply_markup=markup_start)


def foto(kords):
    global api_key
    search_api_server = "https://search-maps.yandex.ru/v1/"
    address_ll = str(kords)
    search_params = {
        "apikey": api_key,
        "text": kuda[-1],
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz",
        "results": 3
    }
    response = requests.get(search_api_server, params=search_params)
    if not response:
        return False
    json_response = response.json()  # Преобразуем ответ в json-объект
    delta = "0.005"
    kords_x0, kords_y0 = kords.split(",")
    org_point = "{0},{1}".format(kords_x0, kords_y0)
    if len(json_response["features"]) >= 3:
        organization = [json_response["features"][0], json_response["features"][1], json_response["features"][2]]
        point = [organization[0]["geometry"]["coordinates"], organization[1]["geometry"]["coordinates"],
                 organization[2]["geometry"]["coordinates"]]
        org_point_1 = "{0},{1}".format(point[0][0], point[0][1])  # Получаем координаты ответа.
        org_point_2 = "{0},{1}".format(point[1][0], point[1][1])  # Получаем координаты ответа.
        org_point_3 = "{0},{1}".format(point[2][0], point[2][1])  # Получаем координаты ответа.
        map_params = {                                 # Собираем параметры для запроса к StaticMapsAPI:
            #  "ll": address_ll, отключена чтобы автоматически настраивались размеры для показа меток
            "spn": ",".join([delta, delta]),
            "l": "map",
            "pt": f"{'{0},pm2rdl'.format(org_point_1)}~"f"{'{0},pm2rdl'.format(org_point_2)}"
                  f"~{'{0},pm2rdl'.format(org_point_3)}~{'{0},flag'.format(org_point)}"
        }
    elif len(json_response["features"]) == 2:
        organization = [json_response["features"][0], json_response["features"][1]]
        point = [organization[0]["geometry"]["coordinates"], organization[1]["geometry"]["coordinates"]]
        org_point_1 = "{0},{1}".format(point[0][0], point[0][1])  # Получаем координаты ответа.
        org_point_2 = "{0},{1}".format(point[1][0], point[1][1])  # Получаем координаты ответа.
        map_params = {                                 # Собираем параметры для запроса к StaticMapsAPI:
            # "ll": address_ll,
            "spn": ",".join([delta, delta]),           # позиционируем карту центром на наш исходный адрес
            "l": "map",
            "pt": f"{'{0},pm2rdl'.format(org_point_1)}~"f"{'{0},pm2rdl'.format(org_point_2)}"
                  f"~{'{0},flag'.format(org_point)}"
        }
    elif len(json_response["features"]) == 1:
        organization = [json_response["features"][0]]
        point = [organization[0]["geometry"]["coordinates"]]
        org_point_1 = "{0},{1}".format(point[0][0], point[0][1])  # Получаем координаты ответа.
        map_params = {                                 # Собираем параметры для запроса к StaticMapsAPI:
            # "ll": address_ll,
            "spn": ",".join([delta, delta]),           # позиционируем карту центром на наш исходный адрес
            "l": "map",
            "pt": f"{'{0},pm2rdl'.format(org_point_1)}~{'{0},flag'.format(org_point)}"
        }
    else:
        return False
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)  # выполняем запрос
    map_file = "map.png"    # Запишем полученное изображение в файл.
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def main():
    global my_keyboard_geo, kuda, markup_start
    application = Application.builder().token(BOT_TOKEN).read_timeout(30).write_timeout(30).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)  # обработчик echo для текстовых сообщений
    kords_handler = MessageHandler(filters.LOCATION, location)
    application.add_handler(CommandHandler('Obtsepit', Obtsepit))
    application.add_handler(CommandHandler('Products', Products))
    application.add_handler(CommandHandler("Auto", Avto))
    application.add_handler(CommandHandler('Medicine', Medecine))
    application.add_handler(CommandHandler('Magazine', Magazin))
    application.add_handler(CommandHandler('Krasota', krasota))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("Kafe", kafe))
    application.add_handler(CommandHandler("Restoran", restoran))
    application.add_handler(CommandHandler("Vse", vse_ob))
    application.add_handler(CommandHandler("Automoika", auto_moika))
    application.add_handler(CommandHandler("Automasterskaia", auto_masterskaia))
    application.add_handler(CommandHandler("Autozapthasti", auto_zapthasti))
    application.add_handler(CommandHandler("Autosalon", auto_salon))
    application.add_handler(CommandHandler("Apteka", apteka))
    application.add_handler(CommandHandler("Bolnitsa", bolnitsa))
    application.add_handler(CommandHandler("Stomatologiya", stomatologiya))
    application.add_handler(CommandHandler("Detskiy", detskiy))
    application.add_handler(CommandHandler("Sadovod", sadovod))
    application.add_handler(CommandHandler("Kanstovari", kanstovari))
    application.add_handler(CommandHandler("Obuv", obuv))
    application.add_handler(CommandHandler("Odezda", odezda))
    application.add_handler(CommandHandler("Tsevetov", tsevetov))
    application.add_handler(CommandHandler("Sportive", sportive))
    application.add_handler(CommandHandler("Supermarket", supermarket))
    application.add_handler(CommandHandler("Salonkrasoti", salonkrasoti))
    application.add_handler(CommandHandler("Parikxmaxerskai", parikxmaxerskai))
    application.add_handler(CommandHandler("Kosmetika", kosmetika))
    application.add_handler(CommandHandler("Parfumeria", parfumeria))
    application.add_handler(text_handler)  # Регистрируем обработчик в приложении.
    application.add_handler(kords_handler)
    application.run_polling()   # Запускаем приложение.
    application.idle()


if __name__ == '__main__':
    kuda = ["ничего"]
    main()