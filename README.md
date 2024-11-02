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
安装CF Command Line：
https://docs.cloudfoundry.org/cf-cli/install-go-cli.html#pkg


通过 cf cli 登录到组织/空间。然后执行以下命令完成部署：  
```bash
cf push
```


## 部署 ID          配置名称
d22519db36b85d26  anthropic--claude-3.5-sonnet
d5f4dd239ca047ed  anthropic--claude-3-sonnet
d284550b7b7065a8  text-embedding-3-large
d98293f973094cb6  text-embedding-3-small
d0ee97b0389eb76d  gpt-4-32k
d09c4d9ecdbab455  chatgpt-4o
d429f1099b48b117  gpt-4