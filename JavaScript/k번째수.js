{/* level 1 K번째 수
array와 command[i, j, k] 배열이 주어졌을 때, 
array의 i~j번째 숫자까지 자르고 정렬했을 때 k번째 수를 구하기 */}

function solution(array, commands) {
    var temp = [];
    var answer = [];
    for (var i = 0; i < commands.length; i ++) {
        var temp = array.slice(commands[i][0] - 1, commands[i][1]) 
        temp.sort(function(a, b) { return a- b; }) // ASCII 문자 순으로 정열되기 때문에 sorting 기준 명시
        answer.push(temp[commands[i][2] - 1])
    }

    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4]	, [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	))

// 다른 사람 풀이로 js 문법을 더 익혀보쟈

function solution2(array, commands) {
    return commands.map(command => { // for -> map
        const [i, j, k] = command 
        const newArray = array
            .filter((value, fIndex) => fIndex >= i - 1 && fIndex <= j - 1) // sliccing
            .sort((a, b) => a - b) // function을 안 써도 되는구나
            
        return newArray[k - 1]
    })
}

