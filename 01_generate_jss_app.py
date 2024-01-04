##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai




##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse





##### 메인 함수 #####
def main():
    st.set_page_config(page_title="자기소개서 작성 프로그램")
    # session state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""



    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')
        # 입력받은 API 키 표시
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey 
        st.markdown('---')


    #메인공간
    st.header("📝자기소개서 작성 프로그램")
    st.markdown('---')

    st.text('👉 입력내용이 많을 수록 좋은 자기소개서가 작성됩니다! ')
    name = st.text_input("희망 직무명",placeholder="데이터 분석가, 개발자..등")
    strenghth = st.text_input("본인의 직무 강점",placeholder="논리적, 객관적, 꼼꼼함.. 등  ")
    keyword = st.text_input("보유하고 있는 직무역량",placeholder="파이썬, 분석의 이해, 시각화.. 등 ")
    personality = st.text_input("본인의 성격",placeholder="성실함, 차분함, 조직 친화적.. 등")
    exper = st.text_input("직무관련 경험",placeholder="직무 관련 경험(인턴, 프로젝트, 학회 등)")
    licen = st.text_input("직무관련 자격증/수상",placeholder="직무 관련 자격증 및 수상경험 등")
    value = st.text_input("필수 포함 내용",placeholder="본인이 표현하고 싶은 내용을 작성")
    tone_manner = st.text_input("톤엔 메너",placeholder="진지하게, 발랄하게, 차분하게, 열정적으로..")


    if st.button("자기소개서 생성"):
        prompt = f'''
        아래 내용을 참고해서 10줄짜리 자기소개서 작성해줘
        - 희망 직무명: {name}
        - 본인의 직무 강점: {strenghth}
        - 보유하고 있는 직무역량: {keyword}   
        - 직무관련 경험: {exper}
        - 직무관련 자격증/수상: {licen}
        - 본인의 성격: {personality}
        - 필수 포함 내용: {value}
        - 톤엔 메너: {tone_manner}

        '''
        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))

if __name__=='__main__':
    main()