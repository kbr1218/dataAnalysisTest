# Part04_prac02
### 00. 제공 데이터
# weatherAUS_y_train.csv: 일자별 강수 여부 데이터(학습용) >> Date, RainTomorrow(No/Yes)
# weatherAUS_X_train.csv: 일자별 호주 기상 데이터(학습용)
# weatherAUS_X_test.csv: 일자별 호주 기상 데이터(평가용)
# 제출: Date, RainTomorrow_Prob (강수 여부 예측 확률) >> AUC로 채점
# 참고) 시계열성 고려X

### 01. 데이터셋 불러오기
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("\n\n--------------------------- 데이터셋 불러오기")
X_train = pd.read_csv('../../data/연습문제/weatherAUS_X_train.csv')
X_test = pd.read_csv('../../data/연습문제/weatherAUS_X_test.csv')
y_train = pd.read_csv('../../data/연습문제/weatherAUS_y_train.csv')


### 02. 데이터셋 확인
print("\n\n--------------------------- 데이터셋 확인")
print("\nX_train의 shape: ", X_train.shape)          # (11714, 20)
print("\nX_train의 info: ", X_train.info())
# print("\nX_train의 head: ", X_train.head())

print("\nX_test의 shape: ", X_test.shape)            # (5794, 20)
print("\nX_test의 info: ", X_test.info())
# print("\nX_test의 head: ", X_test.head())

print("\ny_train의 shape: ", y_train.shape)           # (11714, 2)
print("\ny_train의 info: ", y_train.info())
# print("\ny_train의 head: ", y_train.head())


### 03. 기초통계량 확인
print("\n\n--------------------------- 기초통계량 확인")
print("\nX_train의 기초통계량: \n", X_train.describe())
print("\nX_test의 기초통계량: \n", X_test.describe())
print("\ny_train의 기초통계량: \n", y_train.describe())


### 04. 불필요한 컬럼 삭제
# X_test의 Date 컬럼은 따로 저장하고 Date 컬럼 삭제
print("\n\n--------------------------- Date 컬럼 삭제")
Date = X_test['Date'].copy()
X_train = X_train.drop(columns = 'Date', axis = 1)
X_test = X_test.drop(columns = 'Date', axis = 1)
y_train = y_train.drop(columns = 'Date', axis = 1)

### 05. 결측치 확인
print("\n\n--------------------------- 결측치 확인")
# print("\nX_train 결측치: \n", X_train.isnull().sum())
# print("\nX_test 결측치: \n", X_test.isnull().sum())
# print("\ny_train 결측치: \n", y_train.isnull().sum())      # 없음

# X_train에서 결측치가 500개 넘는 칼럼은 삭제
col_null_500 = (X_train.isnull().sum() > 500)           # 500개 넘는 컬럼
col_null_500_name = X_train.columns[col_null_500]       # 리스트로 저장
X_train = X_train.drop(columns = col_null_500_name, axis = 1)   # X_train 삭제
X_test = X_test.drop(columns = col_null_500_name, axis = 1)     # X_test 삭제

# 다시 X_train이랑 X_test df 확인
print("\n\n--------------------------- 컬럼 삭제 후 데이터셋 확인")
print("\nX_train의 shape: ", X_train.shape)          # (11714, 8)
print("\nX_train의 info: ", X_train.info())
print("\nX_train의 head: \n", X_train.head())

print("\nX_test의 shape: ", X_test.shape)            # (5794, 8)
print("\nX_test의 info: ", X_test.info())
print("\nX_test의 head: \n", X_test.head())

# 결측치 다시 확인
print("\n\n--------------------------- 결측치 다시 확인")
# print("\nX_train 결측치: \n", X_train.isnull().sum())
# print("\nX_test 결측치: \n", X_test.isnull().sum())

# 결측치가 있는 수치형 데이터는 평균대치
X_train_conti = X_train.select_dtypes(['int', 'float64'])
X_test_conti = X_test.select_dtypes(['int', 'float64'])

# 평균대치
X_train_conti = X_train_conti.fillna(X_train_conti.mean())
X_test_conti = X_test_conti.fillna(X_test_conti.mean())

# print("\n\n--------------------------- 결측치 다시 확인")
# print("\nX_train_conti 결측치: \n", X_train_conti.isnull().sum())
# print("\nX_test_conti 결측치: \n", X_test_conti.isnull().sum())

# 명목형 RainToday는 최빈값으로 대치
X_train_cate = X_train.select_dtypes('object').copy()
X_test_cate = X_test.select_dtypes('object').copy()

# 최빈값으로 대치
print("\n\n--------------------------- 명목형 최빈값 확인")
mode = X_train_cate.value_counts('RainToday')
print("\n최빈값: \n", mode)  # No     8837, Yes    2793 >> No로 대치

X_train_cate = X_train_cate.fillna('No')
X_test_cate = X_test_cate.fillna('No')

# print("\n\n--------------------------- 결측치 다시 확인")
# print("\nX_train_cate 결측치: \n", X_train_cate.isnull().sum())
# print("\nX_test_cate 결측치: \n", X_test_cate.isnull().sum())

# 두 데이터프레임 합치기 (X_train_conti + X_train_cate)
print("\n\n--------------------------- df 합치기")
X_train = pd.concat( [X_train_conti, X_train_cate], axis = 1)
X_test = pd.concat( [X_test_conti, X_test_cate], axis = 1)
print("\nX_train의 shape: ", X_train.shape)          # (11714, 8)
print("\nX_test의 shape: ", X_test.shape)            # (5794, 8)


### 06. 데이터 분할
print("\n\n--------------------------- 데이터 분할")
from sklearn.model_selection import train_test_split
X_TRAIN, X_VAL, y_TRAIN, y_VAL = train_test_split(X_train,
                                                  y_train,
                                                  random_state = 1234,
                                                  test_size = 0.3)
print("\nX_TRAIN의 shape: ", X_TRAIN.shape)        # (8199, 8)
print("\nX_VAL의 shape: ", X_VAL.shape)            # (3515, 8)
print("\ny_TRAIN의 shape: ", y_TRAIN.shape)        # (8199, 1)
print("\ny_VAL의 shape: ", y_VAL.shape)            # (3515, 1)


### 07. One-Hot Encoding
from sklearn.preprocessing import OneHotEncoder
print("\n\n--------------------------- 원핫인코딩")
X_TRAIN_cate = X_TRAIN.select_dtypes('object').copy()
X_VAL_cate = X_VAL.select_dtypes('object').copy()
X_TEST_cate = X_test.select_dtypes('object').copy()

# 원핫인코딩
enc = OneHotEncoder(sparse = False).fit(X_TRAIN_cate)

X_TRAIN_oh = enc.transform(X_TRAIN_cate)
X_VAL_oh = enc.transform(X_VAL_cate)
X_TEST_oh = enc.transform(X_TEST_cate)


### 08. 스케일링
from sklearn.preprocessing import StandardScaler
print("\n\n--------------------------- 스케일링")
# 스케일링할 컬럼만 저장
X_TRAIN_conti = X_TRAIN.select_dtypes(['int', 'float64']).copy()
X_TEST_conti = X_test.select_dtypes(['int', 'float64']).copy()
X_VAL_conti = X_VAL.select_dtypes(['int', 'float64']).copy()

# TRAIN 데이터 기준으로 스케일링
scale = StandardScaler().fit(X_TRAIN_conti)

# z-score 표준화
X_TRAIN_std = scale.transform(X_TRAIN_conti)
X_TEST_std = scale.transform(X_TEST_conti)
X_VAL_std = scale.transform(X_VAL_conti)


### 09. 입력 데이터셋 준비
print("\n\n--------------------------- 입력데이터셋 준비")
X_TRAIN = np.concatenate( [X_TRAIN_oh, X_TRAIN_std], axis = 1)
X_VAL = np.concatenate( [X_VAL_oh, X_VAL_std], axis = 1)

# Yes/No를 1, 0에 매핑
y_TRAIN = y_TRAIN['RainTomorrow'].map( {'No':0, 'Yes':1} )
y_VAL = y_VAL['RainTomorrow'].map( {'No':0, 'Yes':1} )

# 1차원 넘파이 배여로 평탄화
y_TRAIN = y_TRAIN.values.ravel()
y_VAL = y_VAL.values.ravel()


### 10. 모델학습 (랜덤포레스트)
print("\n\n--------------------------- 랜덤포레스트")
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 500,
                            max_depth = 3,
                            min_samples_leaf = 10,
                            max_features = 'sqrt',
                            random_state = 2022)

model_rf = rf.fit(X_TRAIN, y_TRAIN)


### 11. 성능평가
print("\n\n--------------------------- 성능평가 AUC")
from sklearn.metrics import roc_curve, auc

score_rf = model_rf.predict_proba(X_VAL)[:, 1]
fpr, tpr, thresholds = roc_curve(y_VAL, score_rf)
AUC = auc(fpr, tpr)
print("\n랜덤포레스트의 AUC: ", AUC)


### 12. 결과 제출
print("\n\n--------------------------- 결과 제출")
X_TEST = np.concatenate( [X_TEST_oh, X_TEST_std], axis = 1)
y_score = model_rf.predict_proba(X_TEST)[:, 1]

obj = {'Date': Date,
       'RainTomorrow': y_score}
result = pd.DataFrame(obj)

print("\nresult의 shape: ", result.shape)      # (5794, 2)
print("\nresult의 info: \n", result.info())
print("\nresult의 head: \n", result.head())

result.to_csv('part04_연습문제03_답.csv', index = False)