import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_to_file
from utils.bedrock_llm import BedrockLlm  # noqa: F401 — registers bedrock/... model

code_writer_agent = LlmAgent(
    name="code_writer_agent",
    model="bedrock/amazon.nova-lite-v1:0",
    instruction=load_instructions_file("agents/code_writer/instructions.txt"),
    description=load_instructions_file("agents/code_writer/description.txt"),
    tools=[write_to_file]
)
