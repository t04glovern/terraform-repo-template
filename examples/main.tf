provider "aws" {
  region = local.region
}

locals {
  region = "us-east-1"
}

resource "random_pet" "this" {
  length = 2
}


module "example" {
  source = "../"
  prefix = random_pet.this.id
}
