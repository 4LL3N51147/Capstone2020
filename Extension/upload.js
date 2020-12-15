function previewImg(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
      
        reader.onload = function(e) {
            preview_img = $('#preview');
            preview_img.attr('src', e.target.result).width(300).height(300);
            $('#previewbox').html(preview_img);
            preview_img.show();
        }
      
        reader.readAsDataURL(input.files[0]); // convert to base64 string
    }
}
  
$("#imgInput").change(function() {
    previewImg(this);
});

$("#submitButton").click(function (e) {
    e.preventDefault();

    const req = new XMLHttpRequest();

    req.onload = () => {
        base64_src = "data:image/jpeg;charset=utf-8;base64," + req.response;
        result_img = $('#result');
        result_img.attr('src', base64_src).width(300).height(300);
        $('#resultbox').html(result_img);
        result_img.show();
    };

    const baseUrl = "http://127.0.0.1:5000/";

    var formData = new FormData();
    // get the selected file from the file select input and add it to the formdata
    formData.append("file", $("#imgInput").prop('files')[0]);
    // get the selected cloaking mode and add it to the formdata
    formData.append("mode", $("input[name=mode]:checked").val());
    // send the constructed post request to our server
    req.open("POST", baseUrl);
    
    req.send(formData);
});