from app.types.app_exception import AppException, InternalAppClientApiException

DIVIDER = "===+++==="


def app_log(message: str | None = None, exception: AppException | None = None) -> None:
    print(DIVIDER)
    print("APP LOG")
    if message is not None:
        print("Log message: " + message)

    if exception is not None:
        if isinstance(exception, InternalAppClientApiException):
            print("InternalAppClientApiException happened")
            print("Api name: " + exception.api_name)
            print("Http code: " + str(exception.http_code))
            print("Raw external api response: " + exception.raw_response)
        else:
            print("AppException happened")
            print("Exception message: " + exception.message)

    print(DIVIDER)
