import java.util.*

// https://www.acmicpc.net/problem/2248
// 이진수 찾기

var n = 0
var l = 0
var i = 0L
var num = BooleanArray(32) { false }
var count = 0L
val dp = List(32) { LongArray(32) { -1L } }

fun main() {
    input()
    solve()
}

fun input() {
    val reader = Scanner(System.`in`)
    n = reader.nextInt()
    l = reader.nextInt()
    i = reader.nextLong()
}

fun solve() {
    dfs(l, 0)

    for (i in 0 until n) {
        if (num[i]) {
            print("1")
        } else {
            print("0")
        }
    }
    println()
}

fun dfs(remainCount: Int, currentIndex: Int): Boolean {
    if (currentIndex == n) {
        dp[remainCount][currentIndex] = 1L
        count += 1
        return count == i
    }

    if (dp[remainCount][currentIndex] != -1L) {
        if (count + dp[remainCount][currentIndex] < i) {
            count += dp[remainCount][currentIndex]
            return false
        }
    }

    if (dfs(remainCount, currentIndex + 1)) return true
    dp[remainCount][currentIndex] = dp[remainCount][currentIndex + 1]

    if (remainCount > 0) {
        num[currentIndex] = true
        if (dfs(remainCount - 1, currentIndex + 1)) return true
        num[currentIndex] = false
        dp[remainCount][currentIndex] += dp[remainCount - 1][currentIndex + 1]
    }

    return false
}