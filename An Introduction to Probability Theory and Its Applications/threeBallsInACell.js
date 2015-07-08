var abc = 'abc',
    a = 'a',
    b = 'b',
    c = 'c',
    sampleSpace = [ 
      [ abc,, ],
      [ ,abc, ],
      [ ,,abc ],
      [ a+b,c, ],
      [ a+c,b, ],
      [ b+c,a, ],
      [ a+b,,c ],
      [ a+c,,b ],
      [ b+c,,a ],
      [ a,b+c, ],
      [ b,a+c, ],
      [ c,a+b, ],
      [ a,,b+c ],
      [ b,,a+c ],
      [ c,,a+b ],
      [ ,a+b,c ],
      [ ,a+c,b ],
      [ ,b+c,a ],
      [ ,a,b+c ],
      [ ,b,a+c ],
      [ ,c,a+b ],
      [ a,b,c ],
      [ a,c,b ],
      [ b,a,c ],
      [ b,c,a ],
      [ c,a,b ],
      [ c,b,a ]
     ];


// event A: atleast one cell has two or more inhabitants
var eventA = function () {
  return sampleSpace.filter(handleRow);
};

var eventB = function () {
  return sampleSpace.filter(function(e,i,a) {
    if(!!cellEmpty(e,0)) return e;
  });
};

var eventC = function() {
  return sampleSpace.filter(function(e,i,a) {
    if (!cellEmpty(e) && handleRow(e)) return e;
  });
};

var eventCOr = function() {
  return sampleSpace.filter(function(e,i,a) {
    if(cellEmpty(e) || handleRow(e)) return e;
  });
};

var eventD = function () {
  return sampleSpace.filter(function(e,i,a) {
    if (!handleRow(e)) return e; 
  });
};

function handleRow(e) {
  return atleastHasTwo(e[0]) ||
         atleastHasTwo(e[1]) ||
         atleastHasTwo(e[2]) ? 1 : 0;
};

function atleastHasTwo(e) {
  return e ? e.length >= 2 ? true : false : false;
};

function cellEmpty(e,i) {
  return e[i] ? true : false;
}

console.log("Rows with cells that has atleast one element (event A): " + eventA().length);
console.log("Rows with first cells that are not empty (event B): "+ eventB().length);
console.log("Rows that both event A and B occur (event C): "+ eventC().length);
console.log("Rows that event A or B occur: "+ eventCOr().length);
console.log("Rows that event A does not occur (event D): "+ eventD().length);
