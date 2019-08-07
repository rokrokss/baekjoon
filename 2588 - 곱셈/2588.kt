import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val m = br.readLine()
    for (i in 2 downTo 0)
        println(n * (m[i].toInt() - 48))
    println(n * m.toInt())
}
