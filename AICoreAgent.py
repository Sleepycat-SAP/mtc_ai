from OAuthClient import OAuthClient
class AICoreAgent:
    _client_secret_credentials = {
        'url': '',
        'clientid': '',
        'clientsecret': ''
    }
    def getChatCompletion(self, messages):
        oAuthClient = OAuthClient(self._client_secret_credentials)
        oAuthClient.fetch_token_with_client_secret()
        http_request = {
            'url': 'https://example.com/api',
            'method': 'POST',
            'data': {'key': 'value'}
        }
        deploymentUrl = "https://api.ai.internalprod.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/d09c4d9ecdbab455/chat/completions?api-version=2023-05-15"
        # url = `${deploymentUrl}/chat/completions?api-version=${this._options.apiVersion ?? this._apiVersion}`;
        headers = { "AI-Resource-Group": 'default' }
        gptRequest = {
            'messages': messages,
            # max_tokens: options.maxTokens,
            'temperature': 0
            # frequency_penalty: options.frequencyPenalty,
            # presence_penalty: options.presencePenalty,
            # stream: stream
        };
        httpRequest = {
            'url': deploymentUrl,
            'headers': headers,
            'data': gptRequest
        };
        response = oAuthClient.execute_authenticated_http(httpRequest)
        if response:
            return response.json()
    