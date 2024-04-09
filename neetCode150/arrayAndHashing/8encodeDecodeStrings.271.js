// Time Complexity: O(n)
// Space Complexity: O(n)
// 10 minutes
const encode = (strs) => {
  return strs.join(" ");
};

const decode = (s) => {

  return s.split(" ");
};

const arr =["Hello", "World!"]; 

const str = encode(arr);
console.log(str)

const strs = decode(str);



console.log(arr)
console.log(strs)


console.log('=============');


class Encoder {
  encode(strs) {
    let string = "";
    for(const str of strs) {
      string += String(str.length) + "#" + str;
    };

    return string;
  };

  decode(str) {
    // 5#Hello6#Wor#d!
    
    const answer = [];
    const strs = str.split("");

    let i = 0;

    while(i < strs.length) {
      let j = i;

      while(strs[j] !== "#") {
        j++;
      };


      const length = Number(strs[i]);
      const end = j + 1 + length;

      answer.push(str.slice(j + 1, end));

      i = end;
    };

    return answer;
  };
};


const encoder = new Encoder();

const str1 = encoder.encode(["Hello", "Wor#d!"]);

console.log(str1)

console.log(encoder.decode(str1))
