# https://github.com/stellar/new-docs/blob/master/content/api/errors/http-status-codes/horizon-specific/transaction-malformed.mdx

TRANSACTION_MALFORMED_SHAPE_SAMPLE = {
    "type": "https://stellar.org/horizon-errors/transaction_malformed",
    "title": "Transaction Malformed",
    "status": 400,
    "detail": "Horizon could not decode the transaction envelope in this request. A transaction should be an XDR TransactionEnvelope struct encoded using base64.  The envelope read from this request is echoed in the `extras.envelope_xdr` field of this response for your convenience.",
    "extras": {
        "envelope_xdr": "BBBBBPORy3CoX6ox2ilbeiVjBA5WlpCSZRcjZ7VE9Wf4QVk7AAAAZAAAQz0AAAACAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAA85HLcKhfqjHaKVt6JWMEDlaWkJJlFyNntUT1Z/hBWTsAAAAAAAAAAAL68IAAAAAAAAAAARN17BEAAABAA9Ad7OKc7y60NT/JuobaHOfmuq8KbZqcV6G/es94u9yT84fi0aI7tJsFMOyy8cZ4meY3Nn908OU+KfRWV40UCw=="
    },
}
