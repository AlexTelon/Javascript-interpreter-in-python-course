var Base = function(x) {
  this.x = x;
  this.propInSuper = 'hello im propInSuper';
}

Base.prototype = {
  getX : function(){
    console.log(this.x);
  }
}

var Child = function(x){
  Base.call(this, x);
}

Child.prototype = Object.create(Base.prototype);

//@override
Child.prototype.getX = function(){
  console.log(this.x * 2);
}

var base = new Base(2)
base.getX()
console.log(base.propInSuper);

var child = new Child(5);
child.getX();

console.log(child.propInSuper);
