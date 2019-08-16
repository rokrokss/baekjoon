import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val r = br.readLine().toDouble()
    println("%.6f".format(PI * r.pow(2)))
    println("%.6f".format(r.pow(2) * 2))
}
