from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["munich"]:
        return "It's 15 degrees Celsius and cloudy."
    else:
        return "It's 32 degrees Celsius and sunny."


def create_llm(model_name: str = "gpt-4o-mini") -> ChatOpenAI:
    """
    Factory function to create and configure the LLM model with the provided tools.

    Args:
        model_name (str): The name of the language model to use.

    Returns:
        ChatOpenAI: The configured LLM instance.
    """
    tools = [get_weather]
    model = ChatOpenAI(model=model_name, base_url="https://open.bigmodel.cn/api/paas/v4")
    model = model.bind_tools(tools)
    return model


if __name__ == "__main__":
    llm = create_llm("GLM-4-Flash")
    print(llm.invoke("What is the weather in Munich?"))