from stellar_error_handler import NETWORK_PASSPHRASE


class BaseStellarErrorModel:
    """
    Base class for all stellar error models.
    """

    def __init__(
        self,
        title: str,
        status: int,
        message: str,
        more_details: dict = None,
        tx_codes: list = None,
        operations: list = None,
        error_pointer: str = None,
        main_net: bool = True,
    ):
        self.network = (
            NETWORK_PASSPHRASE["MAIN_NET"]
            if main_net
            else NETWORK_PASSPHRASE["TESTNET"]
        )
        self.title = title
        self.status = status
        self.more_details = more_details
        self.tx_codes = tx_codes
        self.message = message
        self.operations = operations
        self.error_pointer = error_pointer

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

    def get_message(self):
        return self.message

    def get_operations(self):
        return self.operations

    def get_status(self):
        return self.status

    def get_tx_codes(self):
        return self.tx_codes

    def get_title(self):
        return self.title

    def get_more_details(self):
        return self.more_details

    def get_error_pointer(self):
        return self.error_pointer

    def __str__(self):
        return self.error_pointer if self.get_error_pointer() else "Object blank"

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
