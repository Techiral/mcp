import os
import subprocess
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.info("Starting Terminal Server MCP...")

mcp = FastMCP("terminal")
DEFAULT_WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "workspace"))
logging.info(f"Workspace path: {DEFAULT_WORKSPACE}")

@mcp.tool()
async def run_command(command: str) -> str:
    logging.info(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, cwd=DEFAULT_WORKSPACE, capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        logging.exception("Command failed")
        return str(e)

if __name__ == "__main__":
    mcp.run(transport='stdio')