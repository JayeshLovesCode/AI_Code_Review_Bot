## Project Overview

This tool is an automated code review assistant that bridges the gap between version control and artificial intelligence. It leverages the **GitHub API** to fetch code changes (diffs) from active Pull Requests and pipelines them to **Google's Gemini 2.5 Pro** model for analysis.

The system is designed to catch bugs, potential logic errors, and security vulnerabilities before they are merged. Currently operating as a secure local script, it handles the complete request lifecycle—authenticating with both services, packaging the code context, and retrieving actionable AI feedback.

---

## How It Works

The system follows a linear data pipeline to process code reviews:

1.  **Fetch Context:** The script connects to the GitHub API using a secure token to identify the specific Pull Request and retrieve the raw "diff" (the lines of code that have changed).
2.  **Prompt Engineering:** The raw code is wrapped in a structured prompt that instructs the AI to act as a Senior Software Engineer, focusing on bugs and security.
3.  **AI Analysis:** This payload is sent to Google's Gemini 2.5 Pro model via the Generative Language API.
4.  **Review Generation:** The AI processes the code changes and returns a detailed analysis, which is currently printed to the console for developer review.

---

## Configuration & Tokens

To use this tool, you must configure two environment variables to authenticate with the necessary APIs.

### 1. Get Your Keys
* **GitHub Token:** Save the Github token as `GITHUB_TOKEN`.
* **Gemini API Key:** Save the gemini token as `GEMINI_KEY`.

### 2. Set Environment Variables
You must set these keys in your environment before running the tool.

---

## Future Improvements

I am actively developing this project to evolve from a local tool into a fully autonomous workflow. The upcoming roadmap includes:

* **GitHub Actions Integration:** Migrating the script to run automatically within the CI/CD pipeline whenever a new Pull Request is opened.
* **Automated Commenting:** Upgrading permissions to allow the bot to post the AI's review directly to the GitHub PR timeline as a comment.
* **Context Optimization:** Implementing logic to handle large files and refine the AI prompts for more specific, high-priority feedback.

---
