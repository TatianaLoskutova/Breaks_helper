def convert_timedelta_to_str_time(delta):
    """Преобразование timedelta в строку."""

    hours = delta.seconds // 3600
    minutes = delta.seconds // 60 % 60
    return f'{hours} ч. {minutes // 10}{minutes % 10} мин.'
