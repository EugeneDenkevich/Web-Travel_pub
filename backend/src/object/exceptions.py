from rest_framework.exceptions import APIException

# Exeptions details:
HOUSE_TAKEN = 'House is already taken. Point another house.'
DESIRED_ARRIVAL = 'The departure date should be later than the arrival date'


class HouseIsTakenExeption(APIException):
    status_code = 409
    default_detail = HOUSE_TAKEN
    default_code = 'house_taken'


class DesiredArivalExeption(APIException):
    status_code = 422
    default_detail = DESIRED_ARRIVAL
    default_code = 'desired_arrival'