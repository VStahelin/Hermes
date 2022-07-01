from flask import Flask
from samples.envelope_samples import OPERATIONS as ENVELOPE_SAMPLES
from stellar_sdk import Server

from error_handler import ErrorHandler
from stellar_error_handler import StellarErrorHandler
from tests.samples.result_xdr_samples.bad_request import BAD_REQUEST_SAMPLE
from tests.samples.result_xdr_samples.before_history import BEFORE_HISTORY_SAMPLE
from tests.samples.result_xdr_samples.resource_missing import RESOURCE_MISSING_SAMPLE
from tests.samples.result_xdr_samples.timeout import TIMEOUT_SAMPLE
from tests.samples.result_xdr_samples.transaction_failed import (
    TRANSACTION_FAILED_SAMPLE,
)
from tests.samples.result_xdr_samples.transaction_malformed import (
    TRANSACTION_MALFORMED_SAMPLE,
)
from tests.samples.result_xdr_samples.unknown import UNKNOWN_SAMPLE

app = Flask(__name__)


@app.route("/v1/<int:sample_index>")
def error_tester(sample_index):
    """
    Test the error handler with a sample envelope
    """
    server = Server("https://horizon-testnet.stellar.org")
    try:
        server.submit_transaction(list(ENVELOPE_SAMPLES.values())[sample_index])
        return "Success?"
    except Exception as error:
        response = StellarErrorHandler(stellar_error=error.__dict__, main_net=False)
        return response.json()


@app.route("/v1/")
def list_all_errors():
    """
    Test the error handler with all samples
    """
    server = Server("https://horizon-testnet.stellar.org")
    response = {}
    for sample in ENVELOPE_SAMPLES:
        try:
            server.submit_transaction(ENVELOPE_SAMPLES[sample])
        except Exception as error:
            print(error)
            response[sample] = StellarErrorHandler(
                stellar_error=error.__dict__, main_net=False
            ).json()

    return response


@app.route("/v2/transaction_failed/")
def v2_transaction_failed():
    """
    Test the error handler with all samples
    """
    response = []
    for envelope in TRANSACTION_FAILED_SAMPLE:
        response.append(ErrorHandler(envelope, main_net=False).get_error().as_dict())
    return {"response": response}


@app.route("/v2/transaction_failed/<int:sample_index>")
def v2_transaction_failed_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(TRANSACTION_FAILED_SAMPLE[sample_index], main_net=False)
        .get_error()
        .as_dict()
    )


@app.route("/v2/transaction_malformed/<int:sample_index>")
def v2_transaction_malformed_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(TRANSACTION_MALFORMED_SAMPLE[sample_index], main_net=False)
        .get_error()
        .as_dict()
    )


@app.route("/v2/timeout/<int:sample_index>")
def v2_timeout_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(TIMEOUT_SAMPLE[sample_index], main_net=False).get_error().as_dict()
    )


@app.route("/v2/bad_request/<int:sample_index>")
def v2_bad_request_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(BAD_REQUEST_SAMPLE[sample_index], main_net=False)
        .get_error()
        .as_dict()
    )


@app.route("/v2/before_history/<int:sample_index>")
def v2_before_history_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(BEFORE_HISTORY_SAMPLE[sample_index], main_net=False)
        .get_error()
        .as_dict()
    )


@app.route("/v2/resource_missing/<int:sample_index>")
def v2_resource_missing_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(RESOURCE_MISSING_SAMPLE[sample_index], main_net=False)
        .get_error()
        .as_dict()
    )


@app.route("/v2/unknown/<int:sample_index>")
def v2_unknown_id(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(UNKNOWN_SAMPLE[sample_index], main_net=False).get_error().as_dict()
    )


if __name__ == "__main__":
    app.run(debug=True)
