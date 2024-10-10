# MarkPoint

Markpoint is a program for me and me only that generates simple PPTX slides from sloppy markdown
notes. This is useful because I hate PowerPoint for writing and I love Vim. But there is not picture
support in Vim and Beamer presentations are cool but you see that they are Beamer presentations and
that your Prof did not want to use PowerPoint because it sucks ass for large presentations with many
information.

## API

> [!NOTE]
> This is the first iteration nobody should use this any ways so don't depend on anything here

## TODO

- [ ] add the ability to only add text to a slide without bullet points
- [ ] if the capabilities of this library grow consider using markdown-analyzer for now a simple
      parsing implementation should suffice
- [ ] write the api
- [ ] make it work as a lib and as a program
- [ ] write setup py
- [ ] define the information api for a `SlideInfo` object
- [ ] define the format that can be chosen for inputing data through markdown
  - this will be a limited set of features for now like
  - bullets
  - text
  - header
- [ ] define a cli api that is comfortable
- [ ] test all the shit
  - [ ] test parsing
  - [ ] test generation
  - [ ] test slideinfo generation

## Contributing to Markpoint

We welcome all contributions to make Markpoint even better! Whether you’re fixing a bug, adding a
new feature, or improving documentation, your help is appreciated.

### Guidelines

- **Code Style**: Follow the code style enforced by [Ruff](https://beta.ruff.rs/docs/), which is
  integrated into the project.
- **Testing**: Please add tests for any new features or bug fixes to help maintain stability.
- **Pull Requests**: Open a PR with a clear description of your changes. Include relevant issue
  numbers, if applicable.

### Getting Started

1. **Fork** this repository and clone it locally.
2. Install any necessary dependencies.
3. Make your changes, following our style and test guidelines.

Thank you for contributing to Markpoint! ❤️ Every PR is valued, and even taking the time to read this means a lot.
