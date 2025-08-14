import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# LM Studio API설정
# LM Studoi가 제공하는 로컬 API 엔드포인트를 지정합니다.
base_url = "http://127.0.0.1:1234/v1"


#LM Studio는 API Key가 필수는 아니지만, LangChain 에서 요구하므로 임의의 값을 넣습니다.
os.environ["OPENAI_API_KEY"] = "not-needed"

#ChatOpenAI 객체 초기화
#openai_api_base를 LM Studio의 엔드포인트로 설정합니다.
llm = ChatOpenAI(openai_api_base=base_url, temperature=0.7)#접속

#LangChain 체인 구축(예시)
prompt = ChatPromptTemplate.from_template("다음 질문에 대해 1~2문장으로 답변해줘: {question}") #질문 시스템 프롬프트
output_parser = StrOutputParser() #결과

#체인실행
chain = prompt | llm | output_parser

response = chain.invoke({"question" : "인공지능이란 무엇인가요?"})
print(response)