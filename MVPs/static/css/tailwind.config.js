/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./MVPs/templates/**/*.html",
    "./MVPs/static/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
