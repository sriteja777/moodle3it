///////////////////////////// this is what is passed to the function at run time /////////////////////////////////
function Person(){
  this.age = 0;

  setTimeout(function() {
    this.age += 10; // |this| properly refers to the ? object
    console.log("normal function: " + this.age); 
  }, 2000);
}

/////////////////////////// this points to the person object ////////////////////////////////////////////
function PersonArrow(){
  this.age = 0;

  setTimeout(() => {
    this.age += 10; // |this| properly refers to the person object
    console.log("using arrow function: " + this.age); 
  }, 2000);
}

var p = new Person();
var p2 = new PersonArrow();
