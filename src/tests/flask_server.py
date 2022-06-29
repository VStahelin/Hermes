from flask import Flask
from samples.envelope_samples import OPERATIONS as ENVELOPE_SAMPLES
from stellar_sdk import Server

from stellar_error_handler import StellarErrorHandler

app = Flask(__name__)


@app.route("/<int:sample_index>")
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


@app.route("/")
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
            response[sample] = StellarErrorHandler(
                stellar_error=error.__dict__, main_net=False
            ).json()

    return response


if __name__ == "__main__":
    app.run(debug=True)
