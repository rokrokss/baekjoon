import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (x, y, w, h) = br.readLine().split(" ").map { it.toInt() }
    println(min(abs(x - w), min(abs(x), min(abs(y - h), abs(y)))))
}
