import openai
import requests

# OpenAI API 키 설정
openai.api_key = 'your-openai-api-key'

# 매니페스트 파일 설정 (예시)
manifest = {
    "schema_version": "v1",
    "name_for_human": "Example Plugin",
    "name_for_model": "example_plugin",
    "description_for_human": "This is an example plugin.",
    "description_for_model": "Plugin to demonstrate example functionalities.",
    "auth": {
        "type": "none"
    },
    "api": {
        "type": "openai",
        "url": "https://api.example.com/endpoint"
    }
}

# 플러그인 매니페스트 파일 생성
with open('plugin_manifest.json', 'w') as f:
    json.dump(manifest, f)

# API 요청 함수
def call_plugin_api(query):
    response = requests.post(
        url=manifest["api"]["url"],
        headers={
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json"
        },
        json={"query": query}
    )
    return response.json()

# 예제 API 호출
query = "Search for information"
response = call_plugin_api(query)
print(response)
