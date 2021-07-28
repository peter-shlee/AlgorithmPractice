import java.util.*
import kotlin.math.max
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
    var maxIndex = -1
    var maxValue = -1

    for (i in start + 1 until end) {
        if (maxValue < blocks[i]) {
            maxIndex = i
            maxValue = blocks[i]
        }
    }

    if (blocks[start] <= maxValue || blocks[end] <= maxValue) {
        return solve(start, maxIndex) + solve(maxIndex, end)
    }

    val height = min(blocks[start], blocks[end])
    var answer = 0
    for (i in start + 1 until end) {
        answer += height - blocks[i]
    }

    return answer
}