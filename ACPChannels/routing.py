from channels.routing import route


channel_routing = [
    route("http.request", "presentation.consumers.http_consumer"),
]
