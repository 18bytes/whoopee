class CartesianProduct
  include Enumerable
  def initialize(first, second)
    @first, @second = first, second
  end

  def each
    @first.each { |a| @second.each { |b| yield [a, b]}}
  end 
end
=begin
  
#Examples of use
c = CartesianProduct.new([:a,:b], [4,5])
c.each { |elt| puts elt.inspect }
# [:a, 4]
# [:a, 5]
# [:b, 4]
# [:b, 5]
c = CartesianProduct.new([:a,:b], [])
c.each { |elt| puts elt.inspect }
# (nothing printed since Cartesian product
# of anything with an empty collection is empty)

=end
