provider "aws" {
  region = "us-east-1"
}

module "example" {
  source = "../"
  prefix = "abcdefg"
}
