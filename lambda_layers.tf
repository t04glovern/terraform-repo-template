locals {
  # https://docs.powertools.aws.dev/lambda/python/latest/
  powertools_layer_versions = {
    "us-east-1" = "arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV2:67",
    "us-west-2" = "arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV2:67"
  }
}