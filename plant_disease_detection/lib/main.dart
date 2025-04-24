import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const PlantDiseaseApp());
}

/// Ana uygulama widget'ı
class PlantDiseaseApp extends StatelessWidget {
  const PlantDiseaseApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bitki Hastalık Tespiti',
      theme: ThemeData(
        primarySwatch: Colors.green,
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
} 