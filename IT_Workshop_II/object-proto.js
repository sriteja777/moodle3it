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

a.constructor.prototype.prop1 = "newly added prop a1 to object of type Person";
b.prop1 == undefined;
c.prop1 == undefined;

//chain the prototypes method1

Student.prototype.__proto__ = Person.prototype;
TStudent.prototype.__proto__ = Student.prototype;

//prop1 is now available to b and c objects

b.prop1 == a.constructor.prototype.prop1;
c.prop1 == a.constructor.prototype.prop1;
