import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val m = br.readLine().split(" ")[1].toInt()
    val a = br.readLine().split(" ").map { it.toInt() }.filter { it < m }.toIntArray()
    var s = 0
    var tmp: Int
    val size = a.size
    for (i in 0..size-3) {
        for (j in i+1..size-2) {
            for (k in j+1..size-1) {
                tmp = a[i] + a[j] + a[k]
                if (tmp in s..m) s = tmp
            }
        }
    }
    println(s)
}
