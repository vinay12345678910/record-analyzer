# Contributing to Record Analyzer

Thank you for your interest in contributing to Record Analyzer! This document provides guidelines and instructions for contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected behavior** vs actual behavior
- **Sample data** that triggers the issue (if applicable)
- **Python version** and operating system

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear use case** - Why is this enhancement needed?
- **Detailed description** of the proposed functionality
- **Examples** of how it would work

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, descriptive commits
3. **Add tests** if you're adding functionality
4. **Update documentation** (README.md) if needed
5. **Ensure tests pass** before submitting
6. **Submit a pull request** with a clear description of changes

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/your-username/record-analyzer.git
cd record-analyzer
```

2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and test them:
```bash
python test_practice.py
```

## Coding Standards

- Follow [PEP 8](https://pep8.org/) style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions explaining parameters and return values
- Keep functions focused on a single responsibility
- Write clear commit messages

### Example Function Documentation

```python
def example_function(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
        
    Returns:
        dict: Description of return value
    """
    # Implementation
```

## Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep first line under 72 characters
- Reference issues and pull requests when relevant

Examples:
```
Add support for CSV input files
Fix validation bug for negative scores
Update README with new examples
```

## Testing

- Add test cases for new functionality
- Ensure all existing tests pass
- Test edge cases and error conditions
- Run tests before submitting PR:

```bash
python -m unittest test_practice.py
```

## Questions?

Feel free to open an issue with the label "question" if you need clarification on anything.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Assume good intentions

Thank you for contributing! 🎉
