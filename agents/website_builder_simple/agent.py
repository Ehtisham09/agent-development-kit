# =============================================================================
# FILE: agent.py
# PURPOSE:
#   Defines the root LLM agent for the website builder using AWS Bedrock.
#   Uses ChatBedrockConverse (same as other notebooks) via a custom ADK wrapper.
# =============================================================================

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from google.adk.agents import LlmAgent

from tools.file_writer_tool import write_to_file
from utils.file_loader import load_instructions_file

# This import registers "bedrock/..." as a valid ADK model — must come before LlmAgent
from utils.bedrock_llm import BedrockLlm  # noqa: F401

root_agent = LlmAgent(
    name="website_builder_simple",

    # Same model we use in all other notebooks — bearer token auth handled automatically
    model="bedrock/amazon.nova-lite-v1:0",

    instruction=load_instructions_file("agents/website_builder_simple/instructions.txt"),
    description=load_instructions_file("agents/website_builder_simple/description.txt"),

    tools=[write_to_file],
)
