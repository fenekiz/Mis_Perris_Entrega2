       
function openNav() {
    document.getElementById("myObjeto").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("myObjeto").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}

var elementTop = $('.nav').offset().top;

$(window).scroll(function(){
    if($(window).scrollTop() >= elementTop){
        $('body').addClass('nav_fixed');
    }else{
        $('body').removeClass('nav_fixed');
    }
})

$('.btn-menu').on('click',function(){
    $('.nav').toggleClass('nav-toggle');
})



