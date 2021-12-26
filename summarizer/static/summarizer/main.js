var btnSummary = document.querySelector("#btn-summary");
var txtInput = document.querySelector("#txtInput");
var outputDiv = document.querySelector("#output");

$("#myClickButton").click(function() {
    $.get("/output/", function(data) {
        $("#myOutput").html(data);
    }, "html");
});

$(btnSummary).click(function(){
    var inputText = txtInput.value;
    $.get("/output/", function(inputText){
        $(outputDiv).innerText(data);
    },"html");
});


btnTranslate.addEventListener("click", ClickHandler);

function ClickHandler()
{
    var inputText = txtInput.value;
}