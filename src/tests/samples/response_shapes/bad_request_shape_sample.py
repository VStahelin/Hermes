# https://github.com/stellar/new-docs/blob/master/content/api/errors/http-status-codes/standard.mdx

BAD_REQUEST_SHAPE_SAMPLE = {
    "type": "https://stellar.org/horizon-errors/bad_request",
    "title": "Bad Request",
    "status": 400,
    "detail": "The request you sent was invalid in some way",
    "extras": {"invalid_field": "limit", "reason": "unparseable value"},
}
