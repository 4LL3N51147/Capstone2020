function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
      
        reader.onload = function(e) {
            $('#preview').attr('src', e.target.result).width(330).height(330);;
            $('#preview').show();
        }
      
        reader.readAsDataURL(input.files[0]); // convert to base64 string
    }
}
  
$("#imgInput").change(function() {
    $("#previewbox").hide();
    readURL(this);
});

$("#submitButton").click(function (e) {
    e.preventDefault();

    const req = new XMLHttpRequest();
    const baseUrl = "http://127.0.0.1:5000/";

    var formData = new FormData();
    formData.append("myFile", document.getElementById("imgInput").files[0]);
    formData.append("mode", "min");
    req.open("POST", baseUrl);
    
    req.send(formData);
});
