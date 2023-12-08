import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def make_radar_chart(categories, current_values, ideal_values, ax):
    num_vars = len(categories)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    current_values += current_values[:1]
    ideal_values += ideal_values[:1]
    angles += angles[:1]

    ax.plot(angles, current_values, color='#75B14D', linewidth=2, linestyle='solid')
    ax.fill(angles, current_values, color='#75B14D', alpha=0.25)

    ax.plot(angles, ideal_values, color='#6EB4D1', linewidth=2, linestyle='solid')
    ax.fill(angles, ideal_values, color='#6EB4D1', alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([cat.split('/')[1] for cat in categories])

    ax.set_yticks([])

    return fig

st.title('Life Balance Wheel')

# 변수의 개수 (카테고리)
categories = [
    "비즈니스/Business", "재정/Finance", "건강/Health", "가족/Family",
    "연애/Relationship", "성장/Personal Growth", "여가/Leisure", "주변환경/Environment"
]

# '현재 내 삶의 점수' 헤더와 입력 필드
st.header('현재 내 삶의 점수')
cols = st.columns(4)
current_values = []
for i, category in enumerate(categories):
    with cols[i % 4]:
        score = st.number_input(f'{category.split("/")[0]} ({category.split("/")[1]}) 점수',
                                min_value=0, max_value=10, value=5, step=1,
                                key=f'current_{i}')
        current_values.append(score)

# '내가 지향하는 삶의 점수' 헤더와 입력 필드
st.header('내가 지향하는 삶의 점수')
cols = st.columns(4)
ideal_values = []
for i, category in enumerate(categories):
    with cols[i % 4]:
        score = st.number_input(f'{category.split("/")[0]} ({category.split("/")[1]}) 점수',
                                min_value=0, max_value=10, value=5, step=1,
                                key=f'ideal_{i}')
        ideal_values.append(score)

# '차트 생성' 버튼
if st.button('차트 생성'):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    make_radar_chart(categories, current_values, ideal_values, ax)
    st.pyplot(fig)
