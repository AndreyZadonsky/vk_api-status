import vk_api
import time
import datetime
while True:
    vkapi = vk_api.VkApi(token = "")
    finaldate = datetime.date(2022, 10, 25)
    currentdate = datetime.date.today()
    days = str(finaldate - currentdate)
    days = days[:3]
    if int(days) % 100 in range(11, 20):
        vkapi.method("status.set", {"text": "До дня макарон осталось " + days + " дней"})
    elif int(days) % 10 == 1:
        vkapi.method("status.set", {"text": "До дня макарон остался " + days + " день"})
    elif int(days) % 10 in range(2, 5):
        vkapi.method("status.set", {"text": "До дня макарон осталось " + days + " дня"})
    else:
        vkapi.method("status.set", {"text": "До дня макарон осталось " + days + " дней"})
    time.sleep(3600) 
