/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

module.exports = {
  content: ["./dddashboard/**/*.{html,js}"],
  theme: {
    colors: colors,
    extend: {},
  },
  plugins: [],
}

