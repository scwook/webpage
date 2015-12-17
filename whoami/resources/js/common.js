$(document).ready(function() {
  $(".de_side").hover(function() {
    $(".de_menu").stop().animate({"opacity":1});
    $(".de_menu").css("display","block");
   }, function() {
          $(".de_menu").stop().animate({"opacity":0});
          $(".de_menu").css("display","none");
     });
  
  $(".ep_side").hover(function() {
    $(".ep_menu").stop().animate({"opacity":1});
    $(".ep_menu").css("display","block");
   }, function() {
          $(".ep_menu").stop().animate({"opacity":0});
          $(".ep_menu").css("display","none");
     });

  $(".ra_side").hover(function() {
    $(".ra_menu").stop().animate({"opacity":1});
    $(".ra_menu").css("display","block");
   }, function() {
          $(".ra_menu").stop().animate({"opacity":0});
          $(".ra_menu").css("display","none");
     });

  $(".ht_side").hover(function() {
    $(".ht_menu").stop().animate({"opacity":1});
    $(".ht_menu").css("display","block");
   }, function() {
          $(".ht_menu").stop().animate({"opacity":0});
          $(".ht_menu").css("display","none");
     });

  $(".ja_side").hover(function() {
    $(".ja_menu").stop().animate({"opacity":1});
    $(".ja_menu").css("display","block");
   }, function() {
          $(".ja_menu").stop().animate({"opacity":0});
          $(".ja_menu").css("display","none");
     });


  $('.menu').click(function() {
    var navPosition = $(this).attr('data-position');
    $('nav.' + navPosition + '').addClass('open');
    $('body').addClass('menu-open');
    return false;
    });

});
