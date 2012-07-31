=begin
# input:
['cars', 'for', 'potatoes', 'racs', 'four','scar', 'creams', 'scream']
#  => output:  [["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"],
["creams", "scream"]]
# HINT: you can quickly tell if two words are anagrams by sorting their
#  letters, keeping in mind that upper vs lowercase doesn't matter
=end

def combine_anagrams(words)
  prepared = {}
  words.each { |w| prepared[w] = w.downcase.chars.sort.join }
  prepared.each_pair {}  
  puts prepared
end

combine_anagrams ['cars', 'for', 'potatoes', 'racs', 'four','scar', 'creams', 'scream']