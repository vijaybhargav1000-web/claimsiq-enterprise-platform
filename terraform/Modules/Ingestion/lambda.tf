/*
resource "aws_lambda_function" "claim_processor" {
  function_name = "ClaimsIQ-Processor"

  role    = aws_iam_role.lambda_role.arn
  handler = "index.handler"
  runtime = "python3.12"

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")
}
*/