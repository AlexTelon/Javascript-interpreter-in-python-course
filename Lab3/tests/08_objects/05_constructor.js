function person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
    this.fullname = function() { return this.firstName + " " + this.lastName }
}
var myFather = new person("John", "Doe", 50, "blue");
var myMother = new person("Sally", "Rally", 48, "green");

console.log(myFather.firstName)
console.log(myMother.eyeColor)
console.log(myFather.fullname())
console.log(myMother.fullname())
