import kotlin.math.min

var n = 0
var dp = mutableListOf<Int>()

fun main() {
    input()
    solve()
}

fun input() {
    val reader = System.`in`.bufferedReader()
    n = reader.readLine().toInt()
    dp = MutableList(n + 1) { -1 }
}

fun solve() {
    dfs(n)
    println(dp[n])
}

fun dfs(currentNum: Int): Int {
    if (currentNum == 1) {
        dp[currentNum] = 0
        return 0
    }

    if (dp[currentNum] != -1) return dp[currentNum]

    var minCount = 987654321
    if (currentNum % 3 == 0) {
        minCount = min(minCount, dfs(currentNum / 3))
    }

    if (currentNum % 2 == 0) {
        minCount = min(minCount, dfs(currentNum / 2))
    }

    if (currentNum > 1) {
        minCount = min(minCount, dfs(currentNum - 1))
    }

    dp[currentNum] = minCount + 1
    return dp[currentNum]
}