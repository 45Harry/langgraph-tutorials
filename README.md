# LangGraph Tutorials

This repository contains a collection of hands-on tutorials and example scripts for learning and experimenting with [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain) in Python. The tutorials cover a range of topics, from building simple computation graphs to creating chatbots, using tools, and integrating memory and human-in-the-loop (HITL) workflows.

## Author

**45Harry**

## Contents

- **1_simple_graph.ipynb**: Introduction to building a simple computation graph using LangGraph.
- **2_graph_with_condition.ipynb**: Demonstrates conditional logic within a graph.
- **3_chatbot.ipynb**: Shows how to build a basic chatbot using LangGraph and LangChain.
- **4_tool_call.ipynb**: Example of calling external tools from within a graph.
- **5_tool_call_agent.ipynb**: Expands on tool calling with agent-based workflows.
- **6_memory.ipynb / 6_memory.py**: Explores adding memory and stateful behavior to your graphs.
- **7_langsmith.ipynb**: Integrates with LangSmith for experiment tracking and evaluation.
- **8_HITL.py**: Demonstrates human-in-the-loop (HITL) patterns in LangGraph.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd langgraph-tutorials
   ```

2. **Install dependencies:**
   This project uses [Python 3.13+](https://www.python.org/downloads/) and the following main packages:
   - `langchain`
   - `langchain-google-genai`
   - `langgraph`
   - `langsmith`
   - `notebook`
   - `numpy`
   - `python-dotenv`

   You can install all dependencies using [uv](https://github.com/astral-sh/uv) (recommended for speed) or pip:
   ```bash
   uv pip install -e .
   ```
   or
   ```bash
   pip install -e .
   ```

   The project uses `pyproject.toml` as the requirements file.

3. **Set up environment variables:**
   Some tutorials require API keys (e.g., for Google GenAI). Create a `.env` file in the project root and add your keys as needed.

## Usage

- Open any of the `.ipynb` notebooks in Jupyter or VSCode to follow along with the tutorials.
- For `.py` scripts, run them directly with Python:
  ```bash
  python 6_memory.py
  ```

## License

MIT License
