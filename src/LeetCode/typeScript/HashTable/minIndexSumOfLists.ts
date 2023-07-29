function minIndex(list1: string[], list2: string[]): string[] {
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


const list1 = ["happy","sad","good"], list2 = ["sad","happy","good"];

// "1"

console.log(minIndex(list1, list2));
