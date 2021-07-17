import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

fun main() {
    val (n, cases) = input()
    val dp = Array(cases.size) { IntArray(cases.size) { -1 } }
    val minCount = solve(n, cases, 0, 1, dp)
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    writer.write("$minCount\n")
    path(n, cases, 0, 1, dp, writer)
    writer.flush()
}

fun input(): Pair<Int, IntArray> {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val n = reader.readLine().toInt()
    val w = reader.readLine().toInt()
    val cases = IntArray(w + 2) { 0 }

    cases[0] = 0
    cases[1] = n * n - 1
    for (i in 2 until w + 2) {
        val (a, b) = reader.readLine().split(" ").map { it.toInt() }
        cases[i] = (a - 1) * n + b - 1
    }

    return Pair(n, cases)
}

fun solve(n: Int, cases: IntArray, first: Int, second: Int, dp: Array<IntArray>): Int {
    val index = max(first, second)

    if (index == cases.size) return 0

    if (dp[first][second] != -1) return dp[first][second]

    var firstDist = 0
    var secondDist = 0
    if (index + 1 < cases.size) {
        val firstR = cases[first] / n
        val firstC = cases[first] % n
        val secondR = cases[second] / n
        val secondC = cases[second] % n
        val nextR = cases[index + 1] / n
        val nextC = cases[index + 1] % n
        firstDist = abs(firstR - nextR) + abs(firstC - nextC)
        secondDist = abs(secondR - nextR) + abs(secondC - nextC)
    }

    dp[first][second] = min(solve(n, cases, index + 1, second, dp) + firstDist,
            solve(n, cases, first, index + 1, dp) + secondDist)

    return dp[first][second]
}

fun path(n: Int, cases: IntArray, first: Int, second: Int, dp: Array<IntArray>, writer: BufferedWriter) {
    val index = max(first, second)

    if (index == cases.size) return

    var firstDist = 0
    var secondDist = 0
    if (index + 1 < cases.size) {
        val firstR = cases[first] / n
        val firstC = cases[first] % n
        val secondR = cases[second] / n
        val secondC = cases[second] % n
        val nextR = cases[index + 1] / n
        val nextC = cases[index + 1] % n
        firstDist = abs(firstR - nextR) + abs(firstC - nextC)
        secondDist = abs(secondR - nextR) + abs(secondC - nextC)
    }

    val firstCost = solve(n, cases, index + 1, second, dp) + firstDist
    val secondCost = solve(n, cases, first, index + 1, dp) + secondDist

    if (index + 1 < cases.size) {
        if (firstCost < secondCost) {
            writer.write("1\n")
            path(n, cases, index + 1, second, dp, writer)
        } else {
            writer.write("2\n")
            path(n, cases, first, index + 1, dp, writer)
        }
    }

    return
}