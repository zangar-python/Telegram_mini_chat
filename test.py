from practice import to_celery,get_all_from_redis


# Добавляем число
# res = to_celery.delay(200)
# print(res)   # должно быть 49

# Смотрим все сохранённые ключи
print(get_all_from_redis())