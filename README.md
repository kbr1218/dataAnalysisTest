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

<br>
<br>

4. **모분산 검정**  
   4-1. **단일표본에 대한 모분산 검정**  
     - 불러오기: `from scipy.stats import chi2`
     - 클래스: `scipy.stats.chi2(df, ...)`
       - **df**: 자유도
     - 함수: `카이제곱분포객체.cdf(x, ...)` 
        - **x** : 관측값(여기서는 검정 통계량 입력)
     - e.g.
       - 좌측검정은 Pr[chisq2(자유도) < 검정통계량] -> `chi2.cdf(x, df)`
       - 우측검정은 Pr[chisq2(자유도) > 검정통계량] -> `1 - chi2.cdf(x, df)`
       - 양측검정은 (2 * 좌측검정의 유의확률) 또는 (2 * 우측검정의 유의확률) -> `2 * chi2.cdf(x, df)`
     - 결괏값: (p-value)
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택)
     - e.g. 가설이 "모분산이 1,100보다 작다"이고 p-value가 0.05 미만이면 모분산이 1,100보다 작다고 할 수 있음

       <br>

   4-2. **이표본에 대한 분산비 검정 (등분산성 검정)**
     - 두 집단 간의 분산 비교
     - 불러오기: `from scipy.stats import f`
       - **dfn**: 자유도1 (일반적으로 분모에 한 유도)
       - **dfd**: 자유도2 (일반적으로 분자에 한 유도)
     - 함수: `F분포객체.cdf(x, df1, df2, ...)`
        - **x** : 관측값(여기서는 검정 통계량 입력)
     - e.g.
       - 좌측검정은 Pr[F(자유도1, 자유도2) < 검정통계량]
       - 우측검정은 Pr[F(자유도1, 자유도2) > 검정통계량]
       - 양측검정 & 검정통계량이 1보다 작은 경우
           - Pr[F(자유도1, 자유도2) < 검정통계량] + Pr[F(자유도2, 자유도1) > 1/검정통계량]
       - 양측검정 & 검정통계량이 1보다 큰 경우
           - Pr[F(자유도1, 자유도2) > 검정통계량] + Pr[F(자유도2, 자유도1) < 1/검정통계량]
     - 결괏값: (p-value)
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택)
     - e.g. 가설이 "a모분산 < b모분산"이고 p-value가 0.05 미만이면 a집단 모분산이 b집단의 분산보다 작다고 할 수 있음

       <br>

   4-3. **Bartlett 검정 (등분산성 검정)**
     - 두 집단 **이상**의 분산비교 (정규성을 충족하는 데이터에 사용)
     - 불러오기: `from scipy.stats import bartlett`
     - 함수: `scipy.stats.bartlett(a, b, c, ...) 또는 bartlett(a, b, c)`
        - **a, b, c** : 1차원 데이터(리스트, 배열, 시리즈 등)
     - 결괏값: (p-value)
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택) >> 그룹 간의 분산에 유의미한 차이가 있다

       <br>

   4-4. **Levene 검정 (등분산성 검정 - 비모수)**
     - 두 집단 **이상**의 분산 비교 (정규성을 충족하지 않는 데이터에 사용
     - 표본이 적은 경우, 표본이 정규분포를 따르지 않는 경우 사용 가능
     - 불러오기: `from scipy.stats import levene`
     - 함수: ```levene(a, b, c)```
        - **a, b, c** : 1차원 데이터(리스트, 배열, 시리즈 등)
     - 결괏값: (p-value)
     - p-value가 유의확률 0.05 미만 >> 귀무가설 기각 (대립가설 채택) >> 그룹 간의 분산에 유의미한 차이가 있다

<br>
<br>

4. **분산분석 (두 집단 이상의 모평균을 검정하기 위함)**  


