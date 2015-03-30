$( document ).ready(function() {
    $("#1.content").addClass("active");
    $("#1.mailSubject").addClass("active");

    activeChange(1);
    activeChangeForType(1, "html");

    function showAndHide(whatToToggle){
      $("."+whatToToggle).hide();
      $("."+whatToToggle+".active").show();
    }

    function activeChange(id){
      $("div.content").removeClass("active");
      $("a.mailSubject").removeClass("active");
      $("div#"+id+".content").addClass("active");
      $("a#"+id+".mailSubject").addClass("active");
      showAndHide("content");
    }

    function activeChangeForType(id, type){
      $(".mail").removeClass("active");
      $("."+type).addClass("active");
      showAndHide("mail");
    }

    $("a.mailSubject").click(function(){
      activeID = $(this).attr("id");
      activeChange(activeID);
    });

    $("#htmlActivation").click(function(){
      $("#textActivation").removeClass('active');
      $(this).addClass('active');

      activeID = $("div.content.active").attr("id");
      type = "html";
      activeChangeForType(activeID, type);
    });

    $("#textActivation").click(function(){
      $("#htmlActivation").removeClass('active');
      $(this).addClass('active');

      activeID = $("div.content.active").attr("id");
      type = "text";
      activeChangeForType(activeID, type);
    });

    $("a#delete").click(function(){
      var id = $("a.mailSubject.active").data("id");
      $("a.mailSubject.active").remove();
      activeChange($("a.mailSubject").first().attr("id"));
      var fireBaseRef = new Firebase("https://parseapi.firebaseio.com/mails/"+id);
      fireBaseRef.remove();
    });
  });