from elasticsearch import Elasticsearch

# you can use RFC-1738 to specify the url
es = Elasticsearch(['https://elastic:Kt0gJjnP@elasticsearch-4570-0.tripanels.com:4608'])

# ... or specify common parameters as kwargs

es2 = Elasticsearch(
    ['https://elasticsearch-4570-0.tripanels.com:4608'],
    http_auth=('elastic', 'Kt0gJjnP'),
    scheme="https",
    port=443,
)

# # SSL client authentication using client_cert and client_key
#
from ssl import create_default_context
#
context = create_default_context(cafile="./ca.crt")
es3 = Elasticsearch(
    ['https://elasticsearch-4570-0.tripanels.com:4608',],
    http_auth=('elastic', 'Kt0gJjnP'),
    scheme="https",
    port=443,
    ssl_context=context,
)

print(es3.indices.get_alias("*"))