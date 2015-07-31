


function checkout(item1, item2, coupon){
  var subtotal = item1 + item2;
  subtotal = subtotal * (1-coupon);
  var total = subtotal * 1.095;

  total = Math.round(total/ 100)*100

  return total;
}

function gotolunch(name){
  alert("lunch time!");
  alert("close your computer, " + name );
  console.log("lets eat food");


}

function roll(){
  var x = Math.floor(Math.random()*6)+1;

  return x;


}

function roll2numbers(){
  console.log(roll());
  console.log(roll());
}

function howamidoing(gpa, isfootballplayer, needtogetintogradschool){
  if (gpa >= 4.0){
    alert("I am so smart");
  }
  else if (gpa >= 3.0 || !needtogetintogradschool) {
    console.log("better get a job");
  }
  else if (gpa >=3.0) {
    alert("not to shabby");
  }
  else if (isfootballplayer == true) {
    alert("Im happy either way");

  }
  else{
  alert("crap better study");
  }
}



    var numbers = [2, 3, 5, 7, 11, 13, 17, 23];
    var i = 0;
    while(i < numbers.length){
      numbers[i] = numbers[i] + 1;
      i = i + 1;
    }

    function multbytwo(arr){
      /*
      var i = 0;
      while(i < arr.length){
        arr[i] = arr[i] * 2;
        i = i + 1;

      }
      */
      for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * 42
      }

      console.log(arr);


    }
