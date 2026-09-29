# Website Builder Agent — AWS Bedrock + Google ADK

A simple AI agent built with **Google Agent Development Kit (ADK)** that generates complete HTML+CSS+JS web pages from natural language prompts and saves them as files. Powered by **AWS Bedrock (Amazon Nova Lite)** using a bearer token — no AWS access keys needed.

---

## Project Structure

```
version_1_website_builder_simple/
├── agents/
│   └── website_builder_simple/
│       ├── agent.py              # Agent definition (model + tools)
│       ├── instructions.txt      # System prompt for the agent
│       └── description.txt       # Short description shown in ADK UI
├── tools/
│   └── file_writer_tool.py       # Tool: saves generated HTML to output/
├── utils/
│   ├── file_loader.py            # Reads instruction/description text files
│   └── bedrock_llm.py            # Custom ADK wrapper for AWS Bedrock
├── output/                       # Auto-created — generated HTML files go here
├── .env                          # Your AWS credentials (never commit this)
├── .gitignore                    # Excludes .env, .venv, output/ etc.
├── pyproject.toml                # Python dependencies
└── agent_runner.py               # Alternative: run agent from terminal
```

---

## Prerequisites

Make sure you have these installed before starting:

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.11+ | [python.org](https://www.python.org/downloads/) |
| uv | latest | `pip install uv` |
| Git | any | [git-scm.com](https://git-scm.com/) |

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/version_1_website_builder_simple
```

---

## Step 2 — Create a Virtual Environment

```bash
uv venv
```

This creates a `.venv` folder in your project directory.

**Activate it:**

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **Mac / Linux:**
  ```bash
  source .venv/bin/activate
  ```

You should see `(.venv)` at the start of your terminal prompt.

---

## Step 3 — Install Dependencies

```bash
uv sync
```

This installs everything listed in `pyproject.toml`:
- `google-adk` — Agent Development Kit framework
- `langchain-aws` — ChatBedrockConverse for AWS Bedrock
- `python-dotenv` — loads `.env` file automatically
- `rich` — nice terminal output

---

## Step 4 — Set Up Your AWS Credentials

Create a `.env` file in the project root:

```bash
# Windows
copy .env.example .env

# Mac / Linux
cp .env.example .env
```

Open `.env` and fill in your values:

```env
AWS_BEARER_TOKEN_BEDROCK=your-bearer-token-here
AWS_REGION_NAME=ap-southeast-2
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

### How to get your AWS Bearer Token

1. Log in to **AWS Console**
2. Open **AWS CloudShell** (top navigation bar)
3. Run this command:
   ```bash
   aws configure export-credentials --format env
   ```
4. Copy the value after `AWS_SESSION_TOKEN=` — that is your bearer token
5. Paste it as `AWS_BEARER_TOKEN_BEDROCK=` in your `.env` file

> **Note:** Bearer tokens expire every ~12 hours. Generate a new one if you get an auth error.

> **Important:** Never commit your `.env` file. It is already in `.gitignore`.

---

## Step 5 — Run the Agent

### Option 1: Browser UI (recommended)

```bash
adk web ./agents
```

Open `http://localhost:8000` in your browser.
Select **website_builder_simple** from the agents list and start chatting.

### Option 2: Terminal

```bash
uv run python -m agent_runner
```

### Option 3: API Server

```bash
adk api_server ./agents
```

Exposes a REST API at `http://localhost:8000`.

---

## Example Prompts

### Simple
```
Create a landing page with a blue background and a centered heading that says "Welcome". Write this to an output file using the tool.
```

### Styled
```
Build a developer portfolio page for "Ali Hassan" with a dark theme, skills section with progress bars (Python 90%, AWS 75%, React 70%), and 3 project cards. Write this to an output file using the tool.
```

### Interactive
```
Create a personal expense tracker app with a form to add expenses (name, amount, category). Show all entries in a table with a delete button and display the total at the bottom. Write this to an output file using the tool.
```

### Dashboard
```
Build an analytics dashboard with a dark theme showing 4 stat cards (Revenue $24,500 / Users 1,842 / Orders 329 / Conversion 4.2%), a bar chart for monthly sales, and a recent orders table. Write this to an output file using the tool.
```

> **Tip:** Always end your prompt with **"Write this to an output file using the tool."** — this tells the agent to call the file writer tool and save the result.

---

## Output Files

Generated pages are saved in the `output/` folder with a timestamp in the filename:

```
output/
└── 260928_143022_generated_page.html
```

Open any file directly in your browser to see the result.

---

## How It Works

```
Your Prompt
    ↓
Google ADK (LlmAgent)
    ↓
BedrockLlm wrapper (utils/bedrock_llm.py)
    ↓
ChatBedrockConverse → AWS Bedrock (Amazon Nova Lite)
    ↓
Agent calls write_to_file tool
    ↓
HTML saved to output/
```

The key file is `utils/bedrock_llm.py` — it acts as a bridge between Google ADK and AWS Bedrock, converting message formats in both directions so ADK can use any Bedrock model without needing AWS access keys.

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `Auth error / ExpiredToken` | Your bearer token expired — generate a new one (Step 4) |
| `Model not found` | Check that `utils/bedrock_llm.py` is imported in `agent.py` |
| `uv: command not found` | Run `pip install uv` first |
| `adk: command not found` | Make sure your virtual environment is activated |
| Agent gives wrong response | Check `agents/website_builder_simple/instructions.txt` content |

---

## Key Concepts Covered

- **Google ADK** — building agents with tools using `LlmAgent`
- **AWS Bedrock** — running foundation models on AWS
- **Custom model wrapper** — extending ADK to support non-Gemini models
- **Tool calling** — agent decides when and how to call `write_to_file`
- **Bearer token auth** — using short-lived AWS tokens instead of access keys

---

## License

GNU General Public License v3.0 — see [LICENSE](./LICENSE) for details.
