
import java.util.*

// LCS2
// https://www.acmicpc.net/problem/9252

fun main() {
    val (a, b) = input()
    val dp = Array(a.length) { Array<String?>(b.length) { null } }
    val answer = solve(a, b, 0, 0, dp)
    println(answer.length)
    if (answer.isNotEmpty()) println(answer)
}

fun input(): Pair<String, String> {
    val reader = Scanner(System.`in`)
    val a = reader.next()
    val b = reader.next()

    return Pair(a, b)
}

fun solve(a: String, b: String, aIndex: Int, bIndex: Int, dp: Array<Array<String?>>): String {
    if (a.length <= aIndex || b.length <= bIndex) return ""

    dp[aIndex][bIndex]?.let {
        return it
    }

    var nextBIndex = -1
    for (i in bIndex until b.length) {
        if (b[i] == a[aIndex]) {
            nextBIndex = i + 1
            break
        }
    }

    if (nextBIndex != -1)
        dp[aIndex][bIndex] =  a[aIndex] + solve(a, b, aIndex + 1, nextBIndex, dp)

    val tmpString = solve(a, b, aIndex + 1, bIndex, dp)
    if (dp[aIndex][bIndex]?.length ?: 0 < tmpString.length)
    dp[aIndex][bIndex] = tmpString

    return dp[aIndex][bIndex] ?: ""
}