package Programmers.NonCompany.Lv0;// https://school.programmers.co.kr/learn/courses/30/lessons/120807

import java.util.Arrays;
import java.util.List;
import java.util.Map;

/*
constraints:
  • 0 ≤ num1 ≤ 10,000
  • 0 ≤ num2 ≤ 10,000
*/

class Solution {
    public int solution(int num1, int num2) {
        return num1 == num2 ? 1 : -1;
    }
}

/*
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 71,398명, 정답률 91%
*/

public class 숫자_비교하기 {
    public static void main(String[] args) {
        List<Map<String, Object>> inputdatas = List.of(
                Map.of("data", Arrays.asList(2, 3), "answer", -1),
                Map.of("data", Arrays.asList(11, 11), "answer", 1),
                Map.of("data", Arrays.asList(7, 99), "answer", -1)
        );

        Solution solution = new Solution();

        for (Map<String, Object> inputdata : inputdatas) {
            Object data = inputdata.get("data");
            Object ans = inputdata.get("answer");

            int num1 = (int) ((List<Object>) data).get(0);
            int num2 = (int) ((List<Object>) data).get(1);
            Object res = solution.solution(num1, num2);

            if (res.equals(ans)) {
                System.out.println("pass");
            } else {
                String summary = "fail";
                summary += "\n  expected:\n";
                summary += "    " + ans;
                summary += "\n  got:\n";
                summary += "    " + res;
                System.out.println(summary);
            }
        }
    }
}

