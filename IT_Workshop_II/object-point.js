

//define a constructor
function Point(x, y){
   this.x =x;
   this.y= y;
 }
   
var pt = new Point(2,3)

pt.constructor === Point;

pt.z === undefined;
  
// add field z  to Point's prototype object
Point.prototype.z = 10;

// pt inherits the field z
pt.z === 10;

// pt doesn't own z; it inherits it
pt.hasOwnProperty('z') === false;
Point.prototype.hasOwnProperty('z') === true;
pt.constructor.prototype.hasOwnProperty('z') === true;
Point.hasOwnProperty('z') === false;

//adding field to constructor does not affect the children
Point.w = 20;
pt.w === undefined;

//inner property __proto__ set to the prototype object
pt.__proto__ == pt.constructor.prototype;
pt.__proto__.__proto__ == Object.prototype;
pt.__proto__.__proto__.__proto__ == null;
