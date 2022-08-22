# ci-workflows

Repository for common CI workflows.

## Usage

Any workflow can be called as follows:

```yml
call-worflow:
    uses: appex-development/ci-workflows/.github/workflows/node-build-and-verify.yml@main
```

Parameters can be passed in as follows:

```yml
call-worflow:
    uses: appex-development/ci-workflows/.github/workflows/node-build-and-verify.yml@main
    with:
        node_version: 14
```