output "user" {
  value       = module.user.user
  description = "The IAM user being created to test the cisagov/ansible-role-kali Ansible role."
}

output "user_access_key" {
  value       = module.user.access_key
  description = "The access key for the IAM user being created to test the cisagov/ansible-role-kali Ansible role."
  sensitive   = true
}
