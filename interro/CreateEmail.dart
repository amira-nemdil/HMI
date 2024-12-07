String createEmailAddress(String username, String? department, String domain) {
  if (department == null || department.isEmpty) {
    return '$username@$domain';
  } else {
    return '$username.$department@$domain';
  }
}

void main() {
  // Examples
  String email1 = createEmailAddress('john.doe', null, 'example.com');
  print(email1); // Output: john.doe@example.com

  String email2 = createEmailAddress('jane.smith', 'sales', 'example.com');
  print(email2); // Output: jane.smith.sales@example.com
}
