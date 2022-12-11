var post_to_delete = ''
$(document).on("click", "#myBtn", function (event) {
    post_to_delete = $(this).attr("post_id");

  $("#myModal").modal('toggle');
    //$(".col").load(" .col");

});


function mujheMaaro(){
    
    //var post_to_delete = $(this).attr("item_id");
    console.log(post_to_delete)
    $.ajax({
      url: "delete",
      type: "GET",
      data: {
        post_to_delete: post_to_delete,
      },
      success: function (json) {
        //post_to_delete = ''
        console.log(json);
        console.log("success");
        var meriDiv = document.getElementById(post_to_delete);
        console.log(post_to_delete.type)
        meriDiv.parentNode.removeChild(meriDiv);
        //$("#myModal").modal("hide");
        //$("main").load(" main");


        //$('.col').load(' .col', function(){$(this).children().unwrap()})
      },
      error: function (xhr, errmsg, err) {
        $("#results").html(
          "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
            errmsg +
            " <a href='#' class='close'>&times;</a></div>"
        ); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      },
    });
}

function edoTensei(){
    mujheMaaro();

}

/*
$('#yes_button').on("click", function (event) {
    console.log('Something clicked.')
  event.preventDefault();
  var post_to_delete = $(this).attr("item_id");
  $.ajax({
    url: "delete",
    type: "GET",
    data: {
      post_to_delete: post_to_delete,
    },
    success: function (json) {
      //post_to_delete = ''
      console.log(json);
      console.log("success");
      $(".col").load(" .col");
      //$('#tag_cloud').load(' #tag_cloud', function(){$(this).children().unwrap()})
    },
    error: function (xhr, errmsg, err) {
      $("#results").html(
        "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
          errmsg +
          " <a href='#' class='close'>&times;</a></div>"
      ); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    },
  });
});
*/
