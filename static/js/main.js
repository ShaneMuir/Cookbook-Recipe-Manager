$(document).ready(function() {
    //Materialize function
    $('select').formSelect();
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    //End of Materialize functions
    
    //My functions
    $('#alert_close').click(function() {
        $("#alert_box").fadeOut("slow", function() {});
    });
    //End of my functions

});
