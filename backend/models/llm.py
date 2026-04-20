from langchain_ollama import OllamaLLM

def get_llm(model):
    llm = OllamaLLM(
        model=model,
        temperature=0.3,
        num_predict=300,
    )
    return llm 