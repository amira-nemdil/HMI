class Password {
  String _plainText = 'Fares';

  String getPlainText() {
    return _plainText;
  }

  String get plainText => _plainText;

  set plainText(String text) => _plainText = text;
}