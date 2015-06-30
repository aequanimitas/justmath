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

var ssLen = sampleSpace.length;

console.log(exists(sampleSpace[ 0 ][ 0 ], 'd'));

function exists(ss, ch) {
  var exists = ss.indexOf(ch) !== -1; 
  return exists;
};
