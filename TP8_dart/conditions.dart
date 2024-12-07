// Demonstrates conditional statements
void demoConditions() {
  const trafficLight = 'yellow';
  String command;

  if (trafficLight == 'red') {
    command = 'Stop';
  } else if (trafficLight == 'yellow') {
    command = 'Slow down';
  } else if (trafficLight == 'green') {
    command = 'Go';
  } else {
    command = 'INVALID COLOR!';
  }
  print("Traffic light command: $command");

  const animal = 'Adel';
  if (animal == 'Cat' || animal == 'Dog') {
    print('Animal is a house pet.');
  } else {
    print('Animal is the perfekt fluffy cat pet.');
  }
}
void main() {
  demoConditions();
}