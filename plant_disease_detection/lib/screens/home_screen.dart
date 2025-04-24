import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../services/api_service.dart';

/// Ana ekran widget'ı
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  File? _image;
  String? _result;
  final _apiService = ApiService();
  final _picker = ImagePicker();

  /// Kameradan fotoğraf çekme fonksiyonu
  Future<void> _takePhoto() async {
    try {
      final XFile? photo = await _picker.pickImage(source: ImageSource.camera);
      if (photo != null) {
        setState(() {
          _image = File(photo.path);
          _result = null;
        });
        _analyzeImage();
      }
    } catch (e) {
      _showError('Kamera hatası: $e');
    }
  }

  /// Galeriden fotoğraf seçme fonksiyonu
  Future<void> _pickImage() async {
    try {
      final XFile? image = await _picker.pickImage(source: ImageSource.gallery);
      if (image != null) {
        setState(() {
          _image = File(image.path);
          _result = null;
        });
        _analyzeImage();
      }
    } catch (e) {
      _showError('Galeri hatası: $e');
    }
  }

  /// Görüntüyü analiz etme fonksiyonu
  Future<void> _analyzeImage() async {
    if (_image == null) return;

    try {
      setState(() {
        _result = 'Analiz ediliyor...';
      });

      final result = await _apiService.analyzeImage(_image!);
      setState(() {
        _result = result;
      });
    } catch (e) {
      _showError('Analiz hatası: $e');
    }
  }

  /// Hata mesajı gösterme fonksiyonu
  void _showError(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(message)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Bitki Hastalık Tespiti'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Fotoğraf seçme butonları
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton.icon(
                  onPressed: _takePhoto,
                  icon: const Icon(Icons.camera_alt),
                  label: const Text('Kameradan Çek'),
                ),
                ElevatedButton.icon(
                  onPressed: _pickImage,
                  icon: const Icon(Icons.photo_library),
                  label: const Text('Galeriden Seç'),
                ),
              ],
            ),
            const SizedBox(height: 20),
            
            // Seçilen görüntü
            if (_image != null) ...[
              ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: Image.file(
                  _image!,
                  height: 300,
                  fit: BoxFit.cover,
                ),
              ),
              const SizedBox(height: 20),
            ],
            
            // Analiz sonucu
            if (_result != null)
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Text(
                    _result!,
                    style: Theme.of(context).textTheme.titleMedium,
                    textAlign: TextAlign.center,
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
} 