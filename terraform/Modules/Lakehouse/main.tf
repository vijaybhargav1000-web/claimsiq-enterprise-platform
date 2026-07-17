resource "aws_s3_bucket" "bronze" {
  bucket = "claimsiq-bronze-${random_id.bucket.hex}"
}

resource "aws_s3_bucket" "silver" {
  bucket = "claimsiq-silver-${random_id.bucket.hex}"
}

resource "aws_s3_bucket" "gold" {
  bucket = "claimsiq-gold-${random_id.bucket.hex}"
}

resource "random_id" "bucket" {
  byte_length = 4
}
