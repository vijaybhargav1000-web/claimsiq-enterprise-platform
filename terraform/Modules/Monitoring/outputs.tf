output "log_group" {
  value = aws_cloudwatch_log_group.claimsiq_logs.name
}

output "sns_topic" {
  value = aws_sns_topic.alerts.arn
}
