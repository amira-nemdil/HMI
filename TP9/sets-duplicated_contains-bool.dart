void main() {
  //final Set<int> someSet = {};
  //final someSet2 = <int>{};
  // ignore: equal_elements_in_set
  final anotherSet = {1, 2, 3, 1};
  print(anotherSet);
  final desserts = {'cake', 'pie', 'dount'};
  print(desserts.contains('cake'));//true
  print(desserts.contains('cookies'));//false 
}