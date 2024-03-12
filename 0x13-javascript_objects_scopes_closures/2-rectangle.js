class Rectangle {
    constructor(width, height) {
        if (width > 0) {
            this.width = width;
        } else {
            throw new Error('Width must be a positive number');
        }
        if (height > 0) {
            this.height = height;
        } else {
            throw new Error('Height must be a positive number');
        }
    }
}
