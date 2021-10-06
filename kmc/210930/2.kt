// 빗물

fun main() {
    val w = readLine()!!.split(" ").last().toInt()
    val field = readLine()!!.split(" ").map { it.toInt() }

    var result = 0

    width@ for (x in 0 until w) {
        height@ for (y in 1..field[x]) {
            var cnt = 0
            count@ for (i in x + 1 until w) {
                if (field[i] < y) // empty space
                    cnt += 1
                else {
                    result += cnt // found block : empty space => water space
                    continue@height
                }
            }
            break@height // not found block : empty space => just empty
        }
    }
    print(result)
}
