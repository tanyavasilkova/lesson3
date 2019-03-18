import functools
def check_len(leng):
    # используем замыкание
    def check_len_arg(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            print(args)
            if len(args[0]) > leng:
                return 'Too big'
            value = func(*args, **kwargs)
            # Do something after
            return value
        return wrapper_decorator
    return check_len_arg

