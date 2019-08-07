import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val arr = br.readLines().map { it.toInt() }
    var idx = 1
    var max = arr[0]
    for (i in 1..8) {
        if (arr[i] > max) {
            idx = i + 1
            max = arr[i]
        }
    }
    println("$max\n$idx")
}
