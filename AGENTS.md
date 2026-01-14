# AGENT GUIDELINES

This document outlines the coding standards and operational guidelines for agentic coding agents working within this repository. Adhering to these guidelines ensures consistency, quality, and maintainability of the codebase.

---

## 1. Core Philosophy & Principles

**Golden Rule**: If you can't easily test it, refactor it.

### Core Philosophy
-   **Modular**: Everything is a component - small, focused, reusable.
-   **Functional**: Pure functions, immutability, composition over inheritance.
-   **Maintainable**: Self-documenting, testable, predictable.

### Principles
-   **Modular Design**: Single responsibility per module, clear interfaces, independent and composable. Keep components under 100 lines, ideally under 50.
-   **Functional Approach**:
    -   **Pure functions**: Same input = same output, no side effects.
    -   **Immutability**: Create new data, don't modify existing.
    -   **Composition**: Build complex from simple functions.
    -   **Declarative**: Describe what, not how.

---

## 2. Code Style Guidelines

### Naming Conventions
-   **Files**: `lowercase_with_underscores.py` (adapt extension to language)
-   **Functions**: `snake_case` (e.g., `get_user`, `validate_email`)
-   **Predicates**: `is_valid`, `has_permission`, `can_access`
-   **Variables**: Descriptive (e.g., `userCount` not `uc`), `const` by default.
-   **Constants**: `UPPER_SNAKE_CASE`

### Imports
-   Group imports by type (e.g., built-in, third-party, local).
-   Alphabetize imports within each group.
-   Use relative paths for local imports.

### Formatting
-   Consistent indentation (e.g., 4 spaces, depending on language/project convention).
-   Line length limit (e.g., 100-120 characters).
-   Consistent brace style.
-   Use a linter/formatter if available (see Section 3).

### Types
-   Utilize type-checking where the language supports it (e.g., Python with type hints).
-   Be explicit with types for function parameters and return values.

### Error Handling
-   **Explicit Error Handling**: Functions should clearly indicate success or failure.
    ```python
    # Example: Explicit error handling
    def parse_json(text):
      try:
        return {"success": True, "data": json.loads(text)}
      except json.JSONDecodeError as error:
        return {"success": False, "error": str(error)}
    ```
-   **Validate at Boundaries**: Perform input validation at the entry points of functions or modules.

### Dependency Injection
-   Dependencies should be explicit and passed into functions/modules, rather than imported globally.
    ```python
    # Example: Explicit dependencies
    def create_user_service(database, logger):
      def create_user(user_data):
        logger.info('Creating user')
        return database.insert('users', user_data)
      return {'create_user': create_user}
    ```

---

## 3. Build, Lint, and Test Commands

No specific build, lint, or test configuration files were found in this repository. Agents should infer the appropriate commands based on the project's language and structure.

### General Approach for Agents:
1.  **Identify Project Language**: Determine the primary programming language(s) used (e.g., Python, Go, JavaScript/TypeScript, Rust).
2.  **Search for Common Tools**: Look for common build tools, package managers, and testing frameworks associated with that language.
    -   **Python**: `pytest`, `unittest`, `flake8`, `mypy`, `pip`, `poetry`
3.  **Infer Commands**: Construct commands based on the identified tools.

### Placeholder Commands (Infer or Ask User):
-   **Build Command**: `[Infer from project or ask user]`
-   **Lint Command**: `[Infer from project or ask user]`
-   **Test Command (All)**: `[Infer from project or ask user]`
-   **Test Command (Single Test)**: `[Infer from project or ask user]`
    *Example for Python with pytest*: `pytest path/to/test_file.py::test_function_name`

---

## 4. Agent-Specific Rules

No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` files were found in this repository. Therefore, no agent-specific rules are explicitly defined beyond these general guidelines.

---

**Note to Agents**: If you encounter new patterns, tools, or conventions not covered here, please update this `AGENTS.md` file and propose the changes for review.
