// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (text) => {
  let bCounter = 0, aCounter = 0, lCounter = 0, oCounter = 0, nCounter = 0;

  for(const ch of text) {
    switch(ch) {
      case 'b':
        bCounter++;
        break;
      case 'a':
        aCounter++;
        break;
      case 'l':
        lCounter++;
        break;
      case 'o':
        oCounter++;
        break;
      case 'n':
        nCounter++;
        break;
    };
  };

  // they must be at least 2
  oCounter /= 2;
  lCounter /= 2;

  return Math.floor(Math.min(bCounter, aCounter, lCounter, oCounter, nCounter));
};

// Time Complexity: O(n)
// Space Complexity: O(n)
// Naive
const fnII = () => {
  const map = new Map();
    const keyword = "balloon";

    for(const letter of text) {
        map.set(letter, (map.get(letter) || 0) + 1)
    };
    
    let idx = 0;
    let counter = 0;

    console.log(map)

    while(true) {
        idx = idx % (keyword.length);
  
        if(map.get(keyword[idx]) > 0) {
            map.set(keyword[idx], map.get(keyword[idx]) - 1);
            idx++;
        } else {
            return counter;
        }

         if(idx === 7) {
            counter++;
        }

    };

};

const text = "balon";

console.log(fn(text));
