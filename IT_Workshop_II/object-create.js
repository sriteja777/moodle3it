var Person = function(name, id){
    this.name = name;
    this.id = id;
}

var Student = function(name, id, program){
    Person.call(this, name, id);
    this.program = program;
}

var TStudent = function(name, id, program, subject){
     Student.call(this, name, id, program);
     this.subject  = subject;
}

var a = new Person("person", 1);
var b = new Student("student", 2, "CS");
var c = new TStudent("Tstudent", 3, "CS", "ITW2");

a.constructor.prototype.a1 = "newly added prop a1 to object of type Person";
b.a1 == undefined;
c.a1 == undefined;

//now chain the prototypes using Object.create which returns an empty object
// with [[prototype]] or __proto__ set to object passed in.
// note: constructor property is erased and needs to be reset

Student.prototype = Object.create(Person.prototype); // returns {__proto__: Person.prototype}
TStudent.prototype = Object. create(Student.prototype); // returns {__proto__: Student.prototype} 

Student.prototype.constructor = Student; // {__proto__: Person.prototype, constructor:Student}
TStudent.prototype.constructor = TStudent; //{__proto__: Student.prototype, constructor:TStudent}

var a = new Person("person", 1);
var b = new Student("student", 2, "CS");
var c = new TStudent("Tstudent", 3, "CS", "ITW2");

a.constructor.prototype.a2 = "newly added prop a2 to object of type Person";
b.a2 == a.constructor.prototype.a2;
c.a2 == a.constructor.prototype.a2;
