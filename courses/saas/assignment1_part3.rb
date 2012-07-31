=begin
# input:
['cars', 'for', 'potatoes', 'racs', 'four','scar', 'creams', 'scream']
#  => output:  [["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"],
["creams", "scream"]]
# HINT: you can quickly tell if two words are anagrams by sorting their
#  letters, keeping in mind that upper vs lowercase doesn't matter
=end

def combine_anagrams(words)
  initial    = {}
  prepared   = {}
  result = []
  # Prepare the hash with sorted characters as value
  words.each { |w| initial[w] = w.downcase.chars.sort.join } 
  # Group the values in previous step into arrays with unique keys
  initial.each_pair { |k, v| (prepared[v] == nil) ? prepared[v] = [k] : prepared[v] << k }   
  # Extract the group of arrays and add it to result
  prepared.each_value { |v| result << v}

  return result
end
# FIXME What do you do for duplicate values? :P
puts (combine_anagrams ['cars', 'for', 'potatoes', 'cars', 'racs', 'four','scar', 'creams', 'scream']).inspect


