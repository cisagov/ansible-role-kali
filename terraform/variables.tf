# ------------------------------------------------------------------------------
# Optional parameters
#
# These parameters have reasonable defaults.
# ------------------------------------------------------------------------------

variable "aws_region" {
  type        = string
  description = "The AWS region to deploy into (e.g. us-east-1)."
  default     = "us-east-1"
}

variable "production_bucket_name" {
  type        = string
  description = "The name of the S3 bucket where the production Burp Suite Pro intaller and license live."
  default     = "cisa-cool-third-party-production"
}

variable "production_objects" {
  type        = list(string)
  description = "The Burp Suite Pro installer and license objects inside the production bucket."
  default = [
    "burpsuite_pro.license",
    "burpsuite_pro_linux_v2020_11.sh",
  ]
}

variable "staging_bucket_name" {
  type        = string
  description = "The name of the S3 bucket where the staging Burp Suite Pro intaller and license live."
  default     = "cisa-cool-third-party-staging"
}

variable "staging_objects" {
  type        = list(string)
  description = "The Burp Suite Pro installer and license objects inside the staging bucket."
  default = [
    "burpsuite_pro.license",
    "burpsuite_pro_linux_v2020_11.sh",
  ]
}

variable "tags" {
  type        = map(string)
  description = "Tags to apply to all AWS resources created"

  default = {
    Team        = "VM Fusion - Development"
    Application = "ansible-role-kali testing"
  }
}
