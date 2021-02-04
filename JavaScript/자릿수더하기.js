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