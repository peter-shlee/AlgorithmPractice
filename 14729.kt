import java.util.*
import kotlin.math.min

// 빗물
// https://www.acmicpc.net/problem/14719

lateinit var blocks: MutableList<Int>

fun main() {
    input()
    println(solve(0, blocks.size - 1))
}

fun input() {
    val reader = Scanner(System.`in`)
    val h = reader.nextInt()
    val w = reader.nextInt()
    blocks = MutableList(w) { 0 }
    for (i in 0 until w) {
        blocks[i] = reader.nextInt()
    }
}

fun solve(start: Int, end: Int): Int {
    var nextIndex = -1

    for (i in start + 1 until end) {
        if (blocks[i] >= blocks[start] || blocks[i] >= blocks[end]) {
            nextIndex = i
            break
        }
    }

    if (nextIndex != -1) {
        println(nextIndex)
        return solve(start, nextIndex) + solve(nextIndex, end)
    }

    val height = min(blocks[start], blocks[end])
    var answer = 0
    for (i in start + 1 until end) {
        answer += height - blocks[i]
    }

    return answer
}