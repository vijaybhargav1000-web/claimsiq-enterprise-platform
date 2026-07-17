resource "aws_athena_workgroup" "claimsiq" {
  name = "ClaimsIQ"

  configuration {
    enforce_workgroup_configuration = true
  }
}
