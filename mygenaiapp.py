from gen_ai_hub.proxy.langchain.init_models import init_llm

model = 'gpt-4o' # the model name could be any avaialble LLMs in SAP AI Core, such as "gpt-4", "gpt-4-32k" or "gpt-4o"
llm = init_llm(model, temperature=0.8, max_tokens=256)

prompt = """Translate to Chinese: We are the best Cloud ERP provider"""
result = llm.invoke(prompt).content
print(result)