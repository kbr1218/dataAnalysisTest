### 00. 제공 데이터
# College_y_train.csv: 미국 대학별 사립 여부 데이터(학습용) -- ID(int), Private(범주; No/Yes)
# College_X_train.csv: 대학별 주요 속성 데이터 (학습용) (651개)
# College_X_test.csv: 대학별 주요 속성 데이터 (평가용) (156개)
# 학습용 데이터로 <사립 여부 예측 모형>을 만든 후 이를 평가용 데이터에 적용하여 <사립 여부 예측값>을 csv 파일로 생성 (AUC 평가지표로 채점)
# 제출 형식: ID (수치형), prob_Private (수치형; 사립대학 여부에 대한 예측 확률)

### 01. 데이터셋 불러오기
import pandas as pd
import numpy as np

# row, col 생략없이 출력
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

X_train = pd.read_csv('../../data/연습문제/College_X_train.csv', encoding = 'cp949')
X_test = pd.read_csv('../../data/연습문제/College_X_test.csv', encoding = 'cp949')
y_train = pd.read_csv('../../data/연습문제/College_y_train.csv', encoding = 'cp949')

### 02. 데이터셋 확인
print("X_train df의 shape: ", X_train.shape)  # (621, 19)
# print("X_train df의 info: ", X_train.info())
# print(X_train.head())
print("------------------------------------------------")

print("X_test df의 shape: ", X_test.shape)    # (156, 19)
# print("X_test df의 info: ", X_test.info())
# print(X_test.head())
print("------------------------------------------------")

print("y_train df의 shape: ", y_train.shape)   # (621, 2)
# print("y_train df의 info: ", y_train.info())
# print(y_train.head())
print("------------------------------------------------")

### 03. 기초통계량 확인
print("X_train df의 기초통계량: \n", X_train.describe())
print("X_test df의 기초통계량: \n", X_test.describe())
# print("y_train df의 기초통계량: \n", y_train.describe())

### 04. 불필요한 칼럼 삭제
# X_test df의 ID 컬럼은 따로 저장하고 ID 컬럼 삭제
# X_train과 X_test df의 Name 컬럼도 모델 생성에 필요 없으므로 삭제
ID = X_test['ID'].copy()

X_train = X_train.drop(columns = ['ID', 'Name'], axis = 1)
X_test = X_test.drop(columns = ['ID', 'Name'], axis = 1)
y_train = y_train.drop(columns = 'ID', axis = 1)

# 삭제 후 데이터셋 다시 확인
# print("\n\nX_train df의 shape: ", X_train.shape)  # (621, 17)
# print("X_train df의 info: ", X_train.info())
# print(X_train.head())
# print("------------------------------------------------")

# print("\n\nX_test df의 shape: ", X_test.shape)    # (156, 17)
# print("X_test df의 info: ", X_test.info())
# print(X_test.head())
# print("------------------------------------------------")

# print("\n\ny_train df의 shape: ", y_train.shape)   # (621, 1)
# print("y_train df의 info: ", y_train.info())
# print(y_train.head())

### 05. 결측치 처리
# print("\n\n\n------------------------------------------결측치 확인")
# print("\nX_train의 결측치: ", X_train.isnull().sum())   # 없음
# print("\nX_test의 결측치: ", X_test.isnull().sum())     # 없음
# print("\ny_train의 결측치: ", y_train.isnull().sum())   # 없음

### 06. 수치형 컬럼 전처리
# Top10perc, Top25perc, PhD, Terminal, S.F.Ratio, perc.alumni, Grad.Rate >> 백분율 컬럼들이니까 소수점으로 변환하기
col_per = ['Top10perc', 'Top25perc', 'PhD', 'Terminal', 'S.F.Ratio', 'perc.alumni', 'Grad.Rate']
X_train[col_per] = X_train[col_per] / 100
X_test[col_per] = X_test[col_per] / 100

# 수치형 컬럼으로 상관관계 확인
print("\n\n\n------------------------------------------상관관계 확인")
# print(X_train.corr())
# Apps-Accept, Apps-Enroll, Apps-F.Undergrad, Accept-Enroll, Accept-F.Undergrad, Enroll - F.Undergrad
# >> Apps-Accept-Enroll-F.Undergrad 에서 강한 상관관계
# Top10perc-Top25perc 에서 강한 상관관계
# PhD-Terminal 에서 강한 상관관계
# Apps, Accept, F.Undergrad, Top25perc, Terminal 컬럼 삭제
col_del = ['Apps', 'Accept', 'F.Undergrad', 'Top25perc', 'Terminal']
X_train = X_train.drop(columns = col_del, axis = 1)
X_test = X_test.drop(columns = col_del, axis = 1)

# 삭제 후 데이터셋 다시 확인
print("\n\nX_train df의 shape: ", X_train.shape)  # (621, 12)
print("X_train df의 info: ", X_train.info())
print(X_train.head())
print("------------------------------------------------")

print("\n\nX_test df의 shape: ", X_test.shape)    # (156, 12)
print("X_test df의 info: ", X_test.info())
print(X_test.head())
print("------------------------------------------------")


### 07. 데이터 분할
# X_train을 X_TRAIN과 X_VAL, y_train을 y_TRAIN과 y_VAL로 분할 (각각 학습용-검증용, 비율은 9:1)
from sklearn.model_selection import train_test_split
X_TRAIN, X_VAL, y_TRAIN, y_VAL = train_test_split(X_train,
                                                  y_train,
                                                  random_state = 1234,
                                                  test_size = 0.1,
                                                  stratify = y_train)

print("\n\n\n------------------------------------------분할 후 shape 확인")
print("\nX_train df의 shape: ", X_train.shape)  # (621, 12)
print("\nX_TRAIN df의 shape: ", X_TRAIN.shape)  # (558, 12)
print("\nX_VAL df의 shape: ", X_VAL.shape)  # (63, 12)
print("\ny_train df의 shape: ", y_train.shape)  # (621, 1)
print("\ny_TRAIN df의 shape: ", y_TRAIN.shape)  # (558, 1)
print("\ny_TEST df의 shape: ", y_VAL.shape)  # (63, 1)

### 08. 인코딩
# 명목형 IV가 없으니 생략

### 09. 스케일링
print("\n\n\n------------------------------------------스케일링")
# 수치형 컬럼에 대해 z-score 표준화 실행
# X_TRAIN의 평균과 표준편차를 X_VAL, X_test에 반영하기 위해 .fit() 메소드를 X_TRAIN에만 적용하고 .transform()은 모든 데이터에 적용하여 표준화
from sklearn.preprocessing import StandardScaler
# X_TRAIN 기준으로 표준화
scale = StandardScaler().fit(X_TRAIN)
# z-score 표준화
X_TRAIN_std = scale.transform(X_TRAIN)
X_VAL_std = scale.transform(X_VAL)
X_TEST_std = scale.transform(X_test)


### 10. 입력 데이터셋 준비 (== 덮어쓰기)
print("\n\n\n------------------------------------------입력데이터셋 준비")
X_TRAIN = X_TRAIN_std
X_VAL = X_VAL_std
y_TRAIN = y_TRAIN.values.ravel()
y_VAL = y_VAL.values.ravel()



### 11. 모델학습 (랜덤포레스트만)
from sklearn.ensemble import RandomForestClassifier

print("\n\n\n------------------------------------------모델학습")
rf = RandomForestClassifier(n_estimators = 500,
                            max_depth = 3,
                            min_samples_leaf = 10,
                            max_features = 'sqrt',
                            random_state = 2022)
model_rf = rf.fit(X_TRAIN, y_TRAIN)

### 12. 성능평가 (AUC)
from sklearn.metrics import roc_curve, auc

print("\n\n\n------------------------------------------성능평가")
score_rf = model_rf.predict_proba(X_VAL)[:, 1]

# AUC 계산
fpr, tpr, thresholds = roc_curve(y_VAL, score_rf, pos_label = 'Yes')
AUC = auc(fpr, tpr)
print("랜덤포레스트 AUC: ", AUC)


### 13. 결과 제출
# X_TEST로 예측 확률을 구하고 csv 파일로 저장
print("\n\n\n------------------------------------------결과 제출")

X_TEST = X_TEST_std
y_score_final = model_rf.predict_proba(X_TEST)[:, 1]

# 문제에서 요구하는 형태로 변환
obj = {'ID': ID,
       'prob_Private': y_score_final}
result = pd.DataFrame(obj)

# result 확인
print(result.head(10))

# csv로 저장
result.to_csv("part04_연습문제02_답.csv", index = False)