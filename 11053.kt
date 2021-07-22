import kotlin.math.max

// 가장 긴 증가하는 부분 수열
// https://www.acmicpc.net/problem/11053

lateinit var nums: List<Int>
lateinit var dp: MutableList<Int>

fun main() {
    input()
    println(solve())
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val n = reader.readLine().toInt()
    nums = reader.readLine().split(" ").map { it.toInt() }
    dp = MutableList(n) { 1 }
}

fun solve(): Int {
    for (i in dp.indices) {
        var prevMax = 1
        for (j in i - 1 downTo 0) {
            if (nums[j] < nums[i]) {
                prevMax = max(dp[j] + 1, prevMax)
            }
        }
        dp[i] = prevMax
    }

    return dp.maxOrNull() ?: 0
}