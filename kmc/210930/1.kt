// 쿠키의 신체 측정

fun main() {
    val n = readLine()!!.toInt()

    var head: Int? = null
    var heart: Pair<Int, Int>? = null
    var leftArm = 0
    var rightArm = 0
    var waist = 0
    var startLeftLeg: Pair<Int, Int>? = null
    var leftLeg = 0
    var rightLeg = 0

    for (i in 1..n) {
        val line = readLine()!!

        if (head == null) { // head
            val idx = line.indexOf("*")
            if (idx != -1)
                head = idx
        } else if (heart == null) { // heart & arm
            if (line.contains("***")) {
                heart = Pair(i, head)
                leftArm = head - line.subSequence(0, head).indexOf("*")
                rightArm = line.lastIndexOf("*") - head
            }
        } else if (startLeftLeg == null) { // waist
            if (line.contains("*_*")) {
                waist = (i - 1) - heart.first
                startLeftLeg = Pair(i, line.indexOf("*"))
                leftLeg = 1
                rightLeg = 1
            }
        } else { // leg
            if (line.contains("*_*")) { // *_*
                leftLeg += 1
                rightLeg += 1
            } else if (line.indexOf("*") == startLeftLeg.second) // *__
                leftLeg += 1
            else if (line.indexOf("*") != -1) // __*
                rightLeg += 1
            else // ___
                break
        }
    }
    println("${heart!!.first} ${heart.second + 1}")
    println("$leftArm $rightArm $waist $leftLeg $rightLeg")
}
