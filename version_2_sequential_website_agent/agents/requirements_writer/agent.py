import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from utils.bedrock_llm import BedrockLlm  # noqa: F401 — registers bedrock/... model

requirements_writer_agent = LlmAgent(
    name="requirements_writer_agent",
    model="bedrock/amazon.nova-lite-v1:0",
    instruction=load_instructions_file("agents/requirements_writer/instructions.txt"),
    description=load_instructions_file("agents/requirements_writer/description.txt"),
    output_key="requirements_writer_output"
)
