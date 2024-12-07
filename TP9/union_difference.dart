void main () {
    final setA={8, 2, 3, 1, 4};
  final setB={1, 6, 5, 4};
  // ignore: unused_local_variable
  final intersection= setA.intersection(setB);
  final Union =setA.union(setB);
  print(Union);
  final differenceA =setA.difference(setB);
  print(differenceA);
  final differenceB=setB.difference(setA);
  print(differenceB);
}