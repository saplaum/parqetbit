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
-   **Files**: `lowercase-with-dashes.js` (adapt extension to language)
-   **Functions**: `verbPhrases` (e.g., `getUser`, `validateEmail`)
-   **Predicates**: `isValid`, `hasPermission`, `canAccess`
-   **Variables**: Descriptive (e.g., `userCount` not `uc`), `const` by default.
-   **Constants**: `UPPER_SNAKE_CASE`

### Imports
-   Group imports by type (e.g., built-in, third-party, local).
-   Alphabetize imports within each group.
-   Use relative paths for local imports.

### Formatting
-   Consistent indentation (e.g., 2 or 4 spaces, depending on language/project convention).
-   Line length limit (e.g., 100-120 characters).
-   Consistent brace style.
-   Use a linter/formatter if available (see Section 3).

### Types
-   Utilize type-checking where the language supports it (e.g., TypeScript, Python with type hints, Go).
-   Be explicit with types for function parameters and return values.

### Error Handling
-   **Explicit Error Handling**: Functions should clearly indicate success or failure.
    ```javascript
    // Example: Explicit error handling
    function parseJSON(text) {
      try {
        return { success: true, data: JSON.parse(text) };
      } catch (error) {
        return { success: false, error: error.message };
      }
    }
    ```
-   **Validate at Boundaries**: Perform input validation at the entry points of functions or modules.

### Dependency Injection
-   Dependencies should be explicit and passed into functions/modules, rather than imported globally.
    ```javascript
    // Example: Explicit dependencies
    function createUserService(database, logger) {
      return {
        createUser: (userData) => {
          logger.info('Creating user');
          return database.insert('users', userData);
        }
      };
    }
    ```

---

## 3. Build, Lint, and Test Commands

No specific build, lint, or test configuration files were found in this repository. Agents should infer the appropriate commands based on the project's language and structure.

### General Approach for Agents:
1.  **Identify Project Language**: Determine the primary programming language(s) used (e.g., Python, Go, JavaScript/TypeScript, Rust).
2.  **Search for Common Tools**: Look for common build tools, package managers, and testing frameworks associated with that language.
    -   **Python**: `pytest`, `unittest`, `flake8`, `mypy`, `pip`, `poetry`
    -   **Go**: `go build`, `go test`, `go fmt`, `golangci-lint`
    -   **Rust**: `cargo build`, `cargo test`, `cargo clippy`, `cargo fmt`
    -   **JavaScript/TypeScript**: `npm`, `yarn`, `pnpm`, `webpack`, `rollup`, `jest`, `mocha`, `eslint`, `prettier`, `tsc`
3.  **Infer Commands**: Construct commands based on the identified tools.

### Placeholder Commands (Infer or Ask User):
-   **Build Command**: `[Infer from project or ask user]`
-   **Lint Command**: `[Infer from project or ask user]`
-   **Test Command (All)**: `[Infer from project or ask user]`
-   **Test Command (Single Test)**: `[Infer from project or ask user]`
    *Example for Python with pytest*: `pytest path/to/test_file.py::test_function_name`
    *Example for JavaScript with Jest*: `jest path/to/test_file.test.js -t "test name"`

---

## 4. Agent-Specific Rules

No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` files were found in this repository. Therefore, no agent-specific rules are explicitly defined beyond these general guidelines.

---

**Note to Agents**: If you encounter new patterns, tools, or conventions not covered here, please update this `AGENTS.md` file and propose the changes for review.
