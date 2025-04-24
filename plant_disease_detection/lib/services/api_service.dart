import 'dart:io';
import 'package:http/http.dart' as http;

/// API servis sınıfı
class ApiService {
  /// Backend API endpoint'i
  static const String _baseUrl = 'http://10.0.2.2:5000';
  
  /// Görüntü analizi için API çağrısı yapar
  /// 
  /// [image] analiz edilecek görüntü dosyası
  /// 
  /// Returns:
  ///   String: Analiz sonucu
  Future<String> analyzeImage(File image) async {
    try {
      // Multipart request oluştur
      var request = http.MultipartRequest(
        'POST',
        Uri.parse('$_baseUrl/analyze'),
      );

      // Görüntü dosyasını ekle
      request.files.add(
        await http.MultipartFile.fromPath(
          'image',
          image.path,
        ),
      );

      // İsteği gönder ve yanıtı al
      var response = await request.send();
      var responseData = await response.stream.bytesToString();

      if (response.statusCode == 200) {
        // TODO: JSON yanıtını parse et ve result alanını döndür
        return responseData;
      } else {
        throw Exception('Sunucu hatası: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('API hatası: $e');
    }
  }
} 