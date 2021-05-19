import time
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


def process_template_response(request, response):
    return response


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response = func(self)
        costed = time.time() - start
        print('{:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        #costed = time.time() - self.start_time
        #print('{:.2f}s'.format(costed))
        return response