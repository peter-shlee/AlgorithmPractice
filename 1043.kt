import java.util.*
import kotlin.math.max

// 거짓말
// https://www.acmicpc.net/problem/1043

lateinit var memo: MutableList<Int>
lateinit var party: MutableList<MutableList<Int>>

fun main() {
    input()
    println(solve(0))
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    val m = reader.nextInt()
    memo = MutableList(n + 1) { -1 }

    val t = reader.nextInt()
    for (i in 0 until t) {
        val p = reader.nextInt()
        memo[p] = 1
    }

    party = MutableList(m) { mutableListOf<Int>() }
    for (i in 0 until m) {
        val count = reader.nextInt()

        for (j in 0 until count) {
            party[i].add(reader.nextInt())
        }
    }
}

fun solve(index: Int): Int {
    if (index == party.size) return 0

    var curLieCount = -1
    var curNoLieCount = -1
    var canLieFlag = true
    var truthFlag = true
    val prevMemo = MutableList(memo.size) { 0 }
    for (i in memo.indices) {
        prevMemo[i] = memo[i]
    }

    for (p in party[index]) {
        if (memo[p] == 1) {
            canLieFlag = false
            break
        }
    }

    for (p in party[index]) {
        if (memo[p] == 0) {
            truthFlag = false
            break
        }
    }

    if (canLieFlag) {
        for (p in party[index]) {
            memo[p] = 0
        }
        curLieCount = solve(index + 1) + 1
        if (curLieCount == 0) curLieCount = -1
        for (p in party[index]) {
            memo[p] = prevMemo[p]
        }
    }

    if (truthFlag) {
        for (p in party[index]) {
            memo[p] = 1
        }
        curNoLieCount = solve(index + 1)
        for (p in party[index]) {
            memo[p] = prevMemo[p]
        }
    }

    return max(curLieCount, curNoLieCount)
}