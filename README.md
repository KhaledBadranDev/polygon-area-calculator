# Polygon Area Calculator

This project uses Object-Oriented Programming to calculate the area, perimeter, and other attributes of Polygons.

## Requirements

* Python 3
* No external libraries required

## Features

### Rectangle Class

* **Initialization**: `Rectangle(width, height)`
* **Methods**:
  * `set_width(width)`, `set_height(height)`
  * `get_area()`: Returns the area.
  * `get_perimeter()`: Returns the perimeter.
  * `get_diagonal()`: Returns the diagonal length.
  * `get_picture()`: Returns a string visualization using `*`.
  * `get_amount_inside(shape)`: Calculates how many times another shape fits inside.

### Square Class

* **Initialization**: `Square(side)`
* **Inheritance**: Inherits all methods from `Rectangle`.
* **Methods**:
  * `set_side(side)`: Updates both width and height.
  * `set_width(side)`, `set_height(side)`: Overridden to maintain square geometry.

## Usage

Run the main script to see examples:

```bash
python main.py
```

## License

This project is licensed under the [MIT License](LICENSE).
