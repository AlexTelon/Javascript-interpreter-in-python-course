function person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
}
person.prototype.nationality = "English";

var myFather = new person("John", "Doe", 50, "blue");
console.log(myFather.firstName)
console.log(myFather.nationality)
