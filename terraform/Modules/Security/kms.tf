resource "aws_kms_key" "claimsiq_key" {
  description             = "KMS Key for ClaimsIQ"
  deletion_window_in_days = 7

  tags = {
    Project = "ClaimsIQ"
  }
}
resource "aws_kms_alias" "claimsiq_alias" {
  name          = "alias/claimsiq-key"
  target_key_id = aws_kms_key.claimsiq_key.key_id
}
