import { MyHashSet } from './HashSet1'

function findDuplicates(keys: number[]) {
  const Set = new MyHashSet(keys.length);

  for(const key of keys) {
    if(Set.contains(key)) {
      return true;
    }

    Set.add(key);
  }

  return false;
}


console.log("Duplicated values: ",  findDuplicates([1,2,3,4,5,1]));
