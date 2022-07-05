/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    '/salttohtml/template/*.html',
    '/salttohtml/template/**/*.html',
    '/static/**/*.js',
  ],
  theme: {
    colors: {
      'main': '#92B4EC',
      'white': '#FFFFFF',
      'gray': '#EFEFEF',
      'dark': '#444444',
      'black': '#000000',
      'button': '#FFD24C',
      'blue': '#242F9B',
    },
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    // * comment if build:css error
    // require('@tailwindcss/forms'),
  ],
  purge: {
    enabled: true,
    content: [
      'salttohtml/template/*.html',
      'salttohtml/template/**/*.html',
    ],
  },
}
