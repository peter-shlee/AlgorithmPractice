
import java.util.*
import kotlin.math.abs

// 숨바꼭질 2
// https://www.acmicpc.net/problem/12851

fun main() {
    val (start, dest) = input()
    val (minTime, count) = solve(start, dest)
    println(minTime)
    println(count)
}

fun input(): Pair<Int, Int> {
    val reader = Scanner(System.`in`)
    val start = reader.nextInt()
    val dest = reader.nextInt()

    return Pair(start, dest)
}

fun solve(start: Int, dest: Int): Pair<Int, Int> {
    val dp = IntArray(100000 * 2) { -1 }
    val queue: Queue<Int> = LinkedList()
    var count = 0

    queue.add(start)
    dp[start] = 0

    while (!queue.isEmpty()) {
        val cur =  queue.poll()
        if (cur == dest) {
            count += 1
            continue
        }

        var next = cur - 1
        if (next >= 0 && (dp[next] == -1 || dp[next] == dp[cur] + 1)) {
            dp[next] = dp[cur] + 1
            queue.add(next)
        }

        next = cur + 1
        if (next <= dest && (dp[next] == -1 || dp[next] == dp[cur] + 1)) {
            dp[next] = dp[cur] + 1
            queue.add(next)
        }

        next = cur * 2
        if (abs(next - dest) <= abs(dest - cur) && (dp[next] == -1 || dp[next] == dp[cur] + 1)) {
            dp[next] = dp[cur] + 1
            queue.add(next)
        }
    }

    return Pair(dp[dest], count)
}