import streamlit as st

#h1 태크
st.title("타이틀입니다. :100: :coffee:")

#h2 태크
st.header("헤더 입니다.")

#h3 태그
st.subheader("작은헤더 입니다.")

#p 태그
st.caption("캡션 입니다.")

# code 태그
st.code("st.code("",language="")", language="python")


cd="""
def 함수():
    pass
"""
st.code(cd,language="python")


#div 태그
st.text("일반 글 입니다.")

# p 태그에서 강조를 위해 strong 적용
st.markdown("파이썬은 **너무 너무** 쉽다")

#수식 표현 방법
st.markdown(":green[$\sqrt{x^2+y^2}=1$]")
st.latex(r"\sqrt{x^2+y^2}=1")