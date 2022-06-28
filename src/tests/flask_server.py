from flask import Flask
from samples.envelope_samples import OPERATIONS as ENVELOPE_SAMPLES
from stellar_sdk import Server

from stellar_error_handler import StellarErrorHandler

app = Flask(__name__)


@app.route("/")
def error_tester():
    server = Server("https://horizon-testnet.stellar.org")
    try:
        server.submit_transaction(ENVELOPE_SAMPLES["signature_error"])
        return "Success?"
    except Exception as error:
        response = StellarErrorHandler(stellar_error=error.__dict__, main_net=False)
        return response.json()


if __name__ == "__main__":
    app.run(debug=True)
