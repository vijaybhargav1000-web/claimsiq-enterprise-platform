resource "aws_cloudwatch_log_group" "claimsiq_logs" {
  name              = "/aws/claimsiq/application"
  retention_in_days = 7
}

resource "aws_sns_topic" "alerts" {
  name = "claimsiq-alerts"
}

resource "aws_cloudwatch_metric_alarm" "cpu_alarm" {
  alarm_name          = "Claimsiq-High-CPU"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 300
  statistic           = "Average"
  threshold           = 80

  alarm_actions = [
    aws_sns_topic.alerts.arn
  ]
}
