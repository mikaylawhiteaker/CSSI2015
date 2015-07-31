$(document).ready(function(){

  $('#bennyimg').click(function(){
    //console.log('work');
    $('#spaceship').fadeIn();
    $('#spaceship').animate({'top': '0px', 'left':'1000px'}, 3000);
    $('#spaceship').fadeOut();
    $('spaceship').stop(true);
  });

  $('#namelink').mouseenter(function(){
    $(this).css('color', 'red');
  });
  $('#namelink').mouseleave(function(){
    $(this).css('color', '#A2D4F5');
  });

  $('#sportslist li:first-child')

});
