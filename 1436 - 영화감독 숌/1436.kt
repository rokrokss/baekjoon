import java.io.BufferedReader
import java.io.InputStreamReader


fun hasSixes(_n : Int) : Boolean {
    var n = _n
    var cnt = 0
    var _cnt = 0
    while (n > 0)
    {
        if (n % 10 == 6)
            _cnt++
        else
        {
            cnt = Math.max(cnt, _cnt)
            _cnt = 0
        }
        n /= 10
    }
    cnt = Math.max(cnt, _cnt)
    return cnt > 2
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var cnt = br.readLine().toInt()
    var i = 666
    while (true)
    {
        if (hasSixes(i))
            cnt--
        if (cnt == 0)
        {
            println(i)
            return
        }
        i++
    }
}

