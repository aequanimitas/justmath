var count = 0;
for (var x = 0; x < 101; x += 1) {
  for (var y = 0; y < 101; y += 1) {
    for (var a = 0; a < 101; a += 1) {
      for (var b = 0; b < 101; b += 1) {
        if ((x + y + a + b) == 100) { count += 1 }
      }
    }
  }
}

console.log(count);
