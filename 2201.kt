val fibonacciDp = MutableList(100) { -1L }
var k = 0L
lateinit var dp: List<MutableList<Long>>
var length = 0

fun main() {
    input()
    if (k == 1L) println(1)
    else {
        solve()
        print(1)
        track(1, 0)
        println()
    }
}

fun input() {
    val reader = System.`in`.bufferedReader()
    k = reader.readLine().toLong()
}

fun solve() {
    var count = 0L
    while (true) {
        length += 1
        if (count + fibonacci(length) >= k) {
            break
        }
        count += fibonacciDp[length]
    }

    k -= count
    dp = List(2) { MutableList(length) { -1L } }
    dp[0][0] = 0
    dp[1][0] = dfs(1,  0)
}

fun dfs(index: Int, current: Int): Long {
    if (index == length - 1) {
        dp[current][index] = 1L
        return 1L
    }

    if (dp[current][index] != -1L) {
        return dp[current][index]
    }

    dp[current][index] = 0
    dp[current][index] += dfs(index + 1,  0)
    if (current == 0) {
        dp[current][index] += dfs(index + 1, 1)
    }

    return dp[current][index]
}

fun track(index: Int, current: Int) {
    print(current)
    if (index == length - 1) {
        return
    }

    if (k <= dp[0][index + 1] || current == 1) {
        track(index + 1,  0)
    } else {
        if (current != 1){
            k -= dp[0][index + 1]
        }
        track(index + 1, 1)
    }
}

fun fibonacci(n: Int): Long {
    if (n < 2) {
        fibonacciDp[n] = n.toLong()
        return fibonacciDp[n]
    }

    if (fibonacciDp[n] != -1L) {
        return fibonacciDp[n]
    }

    fibonacciDp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacciDp[n]
}