val direction = mapOf(
    1 to Pair(0, -1),
    2 to Pair(-1, -1),
    3 to Pair(-1, 0),
    4 to Pair(-1, 1),
    5 to Pair(0, 1),
    6 to Pair(1, 1),
    7 to Pair(1, 0),
    8 to Pair(1, -1)
)

fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    var board: Array<Array<Int>> = arrayOf()
    var clouds: Array<Array<Int>> = createEmptyCloud(n)

    clouds[n - 1][0] = 1
    clouds[n - 1][1] = 1
    clouds[n - 2][0] = 1
    clouds[n - 2][1] = 1

    for (i in 1..n) {
        val line = readLine()!!.split(" ").map { it.toInt() }.toTypedArray()
        board = board.plus(line)
    }

    for (i in 1..m) {
        val (d, s) = readLine()!!.split(" ").map { it.toInt() }

        // 1. move & 2. repair & 3. raining cloud
        val dir = direction[d]!!
        var movedClouds = createEmptyCloud(n)
        for (x in 0 until n) {
            for (y in 0 until n) {
                if (clouds[x][y] == 1) {
                    val repairX = repairPosition(x + (dir.first * s), n)
                    val repairY = repairPosition(y + (dir.second * s), n)

                    movedClouds[repairX][repairY] = 1
                    board[repairX][repairY] += 1
                }
            }
        }
        clouds = movedClouds.copyOf()

        for (x in 0 until n) {
            for (y in 0 until n) {
                if (clouds[x][y] == 1) {
                    if (x - 1 >= 0 && y - 1 >= 0) {
                        if (board[x - 1][y - 1] > 0)
                            board[x][y] += 1
                    }

                    if (x - 1 >= 0 && y + 1 < n) {
                        if (board[x - 1][y + 1] > 0)
                            board[x][y] += 1
                    }

                    if (x + 1 < n && y - 1 >= 0) {
                        if (board[x + 1][y - 1] > 0)
                            board[x][y] += 1
                    }

                    if (x + 1 < n && y + 1 < n) {
                        if (board[x + 1][y + 1] > 0)
                            board[x][y] += 1
                    }
                }
            }
        }

        // 5. create cloud, delete previous cloud
        var newClouds = mutableListOf<Pair<Int, Int>>()
        for (x in 0 until n) {
            for (y in 0 until n) {
                if (board[x][y] >= 2) {
                    if (clouds[x][y] != 1) {
                        clouds[x][y] = 1
                        board[x][y] -= 2
                    } else {
                        clouds[x][y] = 0
                    }
                } else if (clouds[x][y] == 1) {
                    clouds[x][y] = 0
                }
            }
        }
    }

    var result = 0
    board.forEach { line ->
        result += line.sum()
    }
    println(result)
}

fun repairPosition(target: Int, n: Int): Int {
    return if (target < 0) {
        if (target % n == 0)
            0
        else
            n + (target % n)
    } else if (target >= n) {
        target % n
    } else target
}

fun createEmptyCloud(n: Int): Array<Array<Int>> {
    var newEmptyCloud: Array<Array<Int>> = arrayOf()

    for (i in 1..n) {
        var cloudArray = arrayOf<Int>()
        for (j in 1..n) {
            cloudArray = cloudArray.plus(0)
        }
        newEmptyCloud = newEmptyCloud.plus(cloudArray)
    }

    return newEmptyCloud
}
