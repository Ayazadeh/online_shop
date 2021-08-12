import time
import logging


class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # logger = logging.getLogger()
        start = time.time()
        response = self.get_response(request)
        duration = (time.time() - start)
        # logger.info(duration)
        # print(duration)
        return response
