class Class
  def attr_accessor_with_history(attr_name)
    attr_name = attr_name.to_s # make sure it's a string 
    attr_reader attr_name # create the attribute's getter 
    attr_reader attr_name+"_history" # create bar_history getter 
    class_eval "def #{attr_name}= val 
                  @#{attr_name} = val
                  puts 'I am assigning' + val.to_s
                  if @#{attr_name}_history == nil then
                    @#{attr_name}_history = [nil] << val
                  else
                    @#{attr_name}_history << val
                  end
                end"
  end
end

class Foo
  attr_accessor_with_history :bar
  attr_accessor_with_history :x
end
=begin
f = Foo.new
f.bar = 1
f.bar = 2
f.x = 4
f.x = 5
puts f.bar_history.inspect # => if your code works, should be [nil,1,2]
puts f.x_history.inspect

=end

# ===================================


class Numeric
  @@currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019}
  def method_missing(method_id)
    singular_currency = method_id.to_s.gsub( /s$/, '')
    if @@currencies.has_key?(singular_currency)
      self * @@currencies[singular_currency]
    else
     super 
    end
  end
end

puts 10.rupee
