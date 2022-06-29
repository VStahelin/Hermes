# https://github.com/stellar/new-docs/blob/master/content/api/errors/http-status-codes/horizon-specific/stale-history.mdx

STALE_HISTORY_SHAPE_SAMPLE = {
    "type": "https://stellar.org/horizon-errors/stale_history",
    "title": "Historical DB Is Too Stale",
    "status": 503,
    "detail": "This horizon instance is configured to reject client requests when it can determine that the history database is lagging too far behind the connected instance of stellar-core.  If you operate this server, please ensure that the ingestion system is properly running.",
}
