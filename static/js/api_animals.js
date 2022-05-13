$( document ).ready(function() {
    $("#trigger_api").click(function () {
        $.ajax({
            type: "GET",
            url: "https://zoo-animal-api.herokuapp.com/animals/rand/",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (data) {
                $('#id_name').val(data.name);
            }
        })
    });
});
