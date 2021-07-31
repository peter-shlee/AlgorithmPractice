// 구간 합 구하기 5
// https://www.acmicpc.net/problem/11660

val dp = mutableListOf<MutableList<Int>>()

fun main() {
    val reader = System.`in`.bufferedReader()
    val writer = System.out.bufferedWriter()
    val (n, m) = reader.readLine().split(" ").map { it.toInt() }
    dp.add(MutableList(n + 1) { 0 })
    for (i in 1..n) {
        dp.add(MutableList(n + 1) { 0 })

        var sum = 0
        reader.readLine().split(" ").mapIndexed { index, s ->
            val j = index + 1
            val num = s.toInt()
            sum += num
            dp[i][j] = sum + dp[i - 1][j]
        }
    }

    for (i in 0 until m) {
        val (r1, c1, r2, c2) = reader.readLine().split(" ").map { it.toInt() }
        val value = dp[r2][c2] - dp[r1 - 1][c2] - dp[r2][c1 - 1] + dp[r1 - 1][c1 - 1]
        writer.write("$value\n")
    }

    writer.flush()
}