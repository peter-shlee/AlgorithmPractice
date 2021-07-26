import java.util.*
import kotlin.math.max
import kotlin.math.min

// 연산자 끼워넣기
// https://www.acmicpc.net/problem/14888

lateinit var nums: IntArray
val operators = mutableListOf(0, 0, 0, 0)
const val PLUS = 0
const val MINUS = 1
const val MULTIPLICATION = 2
const val DIVISION = 3
var minNum = 1234567890
var maxNum = -1234567890

fun main() {
    input()
    solve()
    println(maxNum)
    println(minNum)
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    nums = IntArray(n)

    for (i in 0 until n) {
        nums[i] = reader.nextInt()
    }

    for (operator in PLUS..DIVISION) {
        operators[operator] = reader.nextInt()
    }
}

fun solve() {
    calc(nums[0], 1)
}

fun calc(currentNum: Int, currentIndex: Int) {
    if (currentIndex == nums.size) {
        maxNum = max(maxNum, currentNum)
        minNum = min(minNum, currentNum)
    }

    for (operator in PLUS..DIVISION) {
        if (operators[operator] > 0) {
            val nextNum = when (operator) {
                PLUS -> {
                    currentNum + nums[currentIndex]
                }
                MINUS -> {
                    currentNum - nums[currentIndex]
                }
                MULTIPLICATION -> {
                    currentNum * nums[currentIndex]
                }
                else -> {
                    currentNum / nums[currentIndex]
                }
            }

            operators[operator] -= 1
            calc(nextNum, currentIndex + 1)
            operators[operator] += 1
        }
    }
}