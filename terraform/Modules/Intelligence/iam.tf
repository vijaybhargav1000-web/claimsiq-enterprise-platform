resource "aws_iam_role" "step_role" {
  name = "ClaimsIQ-StepFunctions-Role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "states.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}
