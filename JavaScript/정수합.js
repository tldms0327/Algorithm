/* level 1 두 정수 사이의 합 
    정수 a, b 사이에 속한 모든 정수의 합 구하기*/

function solution(a, b) {
    if (a===b) {return a;}
    else{
        var answer = 0
        var i = Math.min(a, b)
        for (var i = Math.min(a, b); i < Math.max(a, b); i ++){
            answer += i 
        }
        return answer;
        }
}

