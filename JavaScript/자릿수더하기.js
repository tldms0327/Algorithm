// my solution
function solution(n)
{
    var answer = 0;
    var str = String(n)
    for (var i = 0; i < str.length; i++) {
        answer += parseInt(str[i])
    }

    return answer;
}

//others
function solution2(n)
{
    var a = (n + '').split('');
    console.log(a)
    var b = 0;
    for(var i = 0; i < a.length; ++i) {
        b += parseInt(a[i]);
    }
    return b;
    //return n.toString().split('').reduce((a, b) => (a * 1) + (b * 1));
}

function solution3(n) {
    var arr = n.toString().split('');
    var sum = 0;
    arr.forEach(element => {
        sum += parseInt(element);
    });
    return sum;
}

function solution4(n,a=0,b=0) {
    return String(n).length==a?b:solution4(n,a+1,b+=String(n)[a]*1);
}
// ===는 자료형까지 모두 같을 때, ==는 자료형 상관없이 들어있는 내용이 같을 때!
// string에 1을 곱하면 int로 형변환