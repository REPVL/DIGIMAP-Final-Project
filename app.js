const express = require('express')
const handlebars = require('hbs')
const routes = require('./routes/routes.js')
const app = express()

app.set('view engine', 'hbs')
handlebars.registerPartials(__dirname + './views/partials')

app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))
app.use('/', routes)

app.listen(8080, () => {
  console.log('Server is running at localhost:8080')
})