import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val ws = IntArray(n)
    val hs = IntArray(n)
    val rank = IntArray(n, { 1 })
    for (i in 0..n-1)
    {
        var (w, h) = br.readLine().split(' ').map { it -> it.toInt() }
        ws[i] = w
        hs[i] = h
    }
    for (i in 0..n-1)
    {
        for (j in 0..n-1)
        {
            if(ws[i] > ws[j] && hs[i] > hs[j])
            {
                rank[j]++;
            }
        }
    }
    println("${rank.joinToString(" ")}")
}

