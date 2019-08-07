import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (h, m) = br.readLine().split(" ").map { it.toInt() }
    val hDown = h == 0
    val mDown = m < 45
    println(
            when {
                hDown && mDown -> "23 ${m + 15}"
                !hDown && mDown -> "${h - 1} ${m + 15}"
                else -> "$h ${m-45}"
            }
    )
}
