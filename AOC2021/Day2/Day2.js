
var regexp = [];
var fs = require("fs");
var data = fs.readFileSync("input.txt", "utf8");
data = data.trim();
regexp = data.split(/\n/);

// convertir en string
for (let i = 0; i < regexp.length; i++) {
    let str = regexp[i];
    str = String(str);
    regexp[i] = str;
}
function day2part1(input) {
    //créer l'object
    var obj = {
    forward: 0,
    down: 0,
    up: 0,
};

for (let i = 0; i < input.length; i++) {
    let str = input[i];
    let str2 = str.split(" ");
    let key = str2[0];
    let num = Number(str2[1]);
    obj[key] += num;
}
    // calculer la distance totale de l'objet
return obj.forward * Math.abs(obj.down - obj.up);
}

// part 1
console.log(day2part1(regexp));
function day2part2(input) {
    let obj3 = { h: 0, aim: 0, d: 0 };
    for (let i = 0; i < input.length; i++) {
    let str = input[i];
    let str2 = str.split(" ");
    let key = str2[0];
    let num = Number(str2[1]);
        if (key == "forward") {
        cf(num, obj3);
        } else if (key == "down") {
        cd(num, obj3);
        } else if (key == "up") {
        cu(num, obj3);
        }
    }
return obj3.h * obj3.d;
}
function cf(x, object) {
    let ph = object.h + x;
    let pd = object.d;
    let d = pd + object.aim * x;
    // return { ph, d };
    object.h = ph;
    object.d = d;
}

// part 2
console.log(day2part2(regexp));
function cd(x, object) {
    object.aim = object.aim + x;
}
function cu(x, object) {
    object.aim = object.aim - x;
}