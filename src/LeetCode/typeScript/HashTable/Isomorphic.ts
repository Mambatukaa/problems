// Time Complexity: O(n)
// Space Complexity: O(1)
function isIsomorphic1(s: string, t: string): boolean {
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

function isIsomorphic2(s: string, t: string): boolean {
  const mapST = new Map();
  const mapTS = new Map();


  for(let i = 0; i < s.length; i++) {
    const c1 = s[i];
    const c2 = t[i];

    if((mapST.has(c1) && mapST.get(c1) !== c2) || (mapTS.has(c2) && mapTS.get(c2) !== c1)) {
      return false;
    }

    mapST.set(c1, c2);
    mapTS.set(c2, c1);
  }


  return true;
}

function isIsomorphic(s: string, t: string) {
    for (let i = 0; i < s.length; i++) {
      console.log(s.indexOf(s[i]), ' ------------------------ ', t.indexOf(t[i]));

      if (s.indexOf(s[i]) !== t.indexOf(t[i])) return false

    }

    return true;
}

console.log(isIsomorphic('fooso', 'baaos'));
console.log(isIsomorphic('badc', 'baba'));
