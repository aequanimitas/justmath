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
  var cellCount = 0;
  sampleSpace.forEach(function(e,i,a) {
    cellCount += handleRow(e) ? 1 : 0;
  });
  return cellCount;
};

var eventB = function () {
  var cellCount = 0;
  sampleSpace.forEach(function(e,i,a) {
    cellCount += firstCellEmpty(e) ? 1 : 0;
  });
  return cellCount;
};

var eventC = function () {
  var cellCount = 0;
  sampleSpace.forEach(function(e,i,a) {
    cellCount += firstCellEmpty(e) && handleRow(e) ? 1 : 0;
  });
  return cellCount;
};

var eventCOr = function () {
  var cellCount = 0;
  sampleSpace.forEach(function(e,i,a) {
    cellCount += firstCellEmpty(e) || handleRow(e) ? 1 : 0;
  });
  return cellCount;
};

var eventD = function () {
  var cellCount = 0;
  sampleSpace.forEach(function(e,i,a) {
    cellCount += !handleRow(e) ? 1 : 0;
  });
  return cellCount;
};

function handleRow(e) {
  return atleastHasTwo(e[0]) ||
         atleastHasTwo(e[1]) ||
         atleastHasTwo(e[2]) ? 1 : 0;
};

function atleastHasTwo(e) {
  return e ? e.length >= 2 ? true : false : false;
};

function firstCellEmpty(e) {
  return e[0] ? true : false;
}

console.log("Rows with cells that has atleast one element: "+ eventA());
console.log("Rows with first cells that are not empty: "+ eventB());
console.log("Rows that both event A and B occur: "+ eventC());
console.log("Rows that event A or B occur: "+ eventCOr());
console.log("Rows that event A does not occur: "+ eventD());
