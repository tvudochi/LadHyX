// Window load event used just in case window height is dependant upon images
$(window).bind("load", function() {

    // console.log("document"+" "+$(document).outerHeight());
    // console.log("footer"+" "+$("#footer").outerHeight())

    // console.log("Window"+" "+$(window).height())
    console.log("document"+" "+$(document).outerHeight());

    console.log("container before"+" "+$(".container").outerHeight());

    // $(".container").outerHeight(985);
    console.log("container after"+" "+$(".container").outerHeight());

    console.log($(".content").outerHeight()+$("header").outerHeight()+$(".principale").outerHeight()+
        $(".infospratiques").outerHeight());

    // console.log($(".infospratiques").outerHeight());

    // $( window ).resize(function() {
    //     console.log("resize");
    // });


});