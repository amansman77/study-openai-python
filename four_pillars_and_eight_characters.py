import openai
from openai import OpenAI

try:
  client = OpenAI()

  assistant = client.beta.assistants.create(
    name="사주팔자",
    instructions="""
    너의 역할을 정해줄께.
    너는 사주를 풀이해주는 사람이야.

    상대방이 생년월일과 양력/음력과 시간을 입력해주면 답변은 이렇게 하면 좋을 것 같애.
    "입력해주신 생년월일과 시간은 0000년 00월 00일 00:00 (양력/음력)입니다. 이를 바탕으로 올해의 사주팔자를 알려드리겠습니다."

    **운세 항목별 풀이**:
      - 2024년의 전반적인 연간 운세를 제공합니다.
      - 월별 운세를 제공합니다.
      - 직업운과 재물운을 분석합니다.
      - 건강 운세를 분석합니다.
      - 애정운과 인간관계를 분석합니다.
      - 궁합(커플 궁합, 친구 궁합)을 분석합니다.
      - 자녀 운세를 분석합니다.
      - 특정 사건에 대한 운세(이사 운세, 여행 운세)를 제공합니다.
      - 길흉일 선택에 대한 정보를 제공합니다.
    """,
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o",
  )
  assistant_id = assistant.id

  thread = client.beta.threads.create()
  thread_id = thread.id

  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="0000년 00월 00일 양력 00:00"
  )

  run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id
  )

  if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
      thread_id=thread.id
    )
    for message in messages.data:
      if message.role == 'assistant':
        for each_content in message.content:
          print(each_content.text.value)
        break
  else:
    print(run.status)

except openai.APIError as e:
  #Handle API error here, e.g. retry or log
  print(f"OpenAI API returned an API Error: {e}")
  pass
except openai.APIConnectionError as e:
  #Handle connection error here
  print(f"Failed to connect to OpenAI API: {e}")
  pass
except openai.RateLimitError as e:
  #Handle rate limit error (we recommend using exponential backoff)
  print(f"OpenAI API request exceeded rate limit: {e}")
  pass
