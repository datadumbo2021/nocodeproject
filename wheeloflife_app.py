# Streamlit 라이브러리를 사용하여 레이더 차트를 생성하는 파이썬 코드를 작성해보겠습니다.
# 이 코드는 Streamlit 앱에서 실행되도록 설계되었습니다.

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def make_radar_chart(categories, values):
    # 각 변수의 값을 저장하는 배열
    num_vars = len(categories)

    # 레이더 차트를 그릴 때 필요한 각도 계산
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # 그래프를 닫기 위해 값과 각도의 시작점을 끝에 다시 추가
    values += values[:1]
    angles += angles[:1]

    # 차트를 그릴 준비
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 라인 그리기
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)

    # 축 레이블 추가
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # y축의 점수 표시를 제거
    ax.set_yticks([])

    return fig

# Streamlit 앱의 인터페이스 설정
st.title('레이더 차트 생성기')

# 변수의 개수 (카테고리)
categories = ["비즈니스/커리어", "재정", "건강/체력", "가족/친구", "연애/결혼", "개인/성장", "재미/여가", "환경/공간"]

# 각 카테고리에 대한 슬라이더를 생성하고 점수를 배열로 저장
values = []
for category in categories:
    score = st.slider(f'{category} 점수', 0, 10, 5)  # 기본값은 5점
    values.append(score)

# '차트 생성' 버튼
if st.button('차트 생성'):
    # 차트 생성 함수 호출
    fig = make_radar_chart(categories, values)
    # 차트를 Streamlit에 표시
    st.pyplot(fig)
