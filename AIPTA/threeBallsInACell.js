var assert      = require("assert"),
    sampleSpace = require("./sampleSpace2A")["sampleSpace"];

// event A: atleast one cell has two or more inhabitants
var eventA = function () {
  return sampleSpace.filter(handleRow);
};

var eventB = function () {
  return sampleSpace.filter(function(e,i,a) {
    if(!!cellNotEmpty(e,0)) return e;
  });
};

var eventC = function() {
  return sampleSpace.filter(function(e,i,a) {
    if (!!cellNotEmpty(e, 0) && handleRow(e)) return e;
  });
};

var eventCOr = function() {
  return sampleSpace.filter(function(e,i,a) {
    if(cellNotEmpty(e,0) || handleRow(e)) return e;
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

function cellNotEmpty(e,i) {
  return e[i] ? true : false;
}

console.log(
"Event A: Rows with cells that has atleast one element\n" +
"Event B: Rows with first cells that are not empty\n" + 
"Event C: Rows that both event A and B occur\n" +
"Event COr: Rows that event A or B occur\n" +
"Event D: Rows that event A does not occur");
assert(eventA().length == 21, "Event A should have 21 simple events");
assert(eventB().length == 19, "Event B should have 19 simple events");
assert(eventC().length == 13, "Event C should have 13 simple events");
assert(eventCOr().length == 27, "Event COr should be the whole sample space");
assert(eventD().length == 6, "Event D should have 6 simple events");
