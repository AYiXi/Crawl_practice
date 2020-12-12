import functools
import time


def time_use(function):
    # 打印函数运行时间
    def decorator(*args, **kwargs):
        start = time.time()
        results = function(*args, **kwargs)
        print('[FUNCTION] %s' % function.__name__ + ' USE TIME:', '%.3f' % (time.time() - start) + 's')
        return results

    return decorator

def async_time_use(function):
    # 打印函数运行时间
    async def decorator(*args, **kwargs):
        start = time.time()
        results = await function(*args, **kwargs)
        print('[FUNCTION] %s' % function.__name__ + ' USE TIME:', '%.3f' % (time.time() - start) + 's')
        return results

    return decorator

def repeat(*args, **kwargs):
    # 重复运行函数
    # @repeat_func, @repeat_func(100), @repeat_func(repeat=100)

    # *args, **kwargs: 装饰器的参数
    # 如果装饰器本身不带参数, args[0] == f
    # 此时 repeat_func() ==  decorator,
    # repeat_func()(args[0]) ==  decorator(f)
    if len(args) == 1 and callable(args[0]):
        # repeat_function() -> decorator
        return repeat()(args[0])

    # 装饰器本身带参数
    else:
        # f: 被装饰的函数, *fargs, **fkw: 函数的参数
        def decorator(f):
            @functools.wraps(f)
            def wrap(*fargs, **fkw):
                if not args:
                    repeat_times = kwargs.get('repeat', 10)
                else:
                    repeat_times = kwargs.get('repeat') or args[0]
                for _ in range(repeat_times):
                    f(*fargs, **fkw)

            return wrap

        return decorator