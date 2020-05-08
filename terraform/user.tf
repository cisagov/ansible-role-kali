# Create the test user
module "user" {
  source = "github.com/cisagov/molecule-iam-user-tf-module"

  providers = {
    aws                   = aws.users
    aws.images-production = aws.images_production
    aws.images-staging    = aws.images_staging
  }

  ssm_parameters = ["/gitlab/personal_authorization_token"]
  user_name      = "test-ansible-role-kali"

  tags = {
    Team        = "VM Fusion - Development"
    Application = "ansible-role-kali testing"
  }
}
