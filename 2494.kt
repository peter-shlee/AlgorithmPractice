import java.io.BufferedWriter
import kotlin.math.min

// 숫자 맞추기
// https://www.acmicpc.net/problem/2494

fun main() {
    val (n, start, dest) = input()
    val dp = Array(n) { IntArray(10) { -1 } }
    val writer = System.out.bufferedWriter()
    writer.write("${solve(start, dest, dp, 0, 0)}\n")
    printPath(start, dest, dp, 0, 0, writer)
    writer.flush()
}

fun input(): Triple<Int, CharArray, CharArray> {
    val reader = System.`in`.bufferedReader()
    val n = reader.readLine().toInt()
    val start = reader.readLine().toCharArray()
    val dest = reader.readLine().toCharArray()

    return Triple(n, start, dest)
}

fun solve(startNum: CharArray, destNum: CharArray, dp: Array<IntArray>, leftCount: Int, index: Int): Int {
    if (index == dp.size) return 0

    val numAtIndex = ((startNum[index].code - '0'.code) + leftCount) % 10
    val targetNum = destNum[index].code - '0'.code
    if (dp[index][numAtIndex] != -1) return dp[index][numAtIndex]

    var currentLeftCount = (targetNum - numAtIndex)
    if (currentLeftCount < 0) currentLeftCount += 10

    var rightCount = (numAtIndex - targetNum)
    if (rightCount < 0) rightCount += 10

    dp[index][numAtIndex] = min(
        solve(startNum, destNum, dp, leftCount + currentLeftCount, index + 1) + currentLeftCount,
        solve(startNum, destNum, dp, leftCount, index + 1) + rightCount
    )

    return dp[index][numAtIndex]
}

fun printPath(startNum: CharArray, destNum: CharArray, dp: Array<IntArray>, leftCount: Int, index: Int, writer: BufferedWriter) {
    if (index == dp.size) return

    val numAtIndex = ((startNum[index].code - '0'.code) + leftCount) % 10
    val targetNum = destNum[index].code - '0'.code

    var currentLeftCount = (targetNum - numAtIndex)
    if (currentLeftCount < 0) currentLeftCount += 10

    var rightCount = (numAtIndex - targetNum)
    if (rightCount < 0) rightCount += 10

    val leftAnswer = solve(startNum, destNum, dp, leftCount + currentLeftCount, index + 1) + currentLeftCount
    val rightAnswer = solve(startNum, destNum, dp, leftCount, index + 1) + rightCount

    if (min(leftAnswer, rightAnswer) == 0) return
    if (leftAnswer < rightAnswer) {
        writer.write("${index + 1} $currentLeftCount\n")
        printPath(startNum, destNum, dp, leftCount + currentLeftCount, index + 1, writer)
    } else {
        writer.write("${index + 1} -$rightCount\n")
        printPath(startNum, destNum, dp, leftCount, index + 1, writer)
    }

    return
}