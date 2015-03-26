$(function () {

    var $segundo = $('#segundo');
    var $quinto = $('#quinto');
    
    var socket = io.connect('/connection');
    
    socket.on('connect', function (data) {
        console.log('connected')
    });

    $segundo.click(function (event) {
        socket.emit('recive', 'segundo');
    });

    $quinto.click(function (event) {
		socket.emit('recive', 'quinto');
    });

    socket.on('send', function (data) {
        console.log(data);
        $('#lines').append("<p>" + data + "</p>");
    });

});