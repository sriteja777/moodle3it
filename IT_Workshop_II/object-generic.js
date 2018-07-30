var ar = ["foo", 2,3]
ar.__proto__ == Array.prototype;
ar.__proto__.__proto__ == Object.prototype;
ar.__proto__.__proto__.__proto__ == null;

ar.__proto__ == Array.prototype
Array.prototype.__proto__ == Object.prototype;
Object.prototype.__proto__ == null;

var str = "hello world";
str.__proto__ == String.prototype;
str.__proto__.__proto__ == Object.prototype;
str.__proto__.__proto__.__proto__ == null;

str.__proto__ == String.prototype
String.prototype.__proto__ == Object.prototype;
Object.prototype.__proto__ == null;

var num = 30;
num.__proto__ == Number.prototype;
num.__proto__.__proto__ == Object.prototype;
num.__proto__.__proto__.__proto__ == null;

num.__proto__ == Number.prototype
Number.prototype.__proto__ == Object.prototype;
Object.prototype.__proto__ == null;

var f = function(){return 3};
f.__proto__ == Function.prototype;
f.__proto__.__proto__ == Object.prototype;
f.__proto__.__proto__.__proto__ == null;

f.__proto__ == Function.prototype
Function.prototype.__proto__ == Object.prototype;
Object.prototype.__proto__ == null;
