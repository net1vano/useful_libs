def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))  # Создаем ключ на основе аргументов

        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return wrapper
