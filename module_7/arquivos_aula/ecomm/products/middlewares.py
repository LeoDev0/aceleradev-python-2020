def aceleradev_middleware(get_response):

    def middleware(request):
        if request.method == 'GET':
            print('Método da requisição é GET')

        print('====================')
        print('Acelera Dev')
        response = get_response(request)
        print("Online na Codenation")
        return response

    return middleware
