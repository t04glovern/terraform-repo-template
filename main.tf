module "redrive_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "${var.prefix}-redrive-sqs"

  build_in_docker = true

  handler = "redrive.handler"
  runtime = "python3.11"

  layers = [
    local.powertools_layer_versions[data.aws_region.current.name]
  ]

  source_path = {
    path             = "../redrive/src",
    pip_requirements = "../redrive/requirements.txt"
  }
}
