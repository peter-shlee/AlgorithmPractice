// 성냥개비
// https://www.acmicpc.net/problem/3687

val m = mapOf(0 to 6, 1 to 2, 2 to 5, 4 to 4, 6 to 6, 7 to 3, 8 to 7).toSortedMap()

val dp = Array(51) { _ -> Array(101) { _ -> -1 } }

fun main() {
    val nums = input()

    for (n in nums) {
        val (minNum, maxNum) = solve(n)
        println("$minNum $maxNum")
    }
}

fun input(): IntArray {
    val br = System.`in`.bufferedReader()

    val t = br.readLine().toInt()
    val nums = IntArray(t)

    for (i in 0 until t) {
        val n = br.readLine().toInt()
        nums[i] = n
    }

    return nums
}

fun solve(n: Int): Pair<String, String> {
    var count = n
    val maxNumber = StringBuilder("")

    if (n % 2 == 1) {
        maxNumber.append("7")
        count -= 3
    }

    while (count > 0) {
        maxNumber.append("1")
        count -= 2
    }

    for (i in 1..50) {
        when (dp[i][n]) {
            0 -> continue
            1 -> {
                count = i
                break
            }
            else -> {
                if (match(n, i, true)) {
                    count = i
                    dp[i][n] = 1
                    break
                } else {
                    dp[i][n] = 0
                }
            }
        }
    }
    val minNumber = StringBuilder()
    makeNumber(n, count, minNumber)

    return Pair(minNumber.toString(), maxNumber.toString())
}

fun match(n: Int, k: Int, isFirst: Boolean): Boolean {
    if (k == 0 && n == 0) return true
    else if (k == 0) return false

    for (i in m.keys) {
        if (isFirst && i == 0) continue

        m[i]?.let {
            if (n - it >= 0)
                when (dp[k - 1][n - it]) {
                    0 -> {
                    }
                    1 -> return true
                    else -> {
                        if (match(n - it, k - 1, false)) {
                            dp[k - 1][n - it] = 1
                            return true
                        } else {
                            dp[k - 1][n - it] = 0
                        }
                    }
                }
        }
    }

    return false
}

fun makeNumber(n: Int, k: Int, s: StringBuilder): Boolean {
    val isFirst = s.isEmpty()
    var returnFlag = false

    if (n == 0 && k == 0) return true
    else if (k == 0) return false

    for (i in 0..9) {
        if (isFirst && i == 0) continue

        m[i]?.let {
            if (n - it >= 0) {
                if (dp[k - 1][n - it] == 0) return@let
                if (dp[k - 1][n - it] == 1 || match(n - it, k - 1, isFirst)) {
                    if (makeNumber(n - it, k - 1, s.append(i))) {
                        returnFlag = true
                        return@let
                    }
                    else s.deleteCharAt(s.length - 1)
                }
            }
        }
        if (returnFlag) return true
    }

    return false
}