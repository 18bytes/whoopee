class Dessert 
  def initialize name, calories
    @name = name
    @calories = calories
  end

  def healthy?
    return true if @calories < 200
    false
  end

  def delicious?
    true
  end

  def name
    @name
  end

  def name=(val)
    @name = val
  end

  def calories
    @calories
  end

  def calories=(val)
    @calories = val
  end


end


class JellyBean < Dessert
  def initialize(name, calories, flavor)
    super name, calories
    @flavor = flavor
  end

  def flavor
    @flavor
  end

  def flavor=(val)
    @flavor = val
  end

  def delicious?
    return false if @flavor == "black licorice"
    true
  end
end
