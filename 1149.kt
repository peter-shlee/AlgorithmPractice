import java.util.*
import kotlin.math.min

// RGB거리
// https://www.acmicpc.net/problem/1149

fun main() {
    val prices = input()
    println(solve(prices))
}

fun input(): ArrayList<IntArray> {
    val reader = Scanner(System.`in`)

    val n = reader.nextInt()
    val prices = ArrayList<IntArray>()

    for (i in 0 until n) {
        val r = reader.nextInt()
        val g = reader.nextInt()
        val b = reader.nextInt()

        prices.add(intArrayOf(r, g, b))
    }

    return prices
}

fun solve(prices: ArrayList<IntArray>): Int {
    val dp = Array(prices.size) { Array(3) { 987654321 } }
    for (i in 0..2) {
        dp[0][i] = prices[0][i]
    }

    for (i in 1 until prices.size) {
        for (j in 0..2) {
            for (k in 0..2) {
                if (j != k) {
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + prices[i][j])
                }
            }
        }
    }

    return min(dp[prices.size - 1][0], min(dp[prices.size - 1][1], dp[prices.size - 1][2]))
}