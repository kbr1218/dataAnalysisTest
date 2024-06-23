# 빅데이터분석기사 실기 정리

<br>

## 💡 참고 교재

<div>
  <a href="https://www.dataedu.kr/">
    <img src="https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791197889509.jpg" width="124px" height="180px">
  </a>
</div>

<br>

## 💡 패키지
1. NumPy
2. Pandas
3. SciPy
4. scikit-learn
5. statsmodels

<br>

## 💡 환경 설정
#### 판다스 행/열 최대 출력
```python
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
```

#### 경고 메시지 숨기기
```python
import warnings
warnings.filterwarnings(action = 'ignore')
```

<br>

## 💡 정규성 검정 
#### 샤피로-윌크 검정
```python
from scipy.stats import shapiro
shapiro(x)
# x: 1차원 데이터
```
- 결괏값: (통계량, p-value)
- p-value > 0.05면 귀무가설 채택 >> 정규성 만족

<br>

## 💡 상관분석
#### 피어슨 상관계수
- 연속형 변수 간 일대일 상관성 확인
```python
from scipy.stats import pearsonr
pearsonr(x, y)
# 또는
df[ [x, y] ].corr()
# x, y: 1차원 데이터
```
- 결괏값: (상관계수, p-value)
- p-value < 0.05면 귀무가설 기각 >> 유의미한 상관관계

<br>

## 💡 카이제곱 검정
#### 적합도 검정 (chisquare)
```python
from scipy.stats import chisquare
chisquare(f_obs, f_exp)
# f_obs: 관측도수
# f_exp: 기대도수
```
- 결괏값: (statistic, p-value)
- p-value < 0.05면 귀무가설 기각

<br>

#### 동질성 검정 (chi2_contigency)
```python
from scipy.stats import chi2_contingency
chi, pvalue, dof, expected = chi2_contigency(df)
# df: R X C 교차표로 된 데이터프레임
```
- 결괏값: ( chi(카이제곱통계량), pvalue, dof(자유도), expected(기대빈도) )
- p-vlaue < 0.05면 귀무가설 기각

<br>

#### 독립성 검정 (chi2_contigency)
```python
from scipy.stats import chi2_contigency
chi, pvalue, dof, expected = chi2_contigency(df)
# df: R X C 교차표로 된 데이터프레임
```
- 결괏값: ( chi(카이제곱통계량), pvalue, dof(자유도), expected(기대빈도) )
- p-vlaue < 0.05면 귀무가설 기각

<br>

#### 교차표 만들기
```python
import pandas as pd
pd.crosstab(index, columns, ...)
# index: 교차표 상 행으로 들어갈 데이터
# columns: 교차표 상 열로 들어갈 데이터
```

<br>

## 💡 모평균검정 T-test
#### 단일표본 t-검정
- 모집단 X의 평균(하나의 표본)에 대한 가설 검정 (모집단 평균과 표본평균 비교)
```python
from scipy.stats import ttest_1samp
ttest_1samp(a, popmean, alternative = 'two-sided')
# a: 1차원 데이터
# popmean: 귀무가설에서 설정된 값
# alternative: 대립가설 정의
    # 'two-sided': popmean과 다름 (default)
    # 'less': popmean보다 작음
    # 'greater': popmean보다 큼
```
- 결괏값: (t통계량값, p-value)
- p-value < 0.05면 귀무가설 기각

<br>

#### 대응표본 t-검정
- 서로 대응되는 두 집단(표본 크기 같음)의 평균의 차이 검정 (2개의 연속형 변수)
- 두 표본이 하나의 모집단에서 옴 >> 등분산 가정 성립
```python
from scipy.stats import ttest_rel
ttest_rel(a, b, alternative = 'two-sided')
# a, b: 1차원 데이터
# alternative: 대립가설 정의
    # 'two-sided': 두 표본의 평균의 차이(a-b)가 0이 아님 (default)
    # 'less': 두 표본의 평균의 차이(a-b)가 0보다 작음
    # 'greater': 두 표본의 평균의 차이(a-b)가 0보다 큼
```
- 결괏값: (t통계량값, p-value)
- p-value < 0.05면 귀무가설 기각

<br>

#### 독립표본 t-검정
- 서로 독립인 두 모집단 간 평균 비교 (2개의 범주형 집단에 따른 연속형 자료의 평균 비교)
- 두 표본이 하나의 모집단에서 옴 >> 등분산 가정 성립
```python
from scipy.stats import ttest_ind
ttest_ind(a, b, equal_var = True, alternative = 'two-sided')
# a, b: 1차원 데이터
# equal_var: 등분산 여부
    # True: 등분산 (default)
    # False: 이분산
# alternative: 대립가설 정의
    # 'two-sided': 두 표본의 평균의 차이(a-b)가 0이 아님 (default)
    # 'less': 두 표본의 평균의 차이(a-b)가 0보다 작음
    # 'greater': 두 표본의 평균의 차이(a-b)가 0보다 큼
```
- 결괏값: (t통계량값, p-value)
- p-value < 0.05면 귀무가설 기각

<br>

## 💡 모분산 검정
#### 단일표본 모분산 검정
```python
from scipy.stats import chi2
chi2.cdf(x, dof)
# x: 관측값 (여기서는 검정통계량)
# dof: 자유도

# e.g.
# 좌측검정: Pr[chisq2(dof) < 검정통계량] >> chi2.cdf(x, dof)
# 우측검정: Pr[chisq2(dof) > 검정통계량] >> 1 - chi2.cdf(x, dof)
# 양측검정: (2 * 좌측검정의_유의확률) 또는 (2 * 우측검정의_유의확률) >> 2 * chi2.cdf(x, dof)
```
- 결괏값 (p-value)
- p-value < 0.05면 귀무가설 기각

<br>

#### 이표본에 대한 분산비 검정
```python
from scipy.stats import f
f.cdf(x, dof1, dof2)
# x: 관측값 (여기서는 검정통계량 == (집단a의_분산 / 집단b의_분산)
# dof1: 자유도 (일반적으로 분모에 대한 자유도)
# dof2: 자유도 (일반적으로 분자에 대한 자유도)

# e.g.
# 좌측검정: Pr[F(dof1, dof2) < 검정통계량]
# 우측검정: Pr[F(dof1, dof2) > 검정통계량]
# 양측검정 & 검정통계량이 1보다 작은 경우: Pr[F(dof1, dof2) < 검정통계량] + Pr[F(dof2, dof1) > 1/검정통계량]
# 양측검정 & 검정통계량이 1보다 큰 경우: Pr[F(dof1, dof2) > 검정통계량] + Pr[F(dof2, dof1) < 1/검정통계량]

```
- 결괏값 (p-value)
- p-value < 0.05면 귀무가설 기각

<br>

## 💡 등분산 검정
#### 이표본 이상에 대한 Bartlett 검정 (정규성을 충족하는 데이터에 대해)
```python
from scipy.stats import bartlett
bartlett(a, b, c)
# a, b, c: 1차원 데이터
```
- 결괏값: (검정통계량, p-value)
- p-value < 0.05면 귀무가설 기각

<br>

#### 이표본 이상에 대한 Levene 검정 (정규성을 충족하지 않는 데이터에 대해)
```python
from scipy.stats import levene
levene(a, b, c)
# a, b, c: 1차원 데이터
```
- 결괏값: (검정통계량, p-value)
- p-value < 0.05면 귀무가설 기각

<br>

## 💡 분산분석
#### 일원배치 분산분석
```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
one_way = ols('반응변수~ C(그룹변수)', data = df).fit()
# '반응변수~ C(그룹변수)': 모형에 대한 식
# df: 데이터프레임
anova_lm(one_way)
# one_way = 적합된 모형
```
- 결괏값: ( dof(자유도), sum_sq(합계제곱), mean_sq(평균제곱), F, Pr(>F) )
- Pr(>F) < 0.05면 귀무가설 기각
- 사후검정 수행 필요

#### 사후검정 (Tukey의 HSD)
```python
from statsmodels.multicomp import pairwise_tukeyhsd
pairwise_tukeyhsd(endog = df['반응변수'], groups = df['그룹변수'], alpha = 0.05)
# endog: 반응변수 (1차원 데이터)
# groups: 그룹변수 (1차원 데이터)
# alpha: 유의수준
```
- 결괏값: ( meandiff(두 그룹 간 평균 차이), lower/upper(95%의 신뢰구간), reject )  
  \>\> 신뢰구간에 0을 포함: 해당 그룹 간 평균 차이가 없음  
  \>\> 신뢰구간에 0을 포함하지 않음: 해당 그룹 간 평균 차이가 있음  
  \>\> reject로도 확인 가능 (False- 유의미한 차이 없음, True- 유의미한 차이 있음)

<br>

#### 이원배치 분산분석
```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# 교호작용이 있는 경우
two_way = ols('반응변수~ C(그룹변수1) + C(그룹변수2) + C(그룹변수1):C(그룹변수2)', data = df).fit()
# '반응변수~ C(그룹변수1) + C(그룹변수2) + C(그룹변수1):C(그룹변수2)': 모형에 대한 식
# df: 데이터프레임
anova_lm(two_way)
# two_way: 적합된 모형
```
- 결괏값: ( dof(자유도), sum_sq(합계제곱), mean_sq(평균제곱), F, Pr(>F) )
- ```C(그룹변수1):C(그룹변수2)의 Pr(>F)``` > 0.05면 상호작용 효과가 유의하지 않음 >> 교호작용 제외하고 다시 수행

```python
# 교호작용 제외하고 다시 수행
two_way = ols('반응변수~ C(그룹변수1) + C(그룹변수2)', data = df).fit()
# '반응변수~ C(그룹변수1) + C(그룹변수2)': 모형에 대한 식
# df: 데이터프레임
anova_lm(two_way)
# two_way: 적합된 모형
```
- Pr(>F) < 0.05면 귀무가설 기각 >> 평균에 유의한 차이가 있음

<br>

## 💡 비모수 검정
#### 스피어만 상관계수 검정 (spearmanr)
```python
from scipy.stats import spearmanr
spearmanr(a, b)
# a, b: 1차원 데이터
# 또는
df[ [x, y] ].corr(method = 'spearmanr')
```
- 결괏값: (statistic, p-value)
- p-value < 0.05면 귀무가설 기각
- 순위 데이터에 대해서도 검정 수행 가능

<br>

#### 켄달의 타우 검정 (kendalltau)
```python
from scipy.stats import kendalltau
kendalltau(x, y)
# x, y: 순서가 있는 1차원 데이터
```
- 결괏값: (상관계수, p-value)
- 상관계수가 낮으면 순위 간 상관관계가 거의 없는 것임
- p-value < 0.05면 귀무가설 기각

<br>

#### 윌콕슨의 부호순위 검정 (wilcoxon)
```python
from scipy.stats import wilcoxon
# 일표본일 경우
wilcoxon(x - y)
# x: 순서가 있는 1차원 데이터
# y: 평균 (일표본이므로 하나의 숫자)
```
- 결괏값: ( 검정통계량, p-value )
- p-value < 0.05 면 귀무가설 기각

```python
from scipy.stats import wilcoxon
# 이표본일 경우
wilcoxon(x - y)
# x, y: 순서가 있는 1차원 데이터
```
- 결괏값: ( 검정통계량, p-value )
- p-value < 0.05 면 귀무가설 기각

<br>

#### 만-위트니 U 검정 (mannwhitneyu)
```python
from scipy.stats import mannwhitneyu
mannwhitneyu(x, y)
# x, y: 순서가 있는 1차원 데이터
```
- 결괏값: ( 검정통계량, p-value )
- p-value < 0.05 면 귀무가설 기각

<br>

#### 크루스칼-왈리스 H 검정 (kruskal)
```python
from scipy.stats import kruskal
kruskal(a, b, c, ...)
# a, b, c: 순서가 있는 1차원 데이터
```
- 결괏값: ( 검정통계량, p-value )
- p-value < 0.05 면 귀무가설 기각

<br>

## 💡 선형회귀
#### 단순선형회귀
```python
from scipy.stats import linregress
model = linregress(x, y)
# x, y: 1차원 데이터
```
- 결괏값: ( slope, intercept, rvalue, pvale, stderr, intercept_stderr )  
  \>\> slope: 독립변수에 대한 추정된 회귀계수 (beta 1)   
  \>\> intercept: 상수항 (beta 0)  
  \>\> rvalue: 모형의 설명력 (결정계수)  
  \>\> pvalue: 기울기에 대한 통계적 유의성  
  \>\> stderr & intercept_stderr: 회귀계수들에 대한 표준오차  
- 회귀식: target = intercept + (독립변수*slope)

<br>

#### 다중선형회귀
```python
import statsmodels.api as sm
X = df[ ['IV1', 'IV2'] ]     # 독립변수
y = df['DV']                 # 종속변수
X = sm.add_constant(X)       # 상수항 추가
model = sm.OLS(y, X).fit()
model.summary()
```
- 결괏값: summary() 함수로 확인 가능
  \>\> const(절편), IV들의 p-value(P>|t|) < 0.05면 DV에 유의한 영향  
  \>\> F-statistic이 크고 Prob(F-statistic) < 0.05면 모델이 전반적으로 유의미  
```python
# 반응변수의 기댓값에 대한 점추정 값 계산 (원래 있던 IV)
X.iloc[n]                  # n번째 관측치 데이터값 확인
model.predict(X.iloc[n])   # n번째 관측치에 대한 DV의 기댓값 추정

# 반응변수의 기댓값 예측 (새로운 IV를 입력)
new_data = pd.DataFrame( {'const': [값], 'IV1': [값], 'IV2': [값]} )      # 새로운 IV 배열을 입력값으로 지정
result = model.get_prediction(new_data)
result.summary_frame()
```
- 결괏값: summary_frame() 함수로 확인 가능
  \>\> mean: DV의 예측 기댓값  
  \>\> mean_ci_lower & mean_ci_upper: 95%에서 예측구간  

<br>

## 💡 로지스틱회귀
#### 로지스틱회귀
```python
import statsmodels.api as sm
X = df[ ['IV1', 'IV2'] ]     # 독립변수
y = df['DV']                 # 종속변수
X = sm.add_constant(X)       # 상수항 추가
model = sm.GLM(y, X, family = sm.families.Binomial()).fit()
# family: 분포와 연결함수 설정 (로지스틱 회귀는 sm.families.Binomial())
model.summary()
coef = model.params
```
- 결괏값: summary() 함수로 확인 가능
  \>\> P>|z| < 0.05면 const(절편)와 IV가 통계적으로 유의미  
- model.params 함수로 const(절편)와 IV의 값 더 자세히 확인 가능

<br>

#### 오즈비 계산
```python
# 그룹A의 오즈 계산
log_odds_A = coef[‘const’] + coef[‘IV’]
odds_A = np.exp(log_odds_A)

# 그룹B의 오즈 계산
log_odds_B = coef[‘const’]
odds_B = np.exp(log_odds_B)

# 오즈비 계산
odds_ratio = odds_A / odds_B

model.deviance             # 모형의 이탈도
model.null_deviance        # 영모형(절편만 있는 모형)의 이탈도
stat = dev0 – dev          # 통계량
dof = 2 – 1                # 자유도 = 적합모형의_회귀계수_수 – 영모형의_회귀계수_수

# 카이제곱 통계량과 자유도
from scipy.stats import chi2
pval = 1 – chi2.cdf(stat, dof)        # 유의확률
```
- 결괏값
  \>\> .null_deviance: 영모형(절편만 있는 모형)의 이탈도  
  \>\> .summary()의 Deviance 값 또는 .deviance: 적합모형의 이탈도  
  \>\> 둘의 차이(null_deviance – deviance)는 자유도가 (적합모형의_회귀계수_수 – 영모형의_회귀계수_수)인 카이제곱 분포 하의 모형 적합성을 위한 검정 통계량이 됨  
  \>\> 1 – chi2.cdf(stat, dof) < 0.05면 모형이 데이터를 잘 적합하고 있음  

<br>
<br>

## 💡 제 2유형 문제풀이 순서 정리
#### 01. 행/열 최대 출력
```python
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
```

<br>

#### 02. df 구조, 기초통계량 확인
```python
df.shape           # X_train, X_test, y_train 데이터셋 모두 확인
df.info()
df.head()
df.describe()
```

<br>

#### 03. X_test의 ID/Date 등 기준이 되는 칼럼 복사 & 삭제
```python
ID = X_test['ID'].copy()                                # 결과 제출할 때 기준 칼럼이 있는 경우 변수에 복사하기
X_train = X_train.drop(columns = 'ID', axis = 1)        # X_train, X_test, y_train에서 모두 삭제
```
- 예측에 불필요한 칼럼도 삭제

<br>

#### 04. 결측치 확인 & 결측값 채우기
```python
X_train.isnull().sum()                                  # 결측치 확인 (X_train, X_test에 모두 적용)
# 수치형 변수
X_train['IV'].fillna(X_train['IV'].mean())              # 평균대치
# 명목형 변수
X_train['IV'].unique()                                  # 칼럼의 유일값 확인
X_train['IV'].value_counts()                            # 칼럼의 유일값별 개수 확인
X_train['IV'].fillna('대치할_값')                        # e.g. 최빈값

# 조건에 따라 결측값 채우기
X_train.loc[조건식, '대치할_IV'] = '대치할_값'
```

<br>

#### 05. 레코드 삭제
```python
# 조건변수를 만든 후 레코드 삭제
condition_na = X_train['IV'].isna()                      # 삭제할 레코드 조건 변수 생성 (여기서는 isna() 함수로 결측치 삭제)
X_train = X_train[~condition_na]
y_train = y_train[~condition_na]
```

<br>

#### 06. 자료형별 데이터프레임 나누기 (수치형 & 명목형)
```python
X_train_conti = X_train.select_dtypes( ['int64', 'float64'] )         # X_test에 대해서도 수행
X_train_cate = X_train.select_dtypes('object')                        # X_test에 대해서도 수행
```
- ```.select_dtypes()```는 원하는 dtype을 가진 데이터프레임만 추출

<br>

#### 07. 수치형 칼럼 전처리
```python
# 백분율 칼럼을 소수점으로 변환
col_per = [ 백분율로 되어있는 칼럼명 ]
X_train_conti[col_per] = X_train[col_per] / 100

# 상관관계 확인
X_train_conti.corr()                                         # 강한 상관관계를 가지는 칼럼이 있다면 하나 정도만 남기고 삭제
X_train_conti.drop(columns = ['삭제할_칼럼'], axis = 1)

# 자료형은 수치형이지만 내용이 명목형이라면 dtype 변경
X_train_conti['IV'].astype('object')
```
- 백분율 처리, 상관관계 확인, dtype 변경 등

<br>

#### 08. 명목형 변수 전처리
```python
# 파생변수 만들기
X_train_cate['age_gp'] = X_train_cate['age'].str[0]           # e.g. 나이 IV를 연령대 파생변수로 만들기

# 공백 제거
X_train_cate['IV'].value_counts()                             # 칼럼의 유일값별 개수 확인
X_train_cate['IV'].str.replace(' ', '')

# 문자열을 분리해서 각각 하나의 열로 저장
X_train_cate[ ['IV1', 'IV2'] ] = X_train_cate['IV'].str.split('기준문자'], expand = True)
```

<br>

#### 09. 두 개의 데이터프레임 합치기
```python
X_train = pd.concat( [X_train_conti, X_train_cate], axis = 1)
X_test = pd.concat( [X_test_conti, X_test_cate], axis = 1)
```

<br>

#### 10. 데이터 분할 (학습용/검증용)
```python
from sklearn.model_selection import train_test_split
X_TRAIN, X_VAL, y_TRAIN, y_VAL = train_test_split(X_train,
                                                  y_train,
                                                  test_size = 0.2,     # 8:2
                                                # stratify = y_train,
                                                  random_state = 1234)

df.shape # 분할한 모든 df에 대해 shape로 크기 확인
```
- ```stratify```는 타겟변수의 비율을 유지하면서 df를 나누는 옵션 (연속형일 경우 생략)

<br>

#### 11. 원-핫 인코딩
```python
from sklearn.preprocessing import OneHotEncoder
X_TRAIN_cate = X_TRAIN.select_dtypes('object').copy()          # X_VAL, X_test에서도 명목형만 저장

enc = OneHotEncoder(handle_unknown = 'ignore', sparse = False).fit(X_TRAIN_cate)
X_TRAIN_oh = enc.transform(X_TRAIN_cate)                       # X_VAL_cate와 X_test_cate에 대해서도 수행
```
- 명목형 변수에 대해서만 원-핫 인코딩 수행
- ```handle_unknown='ignore'```는 train에 없는 레이블이 test에 있더라도 모두 0이 됨

<br>

#### 12. 스케일링 (z-score 표준화)
```python
from sklearn.preprocessing import Standard Scaler
X_TRAIN_conti = X_TRAIN.select_dtypes( ['int64', 'object64'] ).copy()      # X_VAL, X_test에서도 수치형만 저장

scale = StandardScaler().fit(X_TRAIN_conti)                                # X_TRAIN_conti에 대해서만 표준화 객체 생성
X_TRAIN_std = scale.transform(X_TRAIN_conti)                               # X_VAL_conti와 X_test_conti에 대해서도 수행
```

<br>

#### 13. 입력 데이터셋 준비
```python
# 두 개의 데이터 (_oh와 _std) 합치기
X_TRAIN = np.concatenate( [X_TRAIN_oh, X_TRAIN_std], axis = 1)
X_VAL = np.concatenate( [X_VAL_oh, X_VAL_std], axis = 1)
X_test = np.concatenate( [X_test_oh, X_test_std], axis = 1)

# y데이터에서 yes를 1로, no를 0으로 매핑 (연속형 변수가 아니라면)
y_TRAIN = y_TRAIN['DV'].map( {'No': 0, 'Yes': 1} )
y_VAL = y_VAL['DV'].map( {'No': 0, 'Yes': 1} )

# 1차원 넘파이 배열로 평탄화
y_TRAIN = y_TRAIN.values.ravel()
y_VAL = y_VAL.values.ravel()
```

<br>

#### 14. 모델학습 (랜덤포레스트)
```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegresor

# Classifier (범주형 목표변수: 이진분류, 다중클래스 분류)
rf = RandomForestClassifier( n_estimators = 500,
                             max_depth = 3,
                             min_samples_leaf = 10,
                             max_features = 'sqrt',
                             random_state = 1234)
model_rf = rf.fit(X_TRAIN, y_TRAIN)

# Regressor (연속형 목표변수 예측)
rf = RandomForestRegressor( n_estimators = 500,
                            max_depth = 3,
                            min_samples_leaf = 10,
                            max_features = 50,
                            random_state = 1234)
model_rf = rf.fit(X_TRAIN, y_TRAIN)
```

<br>

#### 15. 성능평가
```python
# AUC (이진분류 모델 성능평가)
from sklearn.metrics import roc_curve, auc

score_rf = model_rf.predict_proba(X_VAL)[:, 1]               # predict_proba는 확률값을 예측
fpr, tpr, thresholds = roc_curve(y_VAL, score_rf)
AUC = auc(fpr, tpr)

# RMSE (회귀모델 성능평가)
from sklearn.metrics import mean_squared_error
pred_rf = model_rf.predict(X_VAL)                            # predict는 확률값 기반 클래스 예측 
rmse = mean_squared_error(y_VAL, pred_rf, squared = False)
```

<br>

#### 16. 예측값 생성
```python
# AUC
y_score = model_rf.predict_proba(X_test)[:, 1]
# RMSE
y_pred = model_rf.predict(X_test)
```

<br>

#### 17. 결과 제출
```python
obj = { 'ID': ID,               # 제출 형식에 ID가 있는 경우
        'DV': y_score }         # 또는 y_pred
result = pd.DataFrame(obj)

result.to_csv('파일이름.csv', index = False)
```











