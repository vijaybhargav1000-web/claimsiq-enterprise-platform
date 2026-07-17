/*
output "kinesis_name" {
  value = aws_kinesis_stream.claim_stream.name
}
*/

output "lambda_role" {
  value = aws_iam_role.lambda_role.arn
}
