from stellar_sdk.xdr import DecoratedSignature, TransactionEnvelope, TransactionResult

from consts import MALFORMED_ERRORS_MESSAGES, MESSAGES, RESPONSE_BODY_TYPE
from models import StellarError
from transaction_codes_map import TRANSACTION_CODE_MAP


class ErrorHandler:
    def __init__(self, error: object, main_net: bool = True):
        self.error = error
        self.main_net = main_net

    def get_error(self) -> StellarError:
        """
        Treats the error and returns a stellar error model
        """
        stellar_error = StellarError(main_net=self.main_net)

        error_type = self.error["title"] if "title" in self.error else None
        stellar_error.set_error_type(error_type)

        stellar_error.set_status(
            self.error["status"] if "status" in self.error else None
        )
        stellar_error.set_message(
            self.error["detail"] if "detail" in self.error else None
        )

        error_type = stellar_error.get_error_type()

        if error_type and error_type in RESPONSE_BODY_TYPE:
            return HANDLERS[RESPONSE_BODY_TYPE[error_type]](self.error, stellar_error)
        return HANDLERS["UNKNOWN"](self.error, stellar_error)


def _transaction_failed_(error: object, stellar_error: StellarError) -> StellarError:
    """
    Treats transaction failed error shape and returns a stellar error model
    """
    if "extras" in error and error["extras"]:
        extras = error["extras"]
        tx_result = extras["result_xdr"]

        # Get transaction error codes
        if "result_xdr" in extras:
            try:
                tx_result = TransactionResult.from_xdr(tx_result)
            except Exception as e:
                tx_result = None
                print(e)

            # List the operations performed up to the time of the error in order
            if "result_codes" in extras:
                result_codes = extras["result_codes"]
                if "transaction" in result_codes:
                    stellar_error.set_tx_codes(result_codes["transaction"])
                    stellar_error.set_message(
                        TRANSACTION_CODE_MAP[stellar_error.get_tx_codes()]
                        if stellar_error.get_tx_codes() in TRANSACTION_CODE_MAP
                        else "Untracked error code"
                    )
                if "operations" in result_codes:
                    operations = []
                    for index, operation in enumerate(result_codes["operations"]):
                        op_details = MESSAGES["NO_OPERATION_DETAILS"]
                        if operation in TRANSACTION_CODE_MAP:
                            op_details = TRANSACTION_CODE_MAP[operation]
                        elif tx_result is not None:
                            if hasattr(tx_result, "type"):
                                op_details = (
                                    tx_result.result.results[index]
                                    .tr.type.__str__()
                                    .replace("OperationType.", "")
                                )
                        operation = {
                            "index": index,
                            "code": operation,
                            "detail": op_details,
                        }
                        operations.append(operation)

                        stellar_error.set_operations(operations)

        return stellar_error


def _transaction_malformed_(error: object, stellar_error: StellarError) -> StellarError:
    """
    Treats transaction malformed error shape and returns a stellar error model
    """
    if "extras" in error and error["extras"]:
        extras = error["extras"]
        if "envelope_xdr" in extras:
            try:
                envelope = TransactionEnvelope.from_xdr(extras["envelope_xdr"]).__dict__
                if "v1" in envelope:
                    if hasattr(envelope["v1"], "signatures"):
                        signatures = envelope["v1"].signatures
                        message = {
                            "message": MALFORMED_ERRORS_MESSAGES["BAD_SIGNATURES"],
                            "signatures": [],
                        }
                        for signature in signatures:
                            message["signatures"].append(
                                str(signature.signature.signature)
                            )  # TODO: Convert to string
                            print(signature.signature.signature)
                        stellar_error.set_more_details(message)
            except ValueError as e:
                stellar_error.set_more_details({"envelope": str(e)})
    return stellar_error


def _bad_request_(error: object, stellar_error: StellarError) -> StellarError:
    """
    Treats bad request error shape and returns a stellar error model
    """
    if "extras" in error and error["extras"]:
        extras = error["extras"]
        reason = {}
        if hasattr(extras, "invalid_field"):
            reason["invalid_field"] = extras["invalid_field"]
        if hasattr(extras, "reason"):
            reason["reason"] = extras["reason"]
        stellar_error.set_more_details(reason if reason else None)

    return stellar_error


def _before_history_(error: object, stellar_error: StellarError) -> StellarError:
    return stellar_error


def _stale_history_(error: object, stellar_error: StellarError) -> StellarError:
    return stellar_error


def _timeout_(error: object, stellar_error: StellarError) -> StellarError:
    return stellar_error


def _resource_missing_(error: object, stellar_error: StellarError) -> StellarError:
    return stellar_error


def _unknown_(error: object, stellar_error: StellarError) -> StellarError:
    if stellar_error.get_message() is None:
        stellar_error.set_message("Unknown error")
    stellar_error.set_more_details({"error": error})
    return stellar_error


HANDLERS = {
    "TRANSACTION_FAILED": _transaction_failed_,
    "TRANSACTION_MALFORMED": _transaction_malformed_,
    "BEFORE_HISTORY": _before_history_,
    "STALE_HISTORY": _stale_history_,
    "TIMEOUT": _timeout_,
    "BAD_REQUEST": _bad_request_,
    "RESOURCE_MISSING": _resource_missing_,
    "UNKNOWN": _unknown_,
}
