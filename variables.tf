variable "prefix" {
  type        = string
  description = "Prefix for resources"
  validation {
    condition     = length(var.prefix) <= 15 && can(regex("^[a-zA-Z0-9-]*$", var.prefix))
    error_message = "Prefix must be alphanumeric and hyphens only, and less than 15 characters."
  }
}
