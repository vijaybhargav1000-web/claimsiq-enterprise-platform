resource "aws_sfn_state_machine" "claim_workflow" {
  name     = "claimsiq-workflow"
  role_arn = aws_iam_role.step_role.arn

  definition = jsonencode({
    StartAt = "ProcessClaim"
    States = {
      ProcessClaim = {
        Type   = "Pass"
        End    = true
        Result = "Claim Processed Successfully"
      }
    }
  })
}
