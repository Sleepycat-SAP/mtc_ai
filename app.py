from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from gen_ai_hub.proxy.gen_ai_hub_proxy import GenAIHubProxyClient
from cfenv import AppEnv
from flask import Flask
from AICoreAgent import AICoreAgent

app = Flask(__name__)
env = AppEnv()

@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    # Example usage
    aiCoreAgent = AICoreAgent()
    systemMessage = "You are professional financial expert. You are here to help the user with their financial queries.";
    userMessage = "I am looking for a loan to buy a car.";
    res = aiCoreAgent.getChatCompletion([
        { 'role': "system", 'content': systemMessage },
        { 'role': "user", 'content': userMessage }
    ])
    return res
    # if 'authorization' not in request.headers:
    #      abort(403)
    # my_proxy_client = GenAIHubProxyClient(resource_group="default")
    # # Replace the deployment_id="XXXXXXXX" with real LLM deployment id 
    # chat_llm = ChatOpenAI(deployment_id="d09c4d9ecdbab455", proxy_client=my_proxy_client)
    # result = chat_llm.invoke("who are you")
    # print(result.content)
    # return result.content

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=8080)
