import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      home: Scaffold(
        body: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              CircleAvatar(
                radius: 150.0,
                backgroundColor: const Color.fromARGB(255, 90, 152, 70),
                backgroundImage: NetworkImage(
                    'https://th.bing.com/th/id/R.3c575f7ff4d54a70c2853de961578ab1?rik=1SbUT%2b8mZJ1mNQ&pid=ImgRaw&r=0'),
              ),
              const SizedBox(height: 5), // Add spacing
              const Text(
                'Moss Head',
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center, // Align text center
              ),
            ],
          ),
        ),
        backgroundColor: Colors.teal, // Use Colors.teal
      ),
    );
  }
}
