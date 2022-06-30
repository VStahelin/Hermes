from flask import Flask
from samples.envelope_samples import OPERATIONS as ENVELOPE_SAMPLES
from stellar_sdk import Server

from error_handler import ErrorHandler
from stellar_error_handler import StellarErrorHandler
from tests.samples.result_xdr_samples.transaction_failed import (
    TRANSACTION_FAILED_SAMPLE,
)

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
def list_all_errors_v2():
    """
    Test the error handler with all samples
    """
    response = []
    for envelope in TRANSACTION_FAILED_SAMPLE:
        response.append(ErrorHandler(envelope, main_net=False).get_error().as_dict())
    return {"response": response}


@app.route("/v2/transaction_failed/<int:sample_index>")
def error_tester_v2(sample_index):
    """
    Test the error handler with a sample envelope
    """
    return (
        ErrorHandler(TRANSACTION_FAILED_SAMPLE[sample_index - 1], main_net=False)
        .get_error()
        .as_dict()
    )


if __name__ == "__main__":
    app.run(debug=True)
