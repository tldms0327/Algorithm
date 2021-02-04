function solution(n) {
    var answer = 0;
    var sum = 0;
    var count = 1;
    
    while (sum + count <= n){
        sum += count
        if ((n-sum) % count == 0) ++answer;
        count++;
    }
    return answer;
}

// 홀수인 약수의 개수를 세면 된다고..
function expressions(num) {
    var answer = 0;

  for(var i=1; i<=num; i++) {
    if (num%i == 0 && i%2 == 1)
      answer++
  }
    return answer;
}