// Time Complexity: O(n)
// Space Complexity: O(1)
function isIsomorphic(s: string, t: string): boolean {
  const map: any = {};
  const map1: any = {};

  for(let i = 0; i < s.length; i++) {
    const c1 = s[i];
    const c2 = t[i];

    if( (map[c1] && map[c1] !== c2) || (map1[c2] && map[c2] !== c1)) {

      console.log(map, "-----------", map1);

      return false;
    }

    map[c1] = c2;
    map1[c2] = c1;
    
  }


  return true;
}

console.log(isIsomorphic('badc', 'baba'));
