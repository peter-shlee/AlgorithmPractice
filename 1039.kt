import java.lang.Integer.max
import java.util.*

// 교환
// https://www.acmicpc.net/problem/1039

fun main() {
    val (n, k) = input()

    print(solve(n, k))
}

fun input(): Pair<Int, Int> {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    val k = reader.nextInt()

    return Pair(n, k)
}

fun int2ArrayList(num: Int): ArrayList<Int> {
    val numList = arrayListOf<Int>()
    var currentNum = num

    while (currentNum > 0) {
        numList.add(currentNum % 10)
        currentNum /= 10
    }
    numList.reverse()

    return numList
}

fun arrayList2Int(numArrayList: ArrayList<Int>): Int {
    var num = 0

    for (n in numArrayList) {
        num *= 10
        num += n
    }

    return num
}

fun solve(n: Int, k: Int): Int {
    var answer = -1
    val queue = ArrayDeque<Pair<Int, Int>>()
    val visited = mutableMapOf<Int, MutableSet<Int>>()

    queue.add(Pair(n, 0))
    for (i in 0..k) {
        visited[i] = mutableSetOf()
    }
    visited[0]?.add(n)

    while (!queue.isEmpty()) {
        val (curN, curK) = queue.first
        queue.removeFirst()
        val nextK = curK + 1

        if (curK == k) {
            answer = max(answer, curN)
            continue
        }

        val numArrayList = int2ArrayList(curN)

        for (i in 0 until numArrayList.size - 1) {
            for (j in i + 1 until numArrayList.size) {
                if (i == 0 && numArrayList[j] == 0) continue
                numArrayList[i] = numArrayList[j].also { numArrayList[j] = numArrayList[i] }

                val changedNum = arrayList2Int(numArrayList)
                if (visited[nextK]?.contains(changedNum) == false) {
                    visited[nextK]?.add(changedNum)
                    queue.add(Pair(changedNum, nextK))
                }

                numArrayList[i] = numArrayList[j].also { numArrayList[j] = numArrayList[i] }
            }
        }
    }

    return answer
}