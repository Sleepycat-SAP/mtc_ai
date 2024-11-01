# Deploy a simple app to consume Gen AI HUB
这个 Cloud Foundry 应用程序建立了与 Generative AI Hub 的连接，发送了一个硬编码的输入消息，并显示输出消息。
然而，为了满足生产运营需求，建议通过 Cloud Foundry 环境变量使用服务绑定凭据连接到 Generative AI Hub。

## 先决条件。

* 填写 **.aicore/config.json** 中的必填字段  
  从 AI Core 服务密钥中复制相关字符串：  
    AICORE_AUTH_URL,  
    AICORE_CLIENT_ID,  
    AICORE_CLIENT_SECRET,  
    AICORE_BASE_URL

* 在 app.py 中填写真实的部署 ID  
  将字符串 "xxxxxxxx" 替换为真实的部署 ID。

## 如何在本地环境中调试代码  
  将 config.json 定位到此文件夹：**~/.aicore/config.json**。您可以像往常一样在本地环境中运行应用程序。

## 将应用程序部署到 CF 运行时  
通过 cf cli 登录到组织/空间。然后执行以下命令完成部署：  
```bash
cf push
```

## 验证应用程序  
在 SAP BTP 控制台中启动应用程序，验证 LLM 的答案是否在浏览器中显示。  
![launch_app](./img/launch_app.png)  

## 使用 langchain 连接 Gen AI Hub 的另一种方法  

除了调整大型语言模型中的参数，如 "temperature"、"top_k" 或 "max_tokens"，Gen AI Hub 还提供了各种大型语言模型供客户选择，例如 AWS Claude3 和 GCP gemini。客户可以通过简单地使用函数 **init_llm** 来利用所有这些功能。  
* 在 manifest.yml 中将应用程序名称更新为 **mygenaiapp**  
  `command: python mygenaiapp.py`
* 在 mygenaiapp.py 中填写预期的模型  
  模型名称取决于在 SAP AI Launchpad 中的设置。模型名称可以在 SAP AI Launchpad / ML Operations / Configurtions 中找到。在 SAP AI Core 中，我们提供了这些模型："gpt-4"、"gpt-4-32k" 和 "gpt-4o"  
* 将应用程序部署到 CF 运行时  
```bash
cf push
```

## 引用链接  
[从环境变量连接](https://github.com/SAP-samples/btp-gen-ai-hub-sdk-samples/blob/main/docs/notebook-samples/1-connect-to-aicore-from-env.ipynb)  
[使用 langchain 连接 gen-ai-hub](https://github.com/SAP-samples/btp-gen-ai-hub-sdk-samples/blob/main/docs/notebook-samples/2-connect-genaihub-from-env.ipynb)


## 部署 ID          配置名称
d22519db36b85d26  anthropic--claude-3.5-sonnet
d5f4dd239ca047ed  anthropic--claude-3-sonnet
d284550b7b7065a8  text-embedding-3-large
d98293f973094cb6  text-embedding-3-small
d0ee97b0389eb76d  gpt-4-32k
d09c4d9ecdbab455  chatgpt-4o
d429f1099b48b117  gpt-4