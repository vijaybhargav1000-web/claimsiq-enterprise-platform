resource "aws_s3_bucket" "claimsiq_data_lake" {
  bucket = "claimsiq-data-lake-vj-2026"

  tags = {
    Name        = "ClaimsIQ Data Lake"
    Environment = "Development"
  }
}