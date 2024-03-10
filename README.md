# terraform-repo-template

Example template for creating a new Terraform module.

## Usage

Basic usage of this module is as follows:

```hcl
module "example" {
  source = "github.com/t04glovern/terraform-repo-template?ref=v1.0.0"
  name   = "example"
}
```

## Commit Structure

More information can be found at [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

- **fix**: a commit of the type fix patches a bug in your codebase (this correlates with `PATCH` in Semantic Versioning).
- **feat**: feat: a commit of the type feat introduces a new feature to the codebase (this correlates with `MINOR` in Semantic Versioning).
- **<any>!**: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with `MAJOR` in Semantic Versioning).
  - A BREAKING CHANGE can be part of commits of any type.
- **docs**: updates to documentation such as a the README or other markdown files
- **ci**: continuous integration related
- **chore**: changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)

## Run Pre-commit

```bash
pre-commit run --all-files
```

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 5.0 |
| <a name="requirement_null"></a> [null](#requirement\_null) | >= 3.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | >= 3.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 5.0 |
| <a name="provider_random"></a> [random](#provider\_random) | >= 3.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_redrive_function"></a> [redrive\_function](#module\_redrive\_function) | terraform-aws-modules/lambda/aws | n/a |

## Resources

| Name | Type |
|------|------|
| [random_pet.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet) | resource |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_prefix"></a> [prefix](#input\_prefix) | Prefix for resources | `string` | n/a | yes |

## Outputs

No outputs.