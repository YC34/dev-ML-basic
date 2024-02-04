## ML 기초
* 미국(캘리포니아) 주택 가격 예측모델 만들기
* > longitude : 경도   
  > latitude : 위도  
  > housing_median_age : 중간 주택 나이 (한 블록 그룹마다의 중앙값?)  
  > total_rooms : 총 방 갯수  
  > total_bedrooms : 침술 갯수  
  > population : 인구 수   
  > households : 그룹의 가구의 수?   
  > median_income : 그룹 소득의 중앙값  
  > median_house_value : 중간 주택 가격  
  > ocean_proximity : 바다와의 거리?   

* 결론은 캘리포니아의 각 그룹별 데이터를 가지고 분석을 시작 할 것이다.  
  각 그룹은 (600~3000)명을 한 그룹으로 나눈것 같다.
  (나의 생각으로는 ocean_proximity 범주로 나누지 않았을까 하는 생각이 든다. )
  각 그룹의 대표값으로는 평균값이 아닌 중앙값으로 하였다.(이상치에 많이 영향을 받지 않기 위함..?)
* 총 그룹의 수는 20640정도 될것이라고 생각이 든다.? 
 

* > + object 타입을 제외한 컬럼에 대한 막대 그래프
    ![housing_hist.png](images%2Fhousing_hist.png)
* > 중간 소득 median_income은 US달러로 작성된것이 아닌, 상한이 15, 하한이 0.5가 되도록 하였다.  
  > 1 : 1만 달러  >> 15만 달러 ~ 5천 달러