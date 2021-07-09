// 퍼즐
// https://www.acmicpc.net/problem/1525

import java.util.*
import kotlin.collections.ArrayDeque

fun main(args: Array<String>) {
    val board = input()
    println(solve(board))
}

fun input(): Array<Int> {
    val reader = Scanner(System.`in`)

    val board = Array(3 * 3) { _ -> 0 }

    for (i in 0..2) {
        for (j in 0..2) {
            board[i * 3 + j] = reader.nextInt()
        }
    }

    return board
}

fun solve(board: Array<Int>): Int {
    var startIndex = 0
    var answer = -1

    for (i in 0..board.size) {
        if (board[i] == 0) {
            startIndex = i
            break
        }
    }

    val queue: ArrayDeque<Triple<Int, Array<Int>, Int>> = ArrayDeque()
    queue.add(Triple(startIndex, board, 0))

    val visited: MutableSet<Int> = mutableSetOf(board2key(board))

    while (!queue.isEmpty()) {
        val (currentIndex, currentBoard, currentCount) = queue.first()
        val nextCount = currentCount + 1
        queue.removeFirst()

        if (checkSolved(currentBoard)) {
            answer = currentCount
            break
        }

        if (currentIndex / 3 > 0) {
            val nextIndex = currentIndex - 3
            val nextBoard = move(currentBoard, currentIndex, nextIndex)
            val nextBoardKey = board2key(nextBoard)

            if (!visited.contains(nextBoardKey)) {
                queue.add(Triple(nextIndex, nextBoard, nextCount))
                visited.add(nextBoardKey)
            }
        }

        if (currentIndex / 3 < 2) {
            val nextIndex = currentIndex + 3
            val nextBoard = move(currentBoard, currentIndex, nextIndex)
            val nextBoardKey = board2key(nextBoard)

            if (!visited.contains(nextBoardKey)) {
                queue.add(Triple(nextIndex, nextBoard, nextCount))
                visited.add(nextBoardKey)
            }
        }

        if (currentIndex % 3 > 0) {
            val nextIndex = currentIndex - 1
            val nextBoard = move(currentBoard, currentIndex, nextIndex)
            val nextBoardKey = board2key(nextBoard)

            if (!visited.contains(nextBoardKey)) {
                queue.add(Triple(nextIndex, nextBoard, nextCount))
                visited.add(nextBoardKey)
            }
        }

        if (currentIndex % 3 < 2) {
            val nextIndex = currentIndex + 1
            val nextBoard = move(currentBoard, currentIndex, nextIndex)
            val nextBoardKey = board2key(nextBoard)

            if (!visited.contains(nextBoardKey)) {
                queue.add(Triple(nextIndex, nextBoard, nextCount))
                visited.add(nextBoardKey)
            }
        }
    }

    return answer
}

fun checkSolved(board: Array<Int>): Boolean {
    for (i in 0..7) {
        if (board[i] == i + 1) continue
        else return false
    }

    return true
}

fun move(board: Array<Int>, currentIndex: Int, nextIndex: Int): Array<Int> {
    val boardCopy = board.copyOf()

    boardCopy[currentIndex] = boardCopy[nextIndex]
    boardCopy[nextIndex] = 0

    return boardCopy
}

fun board2key(board: Array<Int>): Int {
    var key = 0

    for (num in board) {
        key *= 10
        key += num
    }

    return key
}