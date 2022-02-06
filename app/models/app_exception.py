class AppException(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


class InternalAppClientApiException(AppException):
    def __init__(self, api_name: str, http_code: int, raw_response: str):
        super().__init__("An error occurred on the service while trying to get data")
        self.api_name = api_name
        self.http_code = http_code
        self.raw_response = raw_response
