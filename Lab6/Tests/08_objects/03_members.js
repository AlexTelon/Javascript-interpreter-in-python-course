var car = {type:"Fiat", model:500, color:"white", changeColor: function(val) { this.color = val; } };
console.log(car.color)
car.changeColor("green")
console.log(car.color)

car.changeType = function(val) { this.type = val; }
console.log(car.type)
car.changeType("Peugeot")
console.log(car.type)
