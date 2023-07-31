function minIndex1(list1: string[], list2: string[]): string[] {
  let n = 10000;
  let obj: any ={} ;


  if(list1.length < list2.length) {
    const temp = list2;
    list2 = list1;
    list1 = temp;
  }

  for(let i = 0; i < list1.length; i++) {
    const item = list1[i];

    if(list2.includes(item)) {
      const index = list2.indexOf(item);

      if(i + index <= n) {
        n = i + index;

        obj[item] = n;
      }
    }
  }

  console.log(obj, ' object ', n);

  const data: string[] = []; 

  for(let key in obj) {
    if(obj[key] === n) {
      data.push(key);
    }
  }

  return data;
}

// Time Complexity: O(l1 + l2);
// Space Complexity: O(l1 * x); hashmap size grows upto l1∗x, where x refers to average string length;

function findMinIndex(list1: string[], list2: string[]): string[] {
  if(list1.length < list2.length) {
    return findMinIndex(list2, list1);
  }

  let minIndex = 10000;
  const map = new Map();
  let result: string[] = [];

  for(let i = 0; i < list1.length; i++) {
    map.set(list1[i], i);
  }


  for(let i = 0; i < list2.length; i++) {
    const word = list2[i];

    if(map.has(word)) {
      const curMinIndex = map.get(word) + i;

      if(curMinIndex < minIndex) {
        minIndex = curMinIndex;

        result = [];

        result.push(word);
      } else if(curMinIndex === minIndex) {
        result.push(word);
      }

    }

  }

  return result; 
}


const list1 = ["happy","ball","good", "basket"], list2 = ["ball","happy","good"];


console.log(findMinIndex(list1, list2));
