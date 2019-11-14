##이상한나라의 문자 만들기
def solution(n):
    answer = ''
    remainder_dict = {0:'4',1:'1',2:'2'}
    mok = 1
    remainder = 1
    while mok != 0:
        mok = n // 3
        remainder = n % 3
        if remainder == 0:
            mok -= 1
        n = mok
        answer = remainder_dict[remainder] +answer
    return answer

##트럭문제
def solution(bridge_length, weight, truck_weights):
    answer = 0
    cross_truckweights=0
    truck_weights = []
    cross_truck =[]
    while truck_weights == []:
        for a in truck_weights:
            cross_truck = truck_weights[0].pop()
            cross_truckweights += cross_truck
            if weight >= cross_truckweights:
                pass
            else:
                cross_truckweights -= cross_truck:



                bridge_length -= 1
            else:







    return answer

