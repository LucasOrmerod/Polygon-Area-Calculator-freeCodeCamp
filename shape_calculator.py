class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    pic_str = ""
    height_remaining = self.height
    width_remaining = self.width
    while height_remaining > 0:
      while width_remaining > 0:
        pic_str += "*"
        width_remaining -= 1
      pic_str += "\n"
      height_remaining -= 1
      width_remaining = self.width
    return pic_str

  def get_amount_inside(self, shape):
    times_shape_fits = int((self.width / shape.width) * (self.height / shape.height))
    if (times_shape_fits > 0):
      return times_shape_fits
    else:
      return 0
    
class Square(Rectangle):
  def __init__(self, sides):
    super().__init__(sides, sides)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, sides):
    super().set_width(sides)
    super().set_height(sides)

  def set_width(self, width):
    super().set_width(width)
    super().set_height(width)

  def set_height(self, height):
    super().set_width(height)
    super().set_height(height)