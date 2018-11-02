from werkzeug.wrappers import Request, Response  # Flask的socket使用werkzeug实现，所以要导入 werkzeug

@Request.application

def hellow(request):
    return Response('Hello World')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost',400,hellow)

werkzeug
