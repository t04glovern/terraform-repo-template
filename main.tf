resource "aws_s3_bucket" "example" {
  bucket = "${var.prefix}-example-bucket"
}
