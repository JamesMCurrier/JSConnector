var ws = new WebSocket("ws://localhost:5555/");

ws.onmessage = function (event) {
    msgs = JSON.parse(event.data);
    document.getElementById("result").innerHTML = msgs;
}
