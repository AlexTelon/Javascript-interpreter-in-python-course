
function person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}

Object.defineProperty(person.prototype, 'fullname', {get: function() { return this.firstName + " " + this.lastName; }, set: function(value) { console.log("Unable to set full name!")} } )

var myFather = new person("John", "Doe", 50, "blue");
console.log(myFather.fullname)
myFather.fullname = "John Doe"
