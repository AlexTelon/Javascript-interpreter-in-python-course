// Detta berör eg även for, do. Det räcker att ni
// funderar ut en lösning här.

// Det är inte OK att införa en till stack _i Executor_
// Däremot kan det vara värt att fundera på nästling.


var i = 0;
try {
    while(i < 3) {
	if (i == 3) {
	    break;
	}
	i = i + 1
	console.log(i);   
	throw "What just happen?"; 
    }
} catch (e) {
    console.log(e);
}
