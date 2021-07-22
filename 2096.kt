import java.util.*
import kotlin.math.max
import kotlin.math.min

// 내려가기
// https://www.acmicpc.net/problem/2096

lateinit var nums: List<MutableList<Int>>

fun main() {
    input()
    println("${solveMax()} ${solveMin()}")
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()

    nums = List(n) { MutableList(3) { 0 } }

    for (i in 0 until n) {
        nums[i][0] = reader.nextInt()
        nums[i][1] = reader.nextInt()
        nums[i][2] = reader.nextInt()
    }
}

fun solveMin(): Int {
    val prev = mutableListOf(nums[0][0], nums[0][1], nums[0][2])
    val cur = mutableListOf(nums[0][0], nums[0][1], nums[0][2])

    for (index in 1 until nums.size) {
        cur[0] = min(prev[0] + nums[index][0], prev[1] + nums[index][0])
        cur[1] = min(min(prev[0] + nums[index][1], prev[1] + nums[index][1]), prev[2] + nums[index][1])
        cur[2] = min(prev[1] + nums[index][2], prev[2] + nums[index][2])

        for (j in 0..2) {
            prev[j] = cur[j]
        }
    }

    return min(min(cur[0], cur[1]), cur[2])
}

fun solveMax(): Int {
    val prev = mutableListOf(nums[0][0], nums[0][1], nums[0][2])
    val cur = mutableListOf(nums[0][0], nums[0][1], nums[0][2])

    for (index in 1 until nums.size) {
        cur[0] = max(prev[0] + nums[index][0], prev[1] + nums[index][0])
        cur[1] = max(max(prev[0] + nums[index][1], prev[1] + nums[index][1]), prev[2] + nums[index][1])
        cur[2] = max(prev[1] + nums[index][2], prev[2] + nums[index][2])

        for (j in 0..2) {
            prev[j] = cur[j]
        }
    }

    return max(max(cur[0], cur[1]), cur[2])
}