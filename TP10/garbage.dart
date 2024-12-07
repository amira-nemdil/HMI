// ignore_for_file: equal_keys_in_map

void main () {
 // ignore: unused_local_variable
 final A =true;
 final treasureMap ={
  'garbage' :"'in the dumpster",
  'glasses':'on your head',
  'gold':'in the cave',
  'gold':'under your mattress',
 };

 final treasureMap2 = {
  'garbage':'in the dumpster',
  'glasses':['on your head'],
  'gold':['in the cave ','under your mattress'],
 };

 print(treasureMap);
 print(treasureMap2);
 }