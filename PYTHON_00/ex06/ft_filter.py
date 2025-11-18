def ft_filter(func, text: str):
    return [word for word in text.split(" ") if func(word)]
