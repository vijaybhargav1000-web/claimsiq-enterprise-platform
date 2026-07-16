provider "aws" {
  region = "ap-south-1"

  default_tags {
    tags = {
      Project     = "ClaimsIQ"
      Environment = "Development"
      Owner       = "VJ"
      ManagedBy   = "Terraform"
    }
  }
}