import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.*

fun expdist(x: List<Double>, y: List<Double>): Double {
    return (x[0] - y[0]).pow(2) + (x[1] - y[1]).pow(2)
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val a = br.readLine().split(" ").map { it.toDouble() }
    val b = br.readLine().split(" ").map { it.toDouble() }
    val c = br.readLine().split(" ").map { it.toDouble() }
    val ab = expdist(a, b)
    val bc = expdist(b, c)
    val ca = expdist(c, a)
    val hypotenuse = max(ab, max(bc, ca))
    when(hypotenuse) {
        ab -> println("${(a[0] + b[0] - c[0]).toInt()} ${(a[1] + b[1] - c[1]).toInt()}")
        bc -> println("${(b[0] + c[0] - a[0]).toInt()} ${(b[1] + c[1] - a[1]).toInt()}")
        else -> println("${(c[0] + a[0] - b[0]).toInt()} ${(c[1] + a[1] - b[1]).toInt()}")
    }
}
