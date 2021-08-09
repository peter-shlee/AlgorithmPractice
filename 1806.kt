import kotlin.math.min

// 부분합
// https://www.acmicpc.net/problem/1806

lateinit var nums: List<Int>
lateinit var sums: List<Int>
var s = 0

fun main() {
    input()
    println(solve())
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val (n, _s) = reader.readLine().split(" ").map { it.toInt() }
    s = _s
    nums = reader.readLine().split(" ").map { it.toInt() }
    sums = nums.scan(0) { acc, i -> acc + i }
}

fun solve(): Int {
    var i = 1
    var j = 0
    var minLength = 987654321

    while (i < sums.size) {
        if (sums[i] - sums[j] < s) {
            i += 1
        } else {
            minLength = min(minLength, i - j)
            j += 1
        }

        if (i <= j) i += 1
    }

    return if (minLength == 987654321) {
        0
    } else {
        minLength
    }
}