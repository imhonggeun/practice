from unstructured.partition.pdf import partition_pdf
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os
import json

file_name = "SPRi_AI_Brief_8월호_산업동향_F.pdf"

def extract_pdf_elements(filepath):
  return partition_pdf(
    filename=filepath,
    languages=["kor"],
    extract_images_in_pdf=False,
    infer_table_structure=False,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
  )
elements = extract_pdf_elements(file_name)

base_url = "http://localhost:1234/v1"
os.environ["OPENAI_API_KEY"] = "not-needed"

llm = ChatOpenAI(
  openai_api_base=base_url,
  temperature=0.7,
  streaming=True,
  callbacks=[StreamingStdOutCallbackHandler()]
)

prompt = PromptTemplate.from_template(
  """Context information is below. You are only aware of this context and nothing else.
---------------------

{context}

---------------------
Given this context, generate only questions based on the below query.
You are an Teacher/Professor in {domain}. 
Your task is to provide exactly **{num_questions}** question(s) for an upcoming quiz/examination. 
You are not to provide more or less than this number of questions. 
The question(s) should be diverse in nature across the document. 
The purpose of question(s) is to test the understanding of the students on the context information provided.
You must also provide the answer to each question. The answer should be based on the context information provided only.

Restrict the question(s) to the context information provided only.
QUESTION and ANSWER should be written in Korean. response in JSON format which contains the `question` and `answer`.
DO NOT USE List in JSON format.
ANSWER should be a complete sentence.

#Format:
```json
{{
    "QUESTION": "바이든 대통령이 서명한 '안전하고 신뢰할 수 있는 AI 개발과 사용에 관한 행정명령'의 주요 목적 중 하나는 무엇입니까?",
    "ANSWER": "바이든 대통령이 서명한 행정명령의 주요 목적은 AI의 안전 마련과 보안 기준 마련을 위함입니다."
}},
{{
    "QUESTION": "메타의 라마2가 오픈소스 모델 중에서 어떤 유형의 작업에서 가장 우수한 성능을 발휘했습니까?",
    "ANSWER": "메타의 라마2는 RAG 없는 질문과 답변 및 긴 형식의 텍스트 생성에서 오픈소스 모델 중 가장 우수한 성능을 발휘했습니다."    
}},
{{
    "QUESTION": "IDC 예측에 따르면 2027년까지 생성 AI 플랫폼과 애플리케이션 시장의 매출은 얼마로 전망되나요?",
    "ANSWER": "IDC 예측에 따르면 2027년까지 생성 AI 플랫폼과 애플리케이션 시장의 매출은 283억 달러로 전망됩니다."    
}}
```
"""
)

def custom_json_parser(response):
  json_string = response.content.strip().removeprefix("```json\n").removesuffix("\n```").strip()
  json_string = f'[{json_string}]'
  return json.loads(json_string)

chain = (prompt | llm | custom_json_parser)

qa = []

for element in elements[1:2]:
  if element.text:
    qa.extend(
      chain.invoke(
        {"context": element.text, "domain": "AI", "num_questions": "3"}
      )
    )

# 결과 내용 jsonl 파일로 저장하기
#print(qa)
try:
    with open ("qa.json","w",encoding="utf-8") as f:
        for data in qa:
            qa_modified = {
                "instuction" : data["QUESTION"],
                "input" : "",
                "output" : data["ANSWER"]
            }
            f.write(json.dumps(qa_modified, ensure_ascii=False) + "\n")
except:
    print("오류 발생!!")