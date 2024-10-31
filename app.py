from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from gen_ai_hub.proxy.gen_ai_hub_proxy import GenAIHubProxyClient
from cfenv import AppEnv
from flask import Flask, request, abort
from sap import xssec

app = Flask(__name__)
env = AppEnv()
uaa_service = env.get_service(name='mtc-uaa').credentials
@app.route('/')
def hello_world():
    if 'authorization' not in request.headers:
         abort(403)
    access_token = request.headers.get('authorization')[7:]
    security_context = xssec.create_security_context(access_token, uaa_service)
    isAuthorized = security_context.check_scope('openid')
    if not isAuthorized:
         abort(403)
    my_proxy_client = GenAIHubProxyClient(resource_group="default")
    # Replace the deployment_id="XXXXXXXX" with real LLM deployment id 
    chat_llm = ChatOpenAI(deployment_id="d09c4d9ecdbab455", proxy_client=my_proxy_client)
    result = chat_llm.invoke("who are you")
    print(result.content)
    return result.content

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=8080)
