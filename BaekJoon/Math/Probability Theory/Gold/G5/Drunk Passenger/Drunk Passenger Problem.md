# Drunk Passenger Problem

1. [조건부 확률](#조건부-확률)
2. [점화식](#점화식)
3. [단순화](#단순화)

> There are 100 passengers boarding an aircraft. Each passenger in the queue has a specified seat number. The first passenger in a queue is drunk and chooses the seat randomly. For each following passenger, if her/his seat has been occupied, she/he then picks the seat randomly, otherwise she/he goes to the assigned seat. The question is what is the probability that the last person in the queue gets her/his designated seat?

오히려 확률 공부를 안해본 사람들이 찍어서 맞추는 문제.

여러 해설들을 봤지만 대부분이 엄밀하지 못하거나 논리적 비약이 심해서 증명이라고 할 수 없었다. 항상 그렇지만 대부분이 스스로 이해했다고 착각하고 있거나 이해하지 못하고 퍼오는 듯.

<br/>

## 조건부 확률

100번 승객이 자신의 자리에 앉는 사건을 Z, 1번 승객이 i번 자리에 앉는 사건을 $A_i$라 하자.

$$
P(Z) = \sum_{i=1}^{100} P(Z|A_i)\cdot P(A_i) = {1 \over 100}\sum_{i=1}^{100} P(Z|A_i)
$$

우리가 단순화 할 수 있는 케이스가 있다. 1번 승객이 1번에 앉을 경우, 이후 사람들은 모두 자신의 자리에 앉으므로 100번도 자신의 자리에 앉게 된다. 1번 승객이 100번 자리에 앉으면 100번 승객이 자신의 자리에 앉을 수 없다.

$$
P(Z|A_1) = 1, \quad P(Z|A_{100}) = 0
$$

문제는 $A_2$ ~ $A_{99}$​다. A가 다른 자리에 앉으면, 그 자리의 승객이 랜덤으로 앉게 되기 때문이다.

두번째 승객이 j번 자리에 앉는 사건을 $B_j$라고 하자.

$$
P(Z|A_2) = \sum_{j=1,3,...100} P(Z|A_2,B_j) \cdot P(B_j|A_2) = {1 \over 99}\sum_{j=1,3,...100} P(Z|A_2,B_j)
$$

벌써 복잡해진다. 이걸 $Z|A_3$ ~ $Z|A_{99}$까지 모두 구하는 것은 현실적이지 못하다.

<br/>

## 점화식

1번 승객이 i번 자리에 앉는다면, i번 승객은 자신의 좌석이 1번인 취객으로 변한다.

1번 승객이 취객일 때, 1번 승객이 '1번' 자리에 앉으면 100번 승객이 제자리에 앉을 확률이 1로 확정됐다. i번 승객이 1번 자리에 앉는다면 1, i만 서로 자리를 교환한 것이므로 나머지 승객은 제자리에 앉게 되어 마찬가지로 Z가 일어날 확률이 1로 확정된다.

1번 승객이 취객일 때, 1번 승객이 '100번' 자리에 앉으면 100번 승객이 제자리에 앉을 확률이 0으로 확정됐다. i번 승객이 100번 자리에 앉더라도 100번 승객은 제자리에 앉을 확률이 0이 된다.

1번과의 차이점은, 남은 자리수가 하나 줄어들었다는 것이다.

이를 위해 승객이 n명일 때 n번째 승객이 자리에 앉을 확률을 Q(n)이라 하자.

$$
Q(1) = 1, \quad Q(2) = {1 \over 2}
$$

Q(3)부터는 3가지 케이스로 나뉜다.

1.  i번 승객(취객)이 1번에 앉으면 n번 승객은 제자리에 앉을 수 있다.

$$
{1 \over n} \cdot 1
$$

2.  취객이 n번에 앉으면 n번 승객은 제자리에 앉을 수 없다.

$$
{1 \over n} \cdot 0
$$

3.  취객이 i번에 앉으면 n번 승객이 제자리에 앉을 확률은 P(n-1)이 된다.

$$
{1 \over n} \cdot P(n-1)
$$

그런데, 3번 케이스는 n-2개 있다. 1번과 2번을 제외하면 모두 3번 케이스이기 때문(수형도를 그려보면 이해하기 편하다)

$$
{(n-2) \over n} \cdot P(n-1)
$$

즉, Q(n)은 다음과 같다.

$$
\begin{align*}
Q(n) &= {1 \over n} \cdot 1 + {1 \over n} \cdot 0 + {(n-2) \over n} \cdot P(n-1) \newline \newline &= {1 \over n} + {(n-2) \over n} \cdot P(n-1) \quad (n \ge 2)
\end{align*}
$$

Q(1)이 주어졌으므로 dp를 통해 원하는 n의 Q값을 구할 수 있다.

조금 부연 설명을 하면, Q(3)부터는 취객만 취급했다. 이유는 Q(n-1)단계에서 1번이나 100번에 앉았다면 이후 승객의 거취는 검토할 필요가 없이 확률이 확정된다. 그래서 그 둘을 제외한 경우의 수에서 이어진 케이스만 생각하면 취객 케이스가 된다. 위에서도 언급했지만 수형도를 그려보면 이해하기 편하다.

물론 값을 구해보면 다 ${1 \over 2}$이지만, 조건이 다른 [변형 문제](https://www.acmicpc.net/problem/23337)(1번 승객이 절대 1번에 앉지 않음)를 풀 때는 이런 원리를 이해해야 확률을 구해서 점화식을 만들 수 있다.

<br/>

## 단순화

대부분의 해설이 이와 유사하나, 핵심 조건들이 빠져있거나 중간 논리들이 빠져있거나 이상하게 비틀어서 논리적 모순들이 가득하다.

핵심은 **100번 승객은 1번 혹은 100번 좌석에만 탑승할 수 있다**는 것이다.

100번의 차례가 왔을 때, 99개의 좌석이 가득차 있고 하나의 좌석만 남는다.

1. i (99 이하)번 승객이 1번에 앉은 경우(취객이므로 i번 자리는 이미 차있다), i+1 이상의 승객(100번 포함)은 모두 제자리에 앉게 된다. 즉, 100번 차례에서 100번 좌석이 남아있다.
2. i (99 이하)번 승객이 100번에 앉은 경우 i+1~ 99번 승객은 자신의 자리에 앉게 된다. i번 승객이 자신의 자리에 앉지 않았다는 것은, 1번 케이스가 발생하지 않았다는 근거가 된다. 즉, 100번 차례에서 1번 자리가 비어있다.

중간 과정에서의 확률을 보는 것이 아니라 1~99번 승객을 통틀어서 보면 '이지선다'가 된다.

100개의 좌석 중 왜 이지선다인지가 문제인데, 일단 1개의 좌석만 남아있을 것이고, '자신의 자리가 차있으면' 취객이 된다는 조건 때문에 1, 100 이외의 자리가 남을 수가 없다. 

i번(2~99) 좌석이 남으려면 i번 승객이 다른 자리에 앉아야 하는데, i번 자리가 비어있으니 자신의 자리에 앉게 된다. 자신의 자리가 비어있는 상태에서 다른 자리를 택할 수 있는 승객은 1번 뿐이다.

그러니 100번 차례에서 1번이 남을 확률, 100번이 남을 확률만 남는데, 무작위 좌석을 선택하는 모든 승객이 각 좌석을 고를 확률은 균등하다. 그러므로 중간에는 50%가 아니지만 각 무작위 선택에서 1, 100이 선택될 확률이 균등하여 최종적으로 50%의 확률이 된다.

위 내용을 정확하게 이해하지 못하고 단순하게 중간과정에서 1, 100을 선택할 수 있으니 결론도 1/2이라고 주장하는 해설들을 받아들인 경우, 조금만 조건이 변해도 상황 파악이 힘들어진다.

예를 들어, 뒤에서 x번째 승객이 제자리에 앉을 확률은 어떻게 되는가? 이를 R이라 하자.

x-1번째 승객까지가 1번, (100 - x + 1) ~ 100 좌석 중 100 - x + 1번을 선택하지 않았을 확률이 된다. 위에서 봤던 것과 같이 모든 무작위 선택에서 각 좌석이 선택될 확률은 균등하므로, x+1개의 좌석 중 x번이 선택되지 않을 확률은 다음과 같다.

$$
R(x) = {x \over {x+1}}
$$
