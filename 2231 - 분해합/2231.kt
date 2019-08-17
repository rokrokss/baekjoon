import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    var sum: Int
    var it: Int
    for (i in 1..n) {
        sum = i
        it = i
        while (it > 0) {
            sum += it % 10
            it /= 10
        }
        if (sum == n) {
            println(i)
            return
        }
    }
    println(0)
}
