provider "aws" {
  region = local.region
}

locals {
  region = "us-east-1"
}

module "example" {
  source = "../"
  name   = "example"
}