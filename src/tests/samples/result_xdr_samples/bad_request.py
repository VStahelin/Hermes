BAD_REQUEST_SAMPLE = [
    {
        "type": "https://stellar.org/horizon-errors/bad_request",
        "title": "Bad Request",
        "status": 400,
        "detail": "The request you sent was invalid in some way.",
        "extras": {
            "invalid_field": "account_id",
            "reason": "Account ID must start with `G` and contain 56 alphanum characters",
        },
    },
]
