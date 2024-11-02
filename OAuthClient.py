import requests
import logging
from requests.auth import HTTPBasicAuth

class OAuthClient:
    _tokenInfo = None
    def __init__(self, client_secret_credentials):
        self._clientSecretCredentials = client_secret_credentials
        self._logger = logging.getLogger(__name__)

    def fetch_token_with_client_secret(self):
        url = self._clientSecretCredentials['url']
        clientid = self._clientSecretCredentials['clientid']
        clientsecret = self._clientSecretCredentials['clientsecret']

        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }

        http_call = {
            'url': url if "/oauth/token" in url else f"{url}/oauth/token",
            'method': "post",
            'auth': HTTPBasicAuth(clientid, clientsecret),
            'data': "grant_type=client_credentials&response_type=token",
            'headers': headers
        }

        res = self.http_call_func_token(http_call)
        json = res.json()
        self._tokenInfo = json['access_token']

    def execute_authenticated_http(self, http_request):
        headers = http_request.get('headers', {})
        headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._tokenInfo}"
        })
        http_request['headers'] = headers
        http_request['method'] = http_request.get('method', 'POST')
        http_response = None
        for retries in range(5):
            try:
                http_response = self.http_call_gpt(http_request)
                if http_response is not None:
                    break
            except requests.RequestException as e:
                self._logger.error(f"Retry: {retries} - API could not be called: {str(e)}")
        return http_response
    
    def http_call_gpt(self, http_request):
        try:
            response = requests.request(
                method=http_request['method'],
                url=http_request['url'],
                headers=http_request['headers'],
                json=http_request.get('data')
            )
            response.raise_for_status()  # Will raise an exception for HTTP errors
        except requests.RequestException as e:
            raise RuntimeError(f"Error while making HTTP call: {str(e)}")
        return response
    
    def http_call_func_token(self, http_call):
        response = requests.post(
            http_call['url'],
            auth=http_call['auth'],
            data=http_call['data'],
            headers=http_call['headers']
        )
        response.raise_for_status()
        return response
