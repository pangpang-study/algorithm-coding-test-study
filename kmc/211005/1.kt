import kotlin.math.abs

var n = 0
var numbers: List<Int> = emptyList()
var operators: Array<Int> = emptyArray()
var maxResult = -1000000001
var minResult = 1000000001

fun main() {
    n = readLine()!!.toInt()
    numbers = readLine()!!.split(" ").map { it.toInt() }
    operators = readLine()!!.split(" ").map { it.toInt() }.toTypedArray()

    dfs(numbers.first(), 1)

    println(maxResult)
    println(minResult)
}

fun dfs(curResult: Int, idx: Int) {
    if (idx == n) {
        if (curResult > maxResult)
            maxResult = curResult
        if (curResult < minResult)
            minResult = curResult
    } else {

        for (op in 0..3) {
            if (operators[op] > 0) {
                var newResult = curResult

                if (op == 0)
                    newResult += numbers[idx]

                if (op == 1)
                    newResult -= numbers[idx]

                if (op == 2)
                    newResult *= numbers[idx]

                if (op == 3) {
                    if (newResult < 0)
                        newResult = -(abs(newResult)) / numbers[idx]
                    else
                        newResult /= numbers[idx]
                }

                operators[op] -= 1
                dfs(newResult, idx + 1)
                operators[op] += 1
            }
        }
    }
}
