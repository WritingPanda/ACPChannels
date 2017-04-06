from channels.routing import route
from presentation.consumers import ws_message


channel_routing = [
    # route("http.request", "presentation.consumers.http_consumer"),
    route("websocket.receive", ws_message),
]
