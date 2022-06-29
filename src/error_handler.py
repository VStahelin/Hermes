from enum import Enum
from types import RESPONSE_BODY_TYPE

from models import BaseStellarErrorModel


class ErrorHandler:
    def __init__(self, error: object):
        self.error = error

    def get_error(self) -> BaseStellarErrorModel:
        """
        Treats the error and returns a stellar error model
        """
        error_type = (
            RESPONSE_BODY_TYPE[self.error["title"]]
            if self.error["title"] in RESPONSE_BODY_TYPE
            else None
        )
        if error_type:
            return HorizonFunctionsEnum.value[error_type](self.error)
        return HorizonFunctionsEnum.value[RESPONSE_BODY_TYPE["Unexpected Error"]](self.error)


def __transaction_failed__(error: object) -> BaseStellarErrorModel:
    pass


def __transaction_malformed__(error: object) -> BaseStellarErrorModel:
    pass


def __before_history__(error: object) -> BaseStellarErrorModel:
    pass


def __stale_history__(error: object) -> BaseStellarErrorModel:
    pass


def __timeout__(error: object) -> BaseStellarErrorModel:
    pass


def __bad_request__(error: object) -> BaseStellarErrorModel:
    pass


def __unexpected_error__(error: object) -> BaseStellarErrorModel:
    pass


class HorizonFunctionsEnum(Enum):
    TRANSACTION_FAILED = __transaction_failed__
    TRANSACTION_MALFORMED = __transaction_malformed__
    BEFORE_HISTORY = __before_history__
    STALE_HISTORY = __stale_history__
    TIMEOUT = __timeout__
    BAD_REQUEST = __bad_request__
    UNEXPECTED_ERROR = __unexpected_error__
