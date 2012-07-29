import java.util.LinkedHashMap
import scala.collection.JavaConversions._

object FindPrime {

  var items   = new LinkedHashMap[Int, Boolean]()

  def main(args: Array[String]) {
    findAllPrime( 2000000)
  }

  def findAllPrime(size: Int): Unit = {
    // Prepare
    for (i <- 2 until size + 1)
      items.put(i, true)

    // Mark prime
    for (item <- items if items.get(item) == true) markPrime(item)
    
    // Calculate sum
    var sum = 0
    var count = 0
    for (item <- items if markers(item - 2) == false)  {
      sum = sum + item
      count = count + 1
      println("item: " + item)
    }
    println("Count: " + count)
    println("Grand total: " + sum)
  }

  def markPrime(in: Int) {
   var count = 2
   var item = in * count

   var max = items.get(item)

   while (item <= max) {
     markers(item - 2) = true
     count = count + 1
     item = in * count
   }
  }
}
