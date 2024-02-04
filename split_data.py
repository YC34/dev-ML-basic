import numpy as np
import data_load as data

housing = data.load_housing_data()
# def shuffle_and_split_data(data, test_radio):
#     shuffled_indices = np.random.permutation(len(data)) ## 좋은 방법은 아니다. 난수를 지정하여 초기값을 지정해줘야 한다. 매번 돌릴떄마다 달라지기 때문.
#     test_set_size = int(len(data) * test_radio)
#     test_indices = shuffled_indices[:test_set_size]
#     train_indices = shuffled_indices[test_set_size:]
#     return data.iloc[train_indices] , data.iloc[test_indices]
#
# train_set , test_set = shuffle_and_split_data(housing,0.2) ## 위에서 가져온 데이터를 적용, 20프로만큼을 test데이터로 만든다.
# print(len(train_set)) ## 16512
# print(len(test_set))  ## 4128

## 위의 방법은 매번 실행 할 때마다 , 데이터가 보존되지않고 변경이 되므로 다른 방법을 사용해야한다.
## 이전에 훈련 세트에 있던 샘플은 포함 되지 않기 위함.


from zlib import crc32
def is_id_in_test_set(identifier,test_ratio):
    return crc32(np.int64(identifier)) <test_ratio * 2**32

def split_data_with_id_hash(data,test_ratio,id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_ : is_id_in_test_set(id_,test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


## data에 식별 컬럼이 없으므로, 행의 인덱스를 ID로 만든다.
housing_with_id = housing.reset_index()
# print(housing_with_id.loc[1])
train_set,test_set = split_data_with_id_hash(housing_with_id,0.2,"index")
print(len(train_set))
print(len(test_set))
