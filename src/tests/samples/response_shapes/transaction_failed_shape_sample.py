# https://github.com/stellar/new-docs/blob/master/content/api/errors/http-status-codes/horizon-specific/transaction-failed.mdx

TRANSACTION_FAILED_SHAPE_SAMPLE = {
    "type": "https://stellar.org/horizon-errors/transaction_failed",
    "title": "Transaction Failed",
    "status": 400,
    "detail": "The transaction failed when submitted to the stellar network. The `extras.result_codes` field on this response contains further details.  Descriptions of each code can be found at: https://www.stellar.org/developers/learn/concepts/list-of-operations.html",
    "extras": {
        "envelope_xdr": "AAAAANPRjCD1iCti3hovsrrz6aSAjmp263grVr6+mI3SQSkcAAAAZAAPRLgAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAArki/TnIipBc7Y+Hd87mnZdtBxzm7vu6iXpwcRz6zGskAAAAAAAAAAAAHoSAAAAAAAAAAAdJBKRwAAABANWeKuRYFmBm1lrMQqMvhbSouwL270SnxcTtv1XI4Y+uVe4yw4Jq7/43EoxwLbRh/pC3V4WfOZRzDqwsTyEztAA==",
        "result_codes": {"transaction": "tx_bad_seq"},
        "result_xdr": "AAAAAAAAAAD////7AAAAAA==",
    },
}
