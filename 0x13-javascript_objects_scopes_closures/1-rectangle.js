#!/usr/bin/env node

// Define the class
class Rect {
  // Constructor with width and height
  constructor(width, height) {
    this._width = width;
    this._height = height;
  }

  // Getter for width
  get width() {
    return this._width;
  }

  // Setter for width
  set width(newWidth) {
    this._width = newWidth;
  }

  // Getter for height
  get height() {
    return this._height;
  }

  // Setter for height
  set height(newHeight) {
    this._height = newHeight;
  }
}

// Export the class
module.exports = Rect;
