
class Basket():
    """
    default behaviors that can be inherited or overrided
    """

    def __init__(self,request):
        self.session = request.session
        #session key
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {
                'number': 123123
            }
            self.basket = basket