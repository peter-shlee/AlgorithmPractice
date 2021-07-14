import java.lang.Integer.max
import java.lang.Integer.min
import java.util.*

// 카드게임
// https://www.acmicpc.net/problem/11062

fun main() {
    val cards = input()

    for (t in 0 until cards.size) {
        solve(cards[t])
    }
}

fun input(): ArrayList<IntArray> {
    val reader = Scanner(System.`in`)

    val t = reader.nextInt()

    val cards = arrayListOf<IntArray>()

    for (i in 0 until t) {
        val n = reader.nextInt()
        val card = IntArray(n) { 0 }

        for (j in 0 until n) {
            card[j] = reader.nextInt()
        }

        cards.add(card)
    }

    return cards
}

fun solve(cards: IntArray) {
    val dp = Array(cards.size) { IntArray(cards.size) { 0 } }
    println(dfs(cards, 0, cards.size - 1, true, dp))
}

fun dfs(cards: IntArray, s: Int, e: Int, flag: Boolean, dp: Array<IntArray>): Int {
    if (dp[s][e] != 0) return dp[s][e]

    if (s == e) {
        dp[s][e] = if (flag) cards[s] else 0
        return dp[s][e]
    }

    if (flag) {
        dp[s][e] = max(dfs(cards, s + 1, e, false, dp) + cards[s], dfs(cards, s, e - 1, false, dp) + cards[e])
    } else {
        dp[s][e] = min(dfs(cards, s + 1, e, true, dp), dfs(cards, s, e - 1, true, dp))
    }

    return dp[s][e]
}