document.getElementById("long_url").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("submit").click();
    }
});
$('#submit').click(function(){
    var url = $('#long_url').val();
    if (!url){
        return
    }
    $.get("/encode_url?url=" + encodeURIComponent(url))
        .done(function(data, status){
            $('#result').empty();
            $("#error").css("display","none");
            $("#result").css("display","block");
            $('#long_url').empty();
            $('#result').text(data.shortUrl);
        })
        .fail(function(data, status, errorThrown){
            $('#error').empty();
            $("#result").css("display","none");
            $("#error").css("display","block");
            $('#error').text(JSON.parse(data.responseText).detail);
        })
})