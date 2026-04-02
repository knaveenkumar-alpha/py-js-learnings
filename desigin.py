class Auth:
    def __init__(self):
        pass
    def wrapper(request):
        token = request.headers.get("authorization")
        decode_data = jwt.decoded(token)
        username, groups, email 
        return decode_data


class Controller(Threadpool):
    def __init__(self, size, limit=10):
        self.size = size
        self.limit = limit
    def processor():


def decorator(nums):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            if nums > 10:
                process = Controller(limit=10)
                res = process.processor()
            return res
        return wrapper
    return inner_decorator


def file_reader(file_path):
    try:
        with open(file_path,  'r') as data_obj:
            data = data_obj.read()
    except PermissionError as per_err:
        print("you don't have permission to open/read the file")
        raise ""
    except EOFError as eof_err:
        print("End of the file error")
    except Exception as err:
        pass
    finally:
        pass
    return data
        
