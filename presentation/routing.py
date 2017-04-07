from channels.routing import route
from presentation.consumers import http_consumer, ws_message, ws_add, ws_disconnect


http_routing = [
    route("http.request", http_consumer),
]

channel_routing = [
    route("websocket.receive", ws_message),
    route("websocket.connect", ws_add),
    route("websocket.disconnect", ws_disconnect),
]
