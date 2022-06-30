from stellar_error_handler import NETWORK_PASSPHRASE


class StellarError:
    """
    Base class for all stellar error models.
    """

    def __init__(
        self,
        main_net: bool = True,
        title: str = None,
        status: int = None,
        message: str = None,
        tx_codes: list = None,
        operations: list = None,
        more_details: dict = None,
        error_pointer: dict = None,
    ):
        self._network_ = (
            NETWORK_PASSPHRASE["MAIN_NET"]
            if main_net
            else NETWORK_PASSPHRASE["TESTNET"]
        )
        self._title_ = title
        self._status_ = status
        self._more_details_ = more_details
        self._tx_codes_ = tx_codes
        self._message_ = message
        self._operations_ = operations
        self._error_pointer_ = error_pointer

    def has_any_info(self):
        """
        Checks if any info is available
        """
        return any(
            [
                self.get_title(),
                self.get_message(),
                self.get_operations(),
                self.get_more_details(),
            ]
        )

    def get_network(self) -> None or str:
        return self._network_

    def set_network(self, network: str) -> None or str:
        if network in NETWORK_PASSPHRASE:
            self._network_ = NETWORK_PASSPHRASE[network]
        return "Network not found"

    def get_title(self) -> None or str:
        return self._title_

    def set_title(self, title: str):
        self._title_ = title

    def get_status(self) -> int:
        return self._status_

    def set_status(self, status: int) -> None or int:
        self._status_ = status

    def get_message(self) -> None or str:
        return self._message_

    def set_message(self, message: str):
        self._message_ = message

    def get_more_details(self) -> None or dict:
        return self._more_details_

    def set_more_details(self, more_details: dict):
        self._more_details_ = more_details

    def get_operations(self) -> None or list:
        return self._operations_

    def set_operations(self, operations: list):
        self._operations_ = operations

    def get_tx_codes(self) -> None or list:
        return self._tx_codes_

    def set_tx_codes(self, tx_codes: list):
        self._tx_codes_ = tx_codes

    def get_error_pointer(self) -> None or dict:
        return self._error_pointer_

    def set_error_pointer(self, error_pointer: dict):
        self._error_pointer_ = error_pointer

    def __str__(self):
        return self._error_pointer_ if self.get_error_pointer() else "Object blank"

    def as_dict(self):
        """
        Returns a dict representation of the error
        """
        if self.has_any_info():
            return {
                "title": self.get_title(),
                "status": self.get_status(),
                "message": self.get_message(),
                "tx_codes": self.get_tx_codes(),
                "operations": self.get_operations(),
                "more_details": self.get_more_details(),
            }

        return {
            "detail": "Object blank",
        }

    def as_json(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.evaluate(*args, **kwargs)

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError("Evaluate method not implemented.")
