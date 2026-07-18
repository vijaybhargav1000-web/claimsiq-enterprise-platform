output "glue_role_arn" {
  value = aws_iam_role.glue_role.arn
}

output "kms_key_arn" {
  value = aws_kms_key.claimsiq_key.arn
}
