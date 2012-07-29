# TODO: Unit tests.
def palindrome? input 
  input.downcase!
  input.gsub!(/[^\w]/, "")
  input == input.reverse
end



def count_words(input)
  result = {}
  input.downcase!
  parts = input.split
  parts.each { |w| result[w] = parts.count w if w.match(/[a-z]+/)}
  result
end


