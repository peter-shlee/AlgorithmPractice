import java.util.*
import kotlin.math.min

// 사회망 서비스(SNS)
// https://www.acmicpc.net/problem/2533

val tree: MutableMap<Int, MutableSet<Int>> = mutableMapOf()
lateinit var dp: List<MutableList<Int>>

fun main() {
    input()
    println(min(solve(1, -1, 0), solve(1, -1, 1)))
    println(dp[0].toString())
    println(dp[1].toString())
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()

    for (i in 0 until n - 1) {
        val a = reader.nextInt()
        val b = reader.nextInt()

        if (tree[a] == null) {
            tree[a] = mutableSetOf()
        }
        tree[a]?.add(b)

        if (tree[b] == null) {
            tree[b] = mutableSetOf()
        }
        tree[b]?.add(a)
    }

    dp = List(2) { MutableList(n + 1) { -1 } }
}

fun solve(index: Int, prev: Int, earlyAdapter: Int): Int {
    if (index == dp[earlyAdapter].size) return 0

    if (dp[earlyAdapter][index] != -1) {
        return dp[earlyAdapter][index]
    }

    var mustBeEarlyAdapter = true
    var edgeFlag = true

    var minValue = 0
    tree[index]?.let {
        for (next in it) {
            if (next == prev) continue
            edgeFlag = false

            val nextIfEarlyAdapter = solve(index + 1, index, 1)
            val nextIfNotEarlyAdapter = solve(index + 1, index, 0)
            if (nextIfEarlyAdapter < nextIfNotEarlyAdapter) {
                mustBeEarlyAdapter = false
            }
            minValue += min(nextIfEarlyAdapter, nextIfNotEarlyAdapter)
        }
    }

    dp[earlyAdapter][index] = if (mustBeEarlyAdapter && earlyAdapter == 0 && !edgeFlag) {
        987654321
    } else if (earlyAdapter == 1) {
        minValue + 1
    } else {
        minValue
    }

    return dp[earlyAdapter][index]
}
