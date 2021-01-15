/* level 1 같은 숫자는 싫어
주어진 배열 arr에서 연속적으로 나타나는 숫자를 제거(배열 순서는 유지) */

function solution(arr) {
    var answer = []
    var now = answer.slice(0)
    arr.forEach(element => {
        if (element != now){
            answer.push(element)
            now = element
        }
    });
    return answer;
}

// console.log(solution([2,2, 3,3,5,2,2]));

/* filter
: 주어진 함수의 테스트를 통과하는 모든 요소를 모야 새로운 배열로 반환하는 메서드
*/
//example
var filtered = [1,2,3,4,5].filter((value) => {
    if (value >= 3) { return value;}
})
console.log(filtered)

function solution2(arr) {
    return arr.filter((num, index) => num != arr[index + 1]);
}