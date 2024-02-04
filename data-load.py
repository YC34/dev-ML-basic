from pathlib import Path
import pandas as pd
import tarfile
import urllib.request



## 데이터 로드 메소드
def load_housing_data():
    tarball_path = Path("step_01/datasets/housing.tgz") ## 불러올 파일 위치 지정
    if not tarball_path.is_file():
        Path("step_01/datasets").mkdir(parents=True,exist_ok=True) ## 위의 경로가 없으면 파일 만든다.
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url,tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="step_01/datasets")
    return pd.read_csv("step_01/datasets/housing/housing.csv")

housing = load_housing_data()

print(housing.head())
print(housing.info())

print(housing['ocean_proximity'].value_counts()) ## 데이터의 타입이 object인 것들을 탐색
print(housing.describe())


## 시각화를 위한 matplotlib import
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(12,8))
plt.show()