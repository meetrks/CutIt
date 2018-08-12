document.getElementById("long_url").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("submit").click();
    }
});
document.getElementById('submit').onclick = function(){
    document.getElementById('msg').style.display = "none";
    var url = document.getElementById('long_url').value;
    if (!url){
        return
    }
    var result_btn = document.getElementById('result');
    var error_btn = document.getElementById('error');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        var resp = {
            detail: "Something went wrong"
        };
        if (this.responseText){
            var resp = JSON.parse(this.responseText);
        }
        if (this.readyState == 4 && this.status == 200) {
            error_btn.style.display = "none";
            result_btn.style.display = "block";
            result_btn.value = resp.shortUrl;
        }else{
            result_btn.style.display = "none";
            error_btn.style.display = "block";
            error_btn.innerHTML = resp.detail;
        }
    };
    xhttp.open("GET", "/encode_url?url=" + encodeURIComponent(url), false);
    xhttp.send();
}
document.getElementById('result').onclick = function(){
    var text = document.getElementById("result");
    text.select();
    document.execCommand("copy");
    document.getElementById('msg').style.display = "block";
    document.getElementById('msg').innerHTML = "Text copied on clipboard: " + text.value;
}