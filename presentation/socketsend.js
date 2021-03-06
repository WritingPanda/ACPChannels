// Note that the path does not matter for routing; any WebSocket
// connection gets bumped over to WebSocket consumers

socket = new WebSocket("ws://" + window.location.host + "/chat/");

socket.onmessage = function(e) {
    alert(e.data);
}

socket.onopen = function() {
    socket.send("Hello world!");
}

// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();