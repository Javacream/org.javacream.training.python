let boardSocket

document.querySelector('#send-echo').onclick = function(e) {
    boardSocket.send("Hello WebSocket " + new Date());
}
document.querySelector('#connect').onclick = function(e) {
    boardSocket=new WebSocket('ws://localhost:8000/ws/echo/');
    boardSocket.onmessage = function(e) {
        document.querySelector('#echo-log').value = e.data;
    };
    boardSocket.onclose = function(e) {
        console.error('Socket closed');
    };
    }
document.querySelector('#disconnect').onclick = function(e) {
    boardSocket.close();
}
