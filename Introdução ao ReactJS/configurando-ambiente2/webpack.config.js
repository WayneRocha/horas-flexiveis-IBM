const path = require('path');

module.exports = {
    entry: './src/index.js',
    ouput: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundler.js'
    }
}