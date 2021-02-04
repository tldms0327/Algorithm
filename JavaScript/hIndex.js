function solution(citations) {
    
    for (var h = Math.max.apply(null, citations); h >= 0; --h ) {
        var count = 0
        citations.forEach(c => {
            if (c >= h){
                count += 1;
            }
        }
        )
        if (count >= h){
            return h
        }
    }
}

// sort하고 index와 비교하기
// 효율성 good
function solution2(citations) {
    var answer = 0;

    citations.sort((a, b) => b - a);

    for(let i = 0; i < citations.length; i++) {
        if(citations[i] > i) answer++;
        else break;
    }

    return answer;
}