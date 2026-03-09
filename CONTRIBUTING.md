# Contributing to CordovaOS

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Workflow](#contribution-workflow)
- [Contribution Types](#contribution-types)
- [Quality Standards](#quality-standards)
- [Review Process](#review-process)
- [Community](#community)

---

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

By participating, you agree to:
- Be respectful and inclusive
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what is best for the community

---

## How Can I Contribute?

### Encouraged Contributions

The following contributions are always welcome:

- **SPARQL Queries**: Cross-domain SPARQL queries demonstrating SDC4 graph traversal
- **Synthetic Data Generators**: New or improved data generation scripts in `datagen/`
- **Domain App Improvements**: Enhance existing Cordova government domain applications
- **Demo UI Enhancements**: Improve the demo interface and user experience
- **Documentation**: Clarify instructions, fix typos, add examples
- **Bug Reports**: Report issues with the demo, data generators, or SPARQL queries
- **Testing**: Validate cross-domain queries and report results

### Contributions Requiring Discussion

Please open an issue first for:

- **New Domain Applications**: Addition of entirely new government domains
- **Architecture Changes**: Significant alterations to project organization
- **Data Model Changes**: Modifications to existing SDC4 data models
- **Standards Updates**: Changes related to SDC4 or DPV evolution

---

## Getting Started

### Prerequisites

- GitHub account
- Docker or Podman installed (see [app/sdc4/README.md](app/sdc4/README.md) for details)
- Python 3.12+ (for data generation scripts)
- Basic understanding of Git and GitHub workflow
- Familiarity with SDC4 data modeling concepts (helpful but not required)

### Development Environment

1. **Fork the Repository**
   ```bash
   # Visit https://github.com/Axius-SDC/CordovaOS
   # Click "Fork" to create your own copy
   ```

2. **Clone Your Fork**
   ```bash
   git clone git@github.com:YOUR_USERNAME/CordovaOS.git
   cd CordovaOS
   ```

3. **Add Upstream Remote**
   ```bash
   git remote add upstream git@github.com:Axius-SDC/CordovaOS.git
   ```

4. **Start the Application**
   ```bash
   cd app/sdc4
   cp .env.example .env
   docker compose up -d --build
   ```

5. **Stay Updated**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

---

## Contribution Workflow

### 1. Create an Issue

For significant changes, create an issue first:
- Describe the problem or enhancement
- Explain your proposed solution
- Wait for maintainer feedback

For small fixes (typos, formatting), you can skip directly to creating a pull request.

### 2. Create a Branch

```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/description` - New features or enhancements
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `data/description` - Data generation or SPARQL query changes

### 3. Make Your Changes

- Follow the [Quality Standards](#quality-standards) below
- Keep commits focused and atomic
- Write clear commit messages

### 4. Commit Your Changes

```bash
git add .
git commit -m "Brief description of changes

Detailed explanation of what changed and why.
References #issue-number if applicable."
```

### 5. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub from your branch to the main repository's `main` branch.

---

## Contribution Types

### SPARQL Queries

**Guidelines:**
- Document what the query demonstrates
- Include expected results or result patterns
- Use standard SPARQL 1.1 syntax
- Test against the CordovaOS GraphDB instance
- Place query files in `sparql/` with sequential numbering

### Synthetic Data

**Guidelines:**
- Data must be obviously fictional (Republic of Cordova setting)
- Maintain referential integrity across domains
- Include enough records to demonstrate cross-domain queries
- Follow the demographic patterns in `design/SYNTHETIC_DATA_PLAN.md`
- Place generator scripts in `datagen/`

### Domain App Improvements

**Guidelines:**
- Follow existing Django patterns in `app/sdc4/`
- Maintain SDC4 compliance in all data models
- Test bulk import with generated XML instances
- Verify RDF triples load correctly into GraphDB

---

## Quality Standards

### Code Standards

- Follow PEP 8 for Python code
- Use consistent naming conventions
- Include docstrings for non-trivial functions
- Test data generators produce valid XML instances

### Markdown Formatting

- Use consistent heading hierarchy
- Include blank lines between sections
- Use code blocks with language specification
- Format lists consistently (use `-` for unordered lists)

### Data Integrity

- All person records must use valid CIDs from the Civil Registry
- Business references must use valid BRNs from the Business Registry
- Cross-domain references must resolve correctly in SPARQL queries

---

## Review Process

### What Reviewers Look For

1. **Correctness**: Do data generators produce valid XML? Do SPARQL queries return expected results?
2. **Cross-Domain Integrity**: Are references consistent across domains?
3. **Consistency**: Does it match existing conventions?
4. **Documentation**: Is the change well-documented?

---

## Community

### Communication Channels

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, community chat
- **Email**: support@axius-sdc.com

### Getting Help

1. Check existing documentation (README, design docs)
2. Search existing issues and discussions
3. Open a new discussion for general questions
4. Open an issue for specific problems

---

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0, the same license as the project.

---

Thank you for contributing to CordovaOS!
