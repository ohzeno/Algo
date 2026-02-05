// https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=javascript
package main

import (
	"fmt"
	"reflect"
	"strings"
)

/*
constraints:

*/

func solution(s string) string {
	ss := strings.Split(s, " ")
	res := []string{}
	for _, word := range ss {
		if len(word) == 0 {
			res = append(res, word)
			continue
		}
		word = strings.ToUpper(string(word[0])) + strings.ToLower(word[1:])
		res = append(res, word)
	}
	return strings.Join(res, " ")
}

/*
연습문제
Lv.2. 현 시점 완료한 사람 44,487명, 정답률 80%
go는 string을 UTF-8 인코딩된 byte 배열로 다루기 때문에 단일 인덱싱은 byte(uint8)을 반환한다.
string(word[0])을 안하면 byte를 그대로 가져와 숫자가 되버린다.
*/

func main() {
	inputDatas := []struct {
		data   []any
		answer any
	}{
		{data: []any{"3people unFollowed me"}, answer: "3people Unfollowed Me"},
		{data: []any{"for the last week"}, answer: "For The Last Week"},
	}

	for i := 0; i < len(inputDatas); i++ {
		tc := inputDatas[i]

		fnValue := reflect.ValueOf(solution)
		args := make([]reflect.Value, len(tc.data))
		for j, arg := range tc.data {
			args[j] = reflect.ValueOf(arg)
		}
		results := fnValue.Call(args)
		res := results[0].Interface()

		if reflect.DeepEqual(res, tc.answer) {
			fmt.Println("pass")
		} else {
			summary := "fail"
			for _, pair := range [][]any{{"expected:", tc.answer}, {"got:", res}} {
				label := pair[0]
				content := pair[1]
				summary += fmt.Sprintf("\n  %v\n", label)
				summary += fmt.Sprintf("    %v", content)
				summary = strings.TrimRight(summary, " \t")
			}
			fmt.Println(summary)
		}
	}
}
