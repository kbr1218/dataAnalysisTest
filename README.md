# 빅데이터분석기사 실기

<br>

## 💡 참고 교재

<div>
  <a href="https://www.dataedu.kr/">
    <img src="https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791197889509.jpg" width="144px" height="200px">
  </a>
</div>

<br>

## 💡 패키지
1. NumPy
2. Pandas
3. SciPy
4. scikit-learn
5. statsmodels
6. Matplotlib

<br>

## 💡 가설 검정

### 모수적 방법
1. **상관분석 (피어슨 상관계수)**
   - 연속형 변수 간 일대일 상관성 확인
   - 불러오기: ```from scipy.stats import pearsonr```
   - 함수: ```pearsonr(x, y)``` 또는 ```df[ [x, y] ].corr()```
     - x, y: 1차원 데이터
   - 결괏값: (상관계수, p-value)
   - p-value가 유의수준(0.05) 미만 >> 귀무가설 기각 (= 대립가설 채택) >> 유의미한 상관계수

<br>

2. **정규성 검정 (샤피로-윌크 검정)**
   - 불러오기: ```from scipy.stats import shapiro```
   - 함수: ```scipy.stats.shapiro(x)``` 또는 ```shapiro(x)```
     - x: 1차원 데이터
   - 결괏값: (통계량, p-value)
   - p-value가 유의수준(0.05) 이상 >> 귀무가설을 기각하지 못함 >> 정규성 만족

<br>

3. **모평균 검정**  
   3-1. **단일표본 t-검정**  
     - 모집단 X의 평균(하나의 표본)에 대한 가설 검정 (모집단 평균과 표본평균 비교)  
     - e.g. 대학생들의 평균 수면 시간은 우리나라 성인 평균 수면 시간과 같은가?  
     - 불러오기: ```from scipy.stats import ttest_1samp```  
     - 함수: ```ttest_1samp(a, popmean, alternative= 'two-sided)```  
        - **a** : 1차원 데이터 (리스트, 배열, 시리즈 등)  
        - **popmean** : 귀무가설에서 설정된 값  
        - **alternative** : 대립가설 정의  
          - 'two-sided' : popmean과 다름 (default)  
          - 'less' : popmean보다 작음  
          - 'greater' : popmean보다 큼  
     - 결괏값: (t통계량값, p-value)  
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택)  

<br>


   3-2. **대응표본 t-검정**  
     - 서로 대응되는 두 집단(표본 크기도 같음)의 평균의 차이 검정 (2개의 연속형 변수의 평균 차이 검증)  
     - 두 표본이 모두 하나의 모집단에서 옴 -> 등분산 가정 성립  
     - 가설: *(변수1)*과 *(변수2)*에는 유의한 차이가 있다  
     - e.g. (품질 만족도)와 (디자인 만족도)에는 유의한 차이가 있다  
     - 불러오기: ```from scipy.stats import ttest_rel```  
     - 함수: ```ttest_rel(a, b, alternative= 'two-sided)```  
        - **a, b** : 1차원 데이터 (리스트, 배열, 시리즈 등)  
        - **alternative** : 대립가설 정의  
          - 'two-sided' : 두 표본의 평균(a-b)의 차이가 0이 아님(default)  
          - 'less' : 두 표본의 평균(a-b)의 차이가 0보다 작음  
          - 'greater' : 두 표본의 평균(a-b)의 차이가 0보다 큼  
     - 결괏값: (t통계량값, p-value)  
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택) >> (변수1)과 (변수2)에는 유의한 차이가 있다  

<br>

   3-3. **독립표본 t-검정**  
     - 서로 독립인 두 모집단 간 평균 비교하는 통계 검정 (2개의 범주형 집단에 따른 연속형 자료의 평균 비교 분석)  
     - 두 표본이 모두 하나의 모집단에서 옴 -> 등분산 가정 성립  
     - 가설: *(독립변수)*에 따라 *(종속변수)*는 유의한 차이가 있다  
     - e.g. (성별)에 따라 (스마트폰 친숙도)는 유의한 차이가 있다  
     - 불러오기: ```from scipy.stats import ttest_ind```  
     - 함수: ```ttest_ind((a, b, equal_var=True, alternative= 'two-sided)```  
        - **a, b** : 1차원 데이터 (리스트, 배열, 시리즈 등)  
        - **equal_var** : 등분산인지 여부 (등분산이면 True, 이분산이면 False) (default = True)  
        - **alternative** : 대립가설 정의  
          - 'two-sided' : 두 표본의 평균(a-b)의 차이가 0이 아님(default)  
          - 'less' : 두 표본의 평균(a-b)의 차이가 0보다 작음  
          - 'greater' : 두 표본의 평균(a-b)의 차이가 0보다 큼  
     - 결괏값: (t통계량값, p-value)  
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택) >> 유의한 차이가 있다  










