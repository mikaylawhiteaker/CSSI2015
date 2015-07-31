var katzDeli = [];

function takeANumber(katzDeli, name){
  katzDeli.push(name);
  console.log("You are number "+katzDeli.length);
}

function nowServing(katzDeli){
  if(katzDeli.length == 0){
    console.log("there is nobody waiting to be served");
  }
  else {
    console.log(katzDeli[0]);
    katzDeli.splice(0,1);
  }
}

function line(katzDeli){
  if(katzDeli.length == 0){
    console.log("there is nobody in line"); 
  }
  else {
    var people = katzDeli.length
    for(var i = 1; i <= people; i++){
      console.log(i + "."+  katzDeli[i-1]);
    }
  }
}
